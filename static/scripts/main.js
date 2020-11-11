$(document).ready(() => {
    $(".linha-time").on('click', (event) => {
        const $id = event.currentTarget.id; 
        const id = `#${$id}`;

        let nome_time = $(id).children(".nome_time").text();

        const time = {
            "logo": $(id).children(".nome_time").children(".logo-time").attr('src'),
            "nome": nome_time.trim().replace(/\s/g, "_"),
            "pontos": $(id).children(".pontos").text(), 
            "vitorias": $(id).children(".vitorias").text(),
            "empates": $(id).children(".empates").text(),
            "derrotas": $(id).children(".derrotas").text(),
            "saldo_gols": $(id).children(".saldo_gols").text(),
            "gols_pro": $(id).children(".gols_pro").text(),
            "gols_contra": $(id).children(".gols_contra").text(),
            "cartoes_amarelos": $(id).children(".cartoes_amarelos").text(),
            "cartoes_vermelhos": $(id).children(".cartoes_vermelhos").text()
        }

        $("#logo-modal").attr("src", time.logo);
        $("#titulo-modal").html(time.nome.replace("_", " "));
        $("#colocacao-modal").html(`${parseInt($id) + 1}º`);
        $("#vitorias-modal").html(time.vitorias);
        $("#empates-modal").html(time.empates);
        $("#derrotas-modal").html(time.derrotas);

        $("#saldo-gols-modal").html(time.saldo_gols);
        $("#gols-pro-modal").html(time.gols_pro);
        $("#gols-contra-modal").html(time.gols_contra);

        $("#amarelo-modal").html(time.cartoes_amarelos);
        $("#vermelho-modal").html(time.cartoes_vermelhos);

        $("#pontos").html(`Pontos: ${time.pontos}`)
        $("#modalDetalhes").modal('show');

        console.log(time);
    })
})