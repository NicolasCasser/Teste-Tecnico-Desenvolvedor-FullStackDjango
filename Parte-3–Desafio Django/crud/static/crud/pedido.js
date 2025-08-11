document.addEventListener('DOMContentLoaded', () => {
  const produtos = document.querySelectorAll('input[name="produtos"]');
  const totalElement = document.getElementById('valor-total');

  function atualizarTotal() {
    let total = 0;
    produtos.forEach(produto => {
      if (produto.checked) {
        const preco = parseFloat(produto.dataset.preco.replace(',', '.'));
        if (!isNaN(preco)) {
          total += preco;
        }
      }
    });
    totalElement.textContent = total.toFixed(2).replace('.', ',');
  }

  produtos.forEach(produto => {
    produto.addEventListener('change', atualizarTotal);
  });

  atualizarTotal();
});
