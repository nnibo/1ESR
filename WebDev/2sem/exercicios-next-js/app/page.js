"use client";

import BotaoAcaoEx7 from './components/BotaoAcaoEx7';
import CardEx4 from './components/CardEx4';
import HelloEx2 from './components/HelloEx2'
import SaudacaoEx6 from './components/SaudacaoEx6';
import BadgeEx9 from './components/BadgeEx9'
import CardEx10 from './components/CardEx10';
import CardHeaderEx10 from './components/CardHeaderEx10';
import CardBodyEx10 from './components/CardBodyEx10';

export default function Home() {
  // Lista Exercicio 5
  const itens = ['Chuteira', 'Cama', 'Mesa']

  // Lista Exercicio 6
  const nomes = ['Nicolas','Bruno', 'Jota']

  // Funcao Exercicio 7
  const handleClick = () => {
    alert('Voce clicou no botao')
  }

  // Lista Objetos Exercicio 8
  const alunos = [{id: 1, nome: "Nicolas"}, {id: 2, nome: "Bruno"}, {id: 3, nome: "Jota"}]


  return (
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

    <CardEx10>
      <CardHeaderEx10><h1>Card Exemplo</h1></CardHeaderEx10>
      <CardBodyEx10><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim, illo?</p></CardBodyEx10>
    </CardEx10>

  );
}
