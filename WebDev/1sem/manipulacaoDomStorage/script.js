// // console.log('hello world');

// const titulo = document.querySelector('h1')
// titulo.textContent = 'Novo titulo'

// const div = document.querySelector('#container')
// div.innerHTML = '<p>Novo paragrafo <b>HTML</b></p>'

// const imagem = document.querySelector('img')
// imagem.setAttribute('src', 'images/pngtree-cartoon-color-simple-male-avatar-png-image_1934459.jpg')
// // imagem.src = 'caminho da imagem'
// imagem.setAttribute('width', '200px')
// imagem.setAttribute('alt', 'Avatar profile')
// // imagem.alt = 'xxxxxxx'
// // setAttribute(passar o elemento, o que vai ser digitado)

// const caixa = document.querySelector('.box')
// const botao = document.getElementById('meuBotao')

// botao.addEventListener("click", () => {
//     caixa.classList.toggle('oculta')
// } )
// // Estilizando uma div
// // caixa.style.width = '200px'
// // caixa.style.height = '200px'
// // caixa.style.backgroundColor = 'lightgreen'
// // caixa.style.border = '10px solid black'

// const novoItem = document.createElement('li')
// novoItem.textContent = 'Novo item'
// const novoItem2 = document.createElement('li')
// novoItem2.textContent = 'Novo item 2'

// document.querySelector('ul').appendChild(novoItem)
// document.querySelector('ul').appendChild(novoItem2)

// localStorage.setItem('nome', 'Daniel')
// localStorage.setItem('nome2', 'Felipe')

// const nome = localStorage.getItem('nome')
// console.log(nome);

// // localStorage.removeItem('nome2')
// // localStorage.clear()

// const usuario = {
//     nome: 'Daniel',
//     idade: 35
// }

// //JSON.stringify faz o objeto virar string
// localStorage.setItem('usuario', JSON.stringify(usuario))

// //JSON.parse faz a string virar objeto novamente
// const usuarioRecuperado = JSON.parse(localStorage.getItem('usuario'))

// Array para tarefas
let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];

// Função para renderizar lista
function renderizarTarefas() {
  const lista = document.getElementById("lista-tarefas");
  lista.innerHTML = "";
  tarefas.forEach((t, i) => {
    const li = document.createElement("li");
    li.textContent = t;
    lista.appendChild(li);
  });
}

renderizarTarefas();

document.getElementById("form-tarefa").onsubmit = (e) => {
  e.preventDefault();
  const input = document.getElementById("input-tarefa");
  tarefas.push(input.value);
  localStorage.setItem("tarefas", JSON.stringify(tarefas));
  input.value = "";
  renderizarTarefas();
};

document.getElementById("btn-limpar").onclick = function () {
  tarefas = [];
  localStorage.removeItem("tarefas");
  renderizarTarefas();
};

