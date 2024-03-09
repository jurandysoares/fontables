function soma_ids() {
    valor_para = {};
    for (i=1; i<=16; i*=2) {
        valor_para['t'+i] = i;
    }

    soma = 0;
    for (var id_tabela in valor_para) {
        caixa_verificacao = document.getElementById(id_tabela);
        if (caixa_verificacao.checked) {
            soma += valor_para[id_tabela];
        }
    }

    resultado = document.getElementById('resultado');
    resultado.innerHTML = soma;
}