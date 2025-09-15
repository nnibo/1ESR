const BotaoIncrementar = ({onIncrementar, onReduzir}) => {
    return (
        <>
            <button onClick={onIncrementar}>Adicionar</button>
            <button onClick={onReduzir}>Reduzir</button>
        </>
    )
}

export default BotaoIncrementar