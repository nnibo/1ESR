const listarProdutos = async() => {
    const res = await fetch('https://66429d3a3d66a67b3437cdb2.mockapi.io/products');
    const produtos = await res.json();
    const ul = document.getElementById("lista-produtos");
    ul.innerHTML = "";
  
    produtos.forEach(p => {
      const li = document.createElement("li");
      li.innerHTML = `
        <img src="${p.image}" width="50">
        <strong>${p.name}</strong> - R$ ${p.price} <em>(${p.seller})</em>
        <button id='excluir-produto' onClick='excluirProduto("${p.id}")'>Excluir</button>
      `;
      ul.appendChild(li);
    });
  }
  listarProdutos();

document.getElementById("salvar-produto").onclick = async (e) => {
    e.preventDefault()
    const name = document.getElementById('name').value.trim()
    const price = document.getElementById('price').value.trim()
    const seller = document.getElementById('seller').value.trim()

    try{
        const res = await fetch('https://66429d3a3d66a67b3437cdb2.mockapi.io/products', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            "createdAt": new Date(),
            name,
            price,
            image:"",
            seller
        })
      })

      if(res.status === 201){
        alert("Produto cadastrado com sucesso!")
        name.value = ""
        price.value = 0
        seller.value = ""
        listarProdutos();
      } else {
        alert("Houve um ou mais erros ao cadsatrar produto")
      }
    } catch(error) {
        console.log(error);
    }
    
}

const excluirProduto = async (produto) => {
    try {
        const resposta = confirm('Voce tem certeza que realmente quer excluir esse produto?')
        if(resposta){
            const res = await fetch(`https://66429d3a3d66a67b3437cdb2.mockapi.io/products/${produto}`, {
                method: 'DELETE',
            })

            if(res.status === 200){
                alert('Produto excluido com sucesso!')
                listarProdutos()
            } else {
                alert("Erro ao excluir o produto")
            }
        }
    } catch (error) {
        console.log(error);
    }
}