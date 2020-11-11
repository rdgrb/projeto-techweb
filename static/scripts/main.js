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
        $("#colocacao-modal").removeClass("text-info text-warning text-success text-danger")
        $("#vitorias-modal").html(time.vitorias);
        $("#empates-modal").html(time.empates);
        $("#derrotas-modal").html(time.derrotas);

        $("#saldo-gols-modal").html(time.saldo_gols);
        $("#gols-pro-modal").html(time.gols_pro);
        $("#gols-contra-modal").html(time.gols_contra);

        $("#amarelo-modal").html(time.cartoes_amarelos);
        $("#vermelho-modal").html(time.cartoes_vermelhos);

        $("#pontos").html(`Pontos: ${time.pontos}`);

        let classificado = "";
        switch(checar_classificacao(parseInt($id) + 1)) {
            case "libertadores":
                classificado = "Classificando para fase de grupos Libertadores"; 
                $("#colocacao-modal").addClass("text-info");
                break; 
            case "qualify-libertadores":
                classificado = "Classificando para qualificatórias da Libertadores";
                $("#colocacao-modal").addClass("text-warning");
                break;
            case "sul-americana":
                classificado = "Classificando para fase de grupos da Copa Sul-Americana";
                $("#colocacao-modal").addClass("text-success");
                break; 
            case "rebaixamento": 
                classificado = "Na zona de rebaixamento";
                $("#colocacao-modal").addClass("text-danger");
                break;
            default: 
                classificado = "Jogando o Brasileirão - Série A";
                $("#colocacao-modal").addClass("text-black");
                break;
        }

        $("#campeonato-modal").html(classificado);
        $("#modalDetalhes").modal('show');

        console.log(time);
    })
})

const checar_classificacao = classificacao => {
    const classificacoes = {
        1: "libertadores", 
        2: "libertadores",
        3: "libertadores", 
        4: "libertadores",
        5: "qualify-libertadores", 
        6: "qualify-libertadores",
        7: "sul-americana",
        8: "sul-americana",
        9: "sul-americana",
        10: "sul-americana",
        11: "sul-americana",
        12: "sul-americana",
        17: "rebaixamento",
        18: "rebaixamento",
        19: "rebaixamento",
        20: "rebaixamento",
    }

    return classificacoes[classificacao]
    ? classificacoes[classificacao]
    : "brasileirao" 
}