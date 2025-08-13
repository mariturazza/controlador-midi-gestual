document.querySelectorAll('.list').forEach(ul => {
  ul.addEventListener('click', function (e) {
    const clickedIcon = e.target.closest('i');
    if (!clickedIcon) return;

    ul.querySelectorAll('i').forEach(icon => icon.classList.remove('active'));

    clickedIcon.classList.add('active');
  });
});

document.querySelectorAll('.list-music').forEach(ul => {
  ul.addEventListener('click', function (e) {
    const clickedIcon = e.target.closest('h4');
    if (!clickedIcon) return;

    ul.querySelectorAll('h4').forEach(icon => icon.classList.remove('active'));

    clickedIcon.classList.add('active');
  });
});


const btnCriativo = document.getElementById("btn-criativo");
const btnVoltar1 = document.getElementById("voltar1");

const blocoInicial = document.getElementById("bloco-inicial");
const blocoCriativo = document.getElementById("bloco-criativo");

function fadeOutThenSwitch(hideEl, showEl) {

  hideEl.classList.remove("visible");
  hideEl.classList.add("hidden");

  setTimeout(() => {
    hideEl.style.display = "none";

    showEl.style.display = "flex";
    showEl.classList.remove("visible");
    showEl.classList.add("hidden");

    setTimeout(() => {
      showEl.classList.remove("hidden");
      showEl.classList.add("visible");
    }, 50);
  }, 500);
}

btnCriativo.addEventListener("click", () => {
  fadeOutThenSwitch(blocoInicial, blocoCriativo);
});

btnVoltar1.addEventListener("click", () => {
  fadeOutThenSwitch(blocoCriativo, blocoInicial);
});

const btnVoltar2 = document.getElementById("voltar2");

const btnRecreativo = document.getElementById("btn-recreativo");
const blocoRecreativo = document.getElementById("bloco-recreativo");

function fadeOutThenSwitch(hideEl, showEl) {

  hideEl.classList.remove("visible");
  hideEl.classList.add("hidden");

  setTimeout(() => {
    hideEl.style.display = "none";

    showEl.style.display = "flex";
    showEl.classList.remove("visible");
    showEl.classList.add("hidden");

    setTimeout(() => {
      showEl.classList.remove("hidden");
      showEl.classList.add("visible");
    }, 50); 
  }, 500);
}

btnRecreativo.addEventListener("click", () => {
  fadeOutThenSwitch(blocoInicial, blocoRecreativo);
});

btnVoltar2.addEventListener("click", () => {
  fadeOutThenSwitch(blocoRecreativo, blocoInicial);
});
