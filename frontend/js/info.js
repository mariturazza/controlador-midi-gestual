document.getElementById("criativo").addEventListener("click", () => {
    // novo método baseado nos ícones ativos
    const instrumentoDireita = document.querySelector(".instrumentos-direita i.active")?.id || "";
    const escalaDireita = document.querySelector(".escalas-direita i.active")?.id || "";
    const instrumentoEsquerda = document.querySelector(".instrumentos-esquerda i.active")?.id || "";
    const escalaEsquerda = document.querySelector(".escalas-esquerda i.active")?.id || "";
    const modo = document.getElementById("criativo")?.id || "";

    const dadosParaEnviar = {
        [modo]: {
                Right: {
                    instrumento: instrumentoDireita.replace("-direita", ""),
                    escala: escalaDireita.replace("-direita", "")
                },
                Left: {
                    instrumento: instrumentoEsquerda.replace("-esquerda", ""),
                    escala: escalaEsquerda.replace("-esquerda", "")
                }
        }
    };

    fetch("http://localhost:5000/receber-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dadosParaEnviar)
    });
});

document.getElementById("recreativo").addEventListener("click", () => {
    // novo método baseado nos ícones ativos
    const musica = document.querySelector(".list-music h4.active")?.id || "";
    const dificuldade = document.querySelector(".dificuldade i.active")?.id || "";
    const modo = document.getElementById("recreativo")?.id || "";

    const dadosParaEnviar = {
        [modo]: {
                musica: musica,
                dificuldade: dificuldade
        }
    };

    fetch("http://localhost:5000/receber-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dadosParaEnviar)
    });
});