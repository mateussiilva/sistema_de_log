const maquinas = {
    1904: "PrismaTex",
    1604: "PrismaJet",
    1602: "Mutoh",
}
function preencherSelectMaquinas(objectMaquinas, tagHTMLSelect) {
    // let selectMaquinas = .getElementById("imaquinas")
    for (let maquina in objectMaquinas) {
        let selectMaquina = document.createElement("option");
        let valorMaquina = objectMaquinas[maquina.toString()]
        selectMaquina.value = maquina
        selectMaquina.text = valorMaquina
        tagHTMLSelect.append(selectMaquina)
    }
}
function calcularMetrosFaltantes(metros, porcentagemAtual) {
    let pCem = (porcentagemAtual / 100)
    let metrosImpressos = pCem * metros
    let metrosFaltantes = metros - metrosImpressos
    return metrosFaltantes
}
function TempoTotalImpressao(metros, idMaquina) {
    const MINUTOS = 60;
    if (idMaquina == 0) {
        let metrosMaquinaPorHora = 58
        let minutosImpressao = Math.round((metros * MINUTOS) / metrosMaquinaPorHora)
        let resultado = `${minutosImpressao} min`
        return resultado
    } else if (idMaquina == 1) {
        let metrosMaquinaPorHora = 17
        let minutosImpressao = Math.round((metros * MINUTOS) / metrosMaquinaPorHora)
        let resultado = `${minutosImpressao} min`
        return resultado

    } else if (idMaquina == 2) {
        let metrosMaquinaPorHora = 9
        let minutosImpressao = Math.round((metros * MINUTOS) / metrosMaquinaPorHora)
        let resultado = `${minutosImpressao} min`
        return resultado
    }
}
let selectMaquinas = document.getElementById("imaquinas")
preencherSelectMaquinas(maquinas, selectMaquinas)

document.addEventListener("submit", (e) => {
    e.preventDefault()
    let maquinaSelecionada = selectMaquinas.options[selectMaquinas.selectedIndex].text
    let inpPorcentagemImpressao = parseInt(document.querySelector("#iporcenteagem").value);
    //let inpPorcentagemImpressao = document.querySelector("#iporcenteagem");
    let quantidadeMetros = parseFloat(document.querySelector("#imetros").value);
    let areaTexResultado = document.querySelector("#areaResultado");

   const metrosFaltantes = calcularMetrosFaltantes(metros = quantidadeMetros, porcentagemAtual = inpPorcentagemImpressao)


    if (maquinaSelecionada !== NaN && quantidadeMetros !== NaN) {
        switch (maquinaSelecionada) {
            case "PrismaTex":
                var res = TempoTotalImpressao(quantidadeMetros, 0)
                break
            case "PrismaJet":
                var res = TempoTotalImpressao(quantidadeMetros, 1)
                break
            case "Mutoh":
                var res = TempoTotalImpressao(quantidadeMetros, 2)
                break
            default:
                0
        }
    }
    areaTexResultado.innerHTML = res
    //console.log(res)

})
