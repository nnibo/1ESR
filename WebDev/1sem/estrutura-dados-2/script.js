// Tipos de array

/*  
const tarefas = ['Estudar js', 'Criar projeto', 'Preparar apresentacao', 'Revisar codigo']
console.table(tarefas)

const categorias = new Array('Trabalho','Estudo','Pessoal','Projetos')
console.table(categorias)

const propriedades = Array.of('baixa', 'media', 'alta')
console.table(propriedades)

const letras = Array.from('Daniel')
console.table(letras)
*/

// -------------------------------------------------------------------------------------------

// Alterando valores nos indices do array

/* 
const tarefas = ['Estudar js', 'Criar projeto', 'Preparar apresentacao', 'Revisar codigo']
console.table(tarefas)
console.log(tarefas[0]);

tarefas[1] = 'Criar projeto novo'
console.table(tarefas)

tarefas.push('Relizar testes') // .push adiciona o elemento ao fim do array
console.table(tarefas);

tarefas.unshift('Revisar documentacao') // .unshift adiciona o elemento no inicio do array
console.table(tarefas)

tarefas.shift() // .shift remove o primeiro elemento do array
console.table(tarefas)

tarefas.pop() // .pop remove o ultimo elemento do array
console.table(tarefas)

tarefas.splice(1, 2, 'Pinto', 'Pau') // recebe o indice e quantos elementos ele remove
console.table(tarefas)
*/

// -------------------------------------------------------------------------------------------

// Funcoes Callback

/* 
const tarefas = ['Estudar js', 'Criar projeto', 'Preparar apresentacao', 'Revisar codigo']

const executarForEach = (elemento, indice) => {
    console.log(`${indice + 1}. ${elemento} `)
} // O .forEach não altera os elementos do array, porem passa por todos eles
tarefas.forEach(executarForEach)

const arrayNovo =  tarefas.map((elemento, indice) => {
    return elemento + ' - Concluido'
}) // O .map percorre por todos os elementos, e consegue alterar eles também
console.table(arrayNovo)

const tarefasComA = tarefas.filter(elemento => elemento.toLowerCase().includes('a'))
console.log(tarefasComA); // Filter sempre retorna um array com elementos com base na regra

const tarefaEncontrada = tarefas.find(elemento => elemento.includes('a'))
console.log(tarefaEncontrada); // Retorna o primeiro elemento que ele achar com base na regra

const indiceTarefaEncontrada = tarefas.findIndex(elemento => elemento.includes('p'))
console.log(indiceTarefaEncontrada);

tarefas.splice(indiceTarefaEncontrada, 1)
console.log(tarefas);

const valorFinal = tarefas.reduce((total, t) => {
    total + t.lenght, 0
})
console.log(valorFinal);

*/

// -------------------------------------------------------------------------------------------

// Manipulando arrays e objetos
/* 
const tarefa = {
    id: 1,
    titulo: 'Aprender sobre objetos',
    descricao: 'Estudar propriedades e metodos',
    concluida: false,
    propriedade: 'alta',
    dataCriacao: new Date()
}
console.log(tarefa);

//Acessando titulo
console.log(tarefa?.titulo); 
console.log(tarefa['titulo']);

const tarefasEspeciais = {
    "data-criacao": new Date(),
    "nome da tarefa": 'nome da tarefa separado'
}
console.log(tarefasEspeciais["data-criacao"]);
console.log(tarefasEspeciais["nome da tarefa"]);
*/

// -------------------------------------------------------------------------------------------

// Manipulando Objeto e criando funcoes

/* 
const projetoTaskMaster = {
    nome: "TaskMaster",
    version: "1.0",
    autor: "Curso JavaScript",
    tarefas: [],
    adicionarTarefa(titulo, prioridade = "média") {
      const novaTarefa = {
        id: this.tarefas.length + 1,
        titulo,
        prioridade,
        concluida: false,
        criada: new Date()
      };
      this.tarefas.push(novaTarefa);
      console.log(`Tarefa "${titulo}" adicionada.`);
      return novaTarefa;
    },
    listarTarefas() {
      console.log(`Projeto ${this.nome} - Lista de Tarefas:`);
      this.tarefas.forEach(t => console.log(`- ${t.id}: ${t.titulo} (${t.prioridade})`));
    }
  };
  
  projetoTaskMaster.adicionarTarefa("Estudar Objetos", "alta");
  projetoTaskMaster.adicionarTarefa("Criar interface");
  projetoTaskMaster.listarTarefas();

console.log(Object.keys(projetoTaskMaster)) // pega as chaves do objeto
console.log(Object.values(projetoTaskMaster)) // pega os valores dos objetos
*/

// -------------------------------------------------------------------------------------------

// Desestruturação e Spread Operator
/* 
const prioridades = ['baixa', 'media', 'alta']
const [baixa, media, alta] = prioridades 

console.log(baixa, media, alta);

const categorias = ['Trabalho', 'Estudo', 'Pessoal', 'Saude']
console.log(categorias);

const [primeiraCategoria, ...outrasCategorias] = categorias

console.log(primeiraCategoria, outrasCategorias);

const projetoTaskMaster = {
    nome: 'TaskMaster',
    version: '1.0',
    autor: 'Curso javascript',
    tarefas: []
}

const {nome, version, autor, tarefas} = projetoTaskMaster
console.log(nome, version, alta, tarefas);

const {nome2, version2, ...outrasProps} = projetoTaskMaster
console.log(nome2, version2, outrasProps);
*/
// -------------------------------------------------------------------------------------------
