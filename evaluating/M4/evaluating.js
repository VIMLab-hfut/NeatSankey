// Metrics No.4
function totalSwingCalc(data) {
    let TSWV = 0 // total-swing-value

    data.links.forEach(link => {
        let currentLineSourceX = link.source.x,
            currentLineSourceY = link.source.y + link.dy/2 + link.sy,
            currentLineTargetX = link.target.x,
            currentLineTargetY = link.target.y + link.dy/2 + link.ty

        TSWV += Math.abs((currentLineTargetY - currentLineSourceY) / (currentLineTargetX - currentLineSourceX))
    })

    localStorage.getItem("order") === null
        ? localStorage.setItem("order", 0)
        : localStorage.setItem("order", Number(localStorage.getItem("order")) + 1)

    localStorage.setItem("data" + localStorage.getItem("order"), TSWV)

    localStorage.getItem("sw") === null
        ? localStorage.setItem("sw", TSWV)
        : localStorage.setItem("sw", TSWV + Number(localStorage.getItem("sw")))


    alert("sw: " + localStorage.getItem("data" + localStorage.getItem("order")))
    alert("total sw: " + localStorage.getItem("sw"))
}
// run these code in the console of browser
// and once finished, get the result through localStorage
