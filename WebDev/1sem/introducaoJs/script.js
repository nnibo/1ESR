//Tipos de console
/*
    console.log('hello world')
    console.info('info');
    console.warn('warning');
    console.error('Error');

    console.table([
        {
            id: 1,
            tarefa: 'estudar js'
        },
        {
            id: 2,
            tarefa: 'Praticar codigo'
        }
    ])

    console.group("Grupo de logs")
    console.log('Log1');
    console.log('Log2');
    console.groupEnd()

    console.time('Timer')
    if(1 == 2){
        console.log('nao')
    }
    console.timeEnd('Timer')
*/


//comentario de 1 linha

/* 
    comentario de
    varias linhas
*/


//Tipos de variaveis
/*
    var antigo = 'valor da variavel'
    console.log(antigo);

    let variavelMutavel = 'valor que pode ser alterado'
    console.log(variavelMutavel);
    const variavelImutavel = 'valor que não pode ser alterado diretamente'

    variavelMutavel = 1
    console.log(variavelMutavel);

    let texto = 'Texto';
    console.log(typeof texto)

    let numero = 1
    console.log(typeof numero);

    let isCompleted = false
    console.log(typeof isCompleted);

    let semValor
    console.log(typeof semValor);

    let nulo = null
    console.log(typeof nulo);

    let uniqueId = Symbol('id')
    console.log(typeof uniqueId);

    let bigNumero = 999999999999n
    console.log(typeof bigNumero);
*/

// Tipos de dados complexos
/* 
    let tarefa = {id: 1, tarefa: 'estudar js'}
    console.log(tarefa.id);
    console.log(tarefa.tarefa);

    let tarefas = [
        {id: 1, tarefa: 'Estudar nodeJS'},
        {id: 2, tarefa: 'Praticar codigo'}
    ]
    console.log(tarefas);
    console.log(tarefas[0]);
    console.log(tarefas[0]['id']);

    let hoje = new Date()
    console.log(hoje);

    //Expressao regular
    let pattern = /^[a-z]+$/i
    console.log(pattern);
*/