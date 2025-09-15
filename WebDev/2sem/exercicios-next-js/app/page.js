"use client";
import {use, useEffect, useState} from 'react';
import BotaoAcaoEx7 from './components/BotaoAcaoEx7';
import CardEx4 from './components/CardEx4';
import HelloEx2 from './components/HelloEx2'
import SaudacaoEx6 from './components/SaudacaoEx6';
import BadgeEx9 from './components/BadgeEx9'
import CardEx10 from './components/CardEx10';
import CardHeaderEx10 from './components/CardHeaderEx10';
import CardBodyEx10 from './components/CardBodyEx10';
import BotaoIncrementar from './components/BotaoIncrementar';

export default function Home() {
  // Lista Exercicio 5
  // const itens = ['Chuteira', 'Cama', 'Mesa']

  // Lista Exercicio 6
  const nomes = ['Nicolas','Bruno', 'Jota']

  // Funcao Exercicio 7
  const handleClick = () => {
    alert('Voce clicou no botao')
  }

  // Lista Objetos Exercicio 8
  const alunos = [{id: 1, nome: "Nicolas"}, {id: 2, nome: "Bruno"}, {id: 3, nome: "Jota"}]

  const [valor, setValor] = useState(0)

  // Exercicio 1 - Estado e Hooks
  const incrementar = () => {
    setValor(prev => prev + 1)
  }

  const reduzir = () => {
    setValor(prev => prev - 1)
  }

  // Exercicio 2 - Estado e Hooks
  // const [hora, setHora] = useState(new Date)

  // useEffect(() => {
  //   const id = setInterval(() => setHora(new Date), 1000)
  //   return () => clearInterval(id)
  // }, [])

  // Exericio 3 - Estados e Hooks
  // const [texto, setTexto] = useState('')

  const [texto, setTexto] = useState('');
  const [itens, setItens] = useState([]);

  const adicionarTarefa = () => {
    const t = texto
    setItens(prev => [...prev, t])
    setTexto('')
  }
  return (
    <div>
      <input type="text" value={texto} onChange={e => setTexto(e.target.value)} placeholder='Criar tarefa' />
      <button onClick={adicionarTarefa}>Adicionar Tarefa</button>

      <ul>
        {itens.map((item, index) => <li key={index}>{item}</li>)}
      </ul>
    </div>

    // Exercicio 1
    // <h1>Hello World</h1>

    // ---------------------------------- 

    // Exercicio 2
    // <HelloEx2 nome="Piruzin"/>

    // ----------------------------------

    // Exercicio 4
    // <CardEx4>
    //   <h1>Titulo EX 4</h1>
    //   <p>Teste</p>
    // </CardEx4>

    // ----------------------------------

    // Exericio 5
    // <ul>
    //   {itens.map(i => <li key={i}>{i}</li>)}
    // </ul>
    
    // ----------------------------------

    // Exercicio 6
    // <>
    //   {nomes.map(nome => <SaudacaoEx6 key={nome} nome={nome}/>)}
    //   <SaudacaoEx6/>
    // </>

    // ----------------------------------

    // Exercicio 7
    // <BotaoAcaoEx7 onAcao={handleClick}>Clique aqui!</BotaoAcaoEx7>

    // ----------------------------------

    // Exercicio 8
    // <ol>
    //   {alunos.map(aluno => <li key={aluno.id}>{aluno.nome}</li>)}
    // </ol>

    // ----------------------------------

    // Exercicio 9
    // <BadgeEx9 tipo='success'>OK</BadgeEx9>

    // <CardEx10>
    //   <CardHeaderEx10><h1>Card Exemplo</h1></CardHeaderEx10>
    //   <CardBodyEx10><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim, illo?</p></CardBodyEx10>
    // </CardEx10>

    // --------------------------------
    // Ex 1 - Estados e Hooks

    // <>
    //   <p>Valor: {valor}</p>
    //   <BotaoIncrementar onIncrementar={incrementar} onReduzir={reduzir}/>
    // </>

    // --------------------------------
    // Ex 2 - Estados e Hooks
    // <p>{hora.toLocaleTimeString()}</p>

    // --------------------------------
    // Ex 3 - Estados e Hooks
    // <>
    //   <input type='text' value={texto} onChange={e => setTexto(e.target.value)} />
    //   <p>{texto}</p>
    //   <p>Contagem: {texto.length}</p>
    // </>
  );
}
