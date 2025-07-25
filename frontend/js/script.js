document.addEventListener("DOMContentLoaded", function () {
    fetch("http://localhost:5000/api/form-data")
        .then(response => response.json())
        .then(data => {
        setupSelects("instrumentos_direita", "escalas_direita", data);
        setupSelects("instrumentos_esquerda", "escalas_esquerda", data);
        })
        .catch(err => console.error("Erro ao buscar dados da API:", err));
});

function setupSelects(instrumentosSelectId, escalasSelectId, data) {
    const instrumentosSelect = document.getElementById(instrumentosSelectId);
    const escalasSelect = document.getElementById(escalasSelectId);
    const instrumentos = data.instrumentos;

    for (const instrumento in instrumentos) {
        const option = document.createElement("option");
        option.value = instrumento;
        option.textContent = instrumento.charAt(0).toUpperCase() + instrumento.slice(1);
        instrumentosSelect.appendChild(option);
    }

    // Atualizar escalas ao mudar o instrumento
    instrumentosSelect.addEventListener("change", function () {
        escalasSelect.innerHTML = '<option value="" disabled selected>Escala</option>';
        const escalas = instrumentos[this.value].escalas;

        for (const escala of escalas) {
        const option = document.createElement("option");
        option.value = escala;
        option.textContent = escala;
        escalasSelect.appendChild(option);
        }
  });
}

document.getElementById("enviar-criativo").addEventListener("click", () => {

    const instrumentoDireita = document.getElementById("instrumentos_direita").value;
    const escalaDireita = document.getElementById("escalas_direita").value;
    const instrumentoEsquerda = document.getElementById("instrumentos_esquerda").value;
    const escalaEsquerda = document.getElementById("escalas_esquerda").value;

    const dadosParaEnviar = {
        Right: {
            instrumento: instrumentoDireita,
            escala: escalaDireita
        },
        Left: {
            instrumento: instrumentoEsquerda,
            escala: escalaEsquerda
        }
    };

    fetch("http://localhost:5000/receber-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dadosParaEnviar)
    })
});