// console.log('hello world');

// let titulo = 'aprender javascript'
// let descricao = 'estudar maniulacao de strings'

// console.log(titulo, typeof(titulo));
// console.log(descricao, typeof(descricao));

// console.log('Tamanho da variavel titulo: ', titulo.length);
// console.log('Tamanho da variavel titulo: ', descricao.length);

// console.log('primeiro caractere: ', titulo[0]);
// console.log('primeiro caractere: ', descricao[0]);

// console.log('ultimo caractere: ', titulo.length -1);

// const palavra = 'palavra'
// console.log('caractere na posição 3:', palavra.charAt(3));

// --------------------------------------------------------------------------------------------------

// let titulo = 'aprender javascript'
// let categoria = 'estudo'

// let infoCompleta = 'categoria: '  + categoria + ' - ' + titulo
// console.log(infoCompleta);

// let infoCompleta2 = `Categoria: ${categoria} - ${titulo}`
// console.log(infoCompleta2);

// --------------------------------------------------------------------------------------------------

// let texto1 = 'posicao de javascript'
// console.log(texto1.indexOf('javascript'));

// console.log(texto1.includes('javascript')); // True, no texto tem javascript

// console.log(texto1.startsWith('posicao')); // True, o texto começa com posicao

// console.log(texto1.endsWith('javascript')); // True, o texto termina com javascript

// --------------------------------------------------------------------------------------------------

// const truncarDescricao = (texto, maxLenght = 30) => {
//     if(texto.length <= maxLenght) {
//         return texto
//     }
//     return texto.substring(0, maxLenght) + '...'
// }

// let descricaoLonga = 'abcdefghijklmnopqrstuvwxyz123456789101112'

// console.log(truncarDescricao(descricaoLonga));

// --------------------------------------------------------------------------------------------------

// let texto = 'javascript,programacao,web,frontend'
// console.log('texto original: ', texto);

// console.log('texto slice: ', texto.slice(0, 10));

// console.log('texto substring: ', texto.substring(0, 10));

// let arrayTags = texto.split(',') // array: palavra separada em virgulas
// console.log(arrayTags);
// console.table(arrayTags);

// console.log(arrayTags.join(',')); // array de volta pra texto

// --------------------------------------------------------------------------------------------------

// const destacarTermo = (texto, termo) => {
//     if(!termo) return texto
//     const regex = new RegExp(termo, 'gi')

//     return texto.replace(regex, '**$&**')
// }

// let busca = destacarTermo('Javascript é uma linguagem incrivel. Amo javascript!', 'javascript')
// console.log(busca);

// --------------------------------------------------------------------------------------------------

// console.log('Math.PI: ', Math.PI);
// console.log('Math.E: ', Math.E);

// const raio = 5

// const areaCirculo = Math.PI * Math.pow(raio, 2)
// console.log('Area do circulo:', areaCirculo);

// const numero = 9.2
// console.log(Math.round(numero)); // se o numero for a partir de 9.5, arredonda pra 10
// console.log(Math.floor(numero)); // arredonda sempre pra baixo
// console.log(Math.ceil(numero)); // não importa o decimal do numero, sempre arredonda pra cima
// console.log(Math.trunc(numero)); // tira a casa decimal

// const numeroAleatorioEntre = (min, max) => {
//     return Math.floor(Math.random() * (max - min + 1)) + min
// }

// console.log(numeroAleatorioEntre(1, 100));

// --------------------------------------------------------------------------------------------------

// const hoje = new Date()
// console.log(hoje);

// console.log(new Date('2025-06-15T10:30:00'));

// const dataComponentes = new Date(2025, 5, 15, 10, 30, 0)
// console.log(dataComponentes);

// const formatarData = (data) => {
//     const dia = data.getDate()
//     const mes = data.getMonth() + 1
//     const ano = data.getFullYear()

//     return `${dia}/${mes}/${ano}`
// }

// console.log(formatarData(hoje));

// const adicionarDias = (data, dias) => {
//     const novaData = new Date(data)

//     novaData.setDate(data.getDate() + dias)

//     return novaData
// }
// console.log(adicionarDias(hoje, 3).toString());
// console.log(adicionarDias(hoje, 10).toString());
// console.log(adicionarDias(hoje, 30).toString());
// console.log(adicionarDias(hoje, 365).toString());

// const dataFinal = new Date('05-11-2025')

// const diferencaMs = dataFinal - hoje
// console.log(diferencaMs);

// const diferencaDias = Math.ceil(diferencaMs / (1000 * 60 * 60 * 24))
// console.log(diferencaDias);

// --------------------------------------------------------------------------------------------------