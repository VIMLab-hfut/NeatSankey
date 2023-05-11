let timer = 0;
window.setInterval(() => timer++, 1000)
let startTime = new Date();
let timecost = 0;

let questionOrder = [{algorithmOrder: 1, mapOrder: 1, problemOrder: 1}]

startTime = startTime.toString()
localStorage.setItem("startTime", startTime)

let randomMaps = new Set();
for (let i = 1; i <= 3; i++)
    for (let t = 1; t <= 5; t++)
        for (let j = 1; j <= 3; j++) {
            if (i === 1 && t === 1 && j === 1)
                continue
            randomMaps.add({
                algorithmOrder: i,
                mapOrder: t,
                problemOrder: j
            })
        }

// randomMaps.delete({algorithmOrder: 1, mapOrder: 1, problemOrder: 1})

// starts from 1st algorithm, 1st map, 1st Q
// from 1 -> 4, break at 5
let problemOrder = 1;
// from 1 -> 6, break at 7
let mapOrder = 1;
// as for algorithm, 1 represents sugiyama, 2 represents ilp and 3 represent new method
let algorithmOrder = 1;

let questAL
let questMA
let questPR

let jumpToNextMap = false;

//let problemSequence = document.getElementById("problemsNumberDisplay")
//let problemsRemains = document.getElementById("remainingProblemsNumberDisplay")


window.onload = () => {
    firstQuestion()
}

function firstQuestion() {
    axios({
        method: "GET",
        url: "pic",
        params: {
            "algorithmOrder": algorithmOrder,
            "mapOrder": mapOrder,
            "problemOrder": problemOrder
        },
        contentType: "application/json",
        responseType: "blob",
        timeout: 3000,
    }).then(async response => {
        document.getElementById("chart").src = URL.createObjectURL(response.data)
        // 'data:image/bmp;base64,' + Base64.encode(response.data)
        // = fileReader.result

        // console.log("OK!")
    })

    axios({
        method: "GET",
        url: "problemsList",
        params: {
            "algorithmOrder": algorithmOrder,
            "mapOrder": mapOrder,
            "problemOrder": problemOrder
        },
        contentType: "application/json",
        timeout: 3000,
    }).then(response => {
        console.log(`-----------Question${response.data['questionNumber']} Start-----------`)
        console.log(response.data)

        document.getElementById("problemDescription").innerText = response.data["description"]

        QuestionNormal({data: response.data})

//        problemSequence.innerText = `第 ${algorithmOrder} 类布局，第 ${mapOrder} 幅，第 ${String(problemOrder)} 题`
//        problemsRemains.innerText = `当前布局结果还剩 ${String(4 - problemOrder)} 题，共4题`

        // console.log("OK!")

        problemOrder++
    })
}

function nextQuestion() {
    // change to next
    if (problemOrder === 4) {
        problemOrder = 1
        mapOrder++
        if (mapOrder === 6) {
            mapOrder = 1
            algorithmOrder++
            if (algorithmOrder === 4) {
                let finishTime = new Date();
                finishTime = finishTime.toString()
                localStorage.setItem("finishTime", finishTime);

                finishQuestion()

                window.location.href = "susInvestigation"

            }
        }
        // changePic()
    }

    let randomNum = Math.floor(Math.random() * randomMaps.size)
    let currentObject = Array.from(randomMaps)[randomNum]

    questionOrder.push(currentObject)

    questAL = currentObject['algorithmOrder']
    questMA = currentObject['mapOrder']
    questPR = currentObject['problemOrder']

    changePic(questAL,questMA,questPR)

    axios({
        method: "GET",
        url: "problemsList",
        params: {
            "algorithmOrder": questAL,
            "mapOrder": questMA,
            "problemOrder": questPR
        },
        contentType: "application/json",
        // responseType: "blob",
        timeout: 3000,
    }).then(response => {
        console.log(`-----------Question${response.data['questionNumber']} Start-----------`)
        console.log(response.data)

        if (response.data["questionNumber"] === 1 || response.data["questionNumber"] === 2 || response.data["questionNumber"] === 3)
            QuestionNormal({data: response.data})
        else
            // QuestionSpecial({data: response.data})
            QuestionSpecial({data: response.data})

//        problemSequence.innerText = `第 ${algorithmOrder} 类布局，第 ${mapOrder} 幅，第 ${String(problemOrder)} 题`
//        problemsRemains.innerText = `当前图像结果还有 ${String(4 - problemOrder)} 题，共4题`

        problemOrder++
        // console.log("OK!")
    })

    randomMaps.delete(currentObject)
}

function changePic(AL, MA, PR) {
    axios({
        method: "GET",
        url: "pic",
        params: {
            "algorithmOrder": AL,
            "mapOrder": MA,
            "problemOrder": PR
        },
        contentType: "application/json",
        responseType: "blob",
        timeout: 3000,
    }).then(async response => {
        document.getElementById("chart").src = URL.createObjectURL(response.data)
        // 'data:image/bmp;base64,' + Base64.encode(response.data)
        // = fileReader.result

        // console.log("OK!")
    })
}


function finishQuestion() {
    let randomQuestionOrder = ""
    questionOrder.forEach(question => {
        randomQuestionOrder = randomQuestionOrder
            + "AL:" + question.algorithmOrder
            + ",MA:" + question.mapOrder
            + ",PR:" + question.problemOrder
            + ";"
    })

    localStorage.setItem("questionOrder", randomQuestionOrder)


    window.location.href = "susInvestigation"
}


let form = document.querySelector("form");
form.addEventListener("submit", function (event) {
    let formData = new FormData(form);

    localStorage.setItem(`Test${(algorithmOrder - 1) * 15 + (mapOrder - 1) * 3 + problemOrder}Timecost`, timer - timecost)
    timecost = timer

    localStorage.setItem(`Test${(algorithmOrder - 1) * 15 + (mapOrder - 1) * 3 + problemOrder}Choice`, formData.get("selections"))

    event.preventDefault(); // prevent the refreshing

    nextQuestion()

}, false);


function QuestionNormal({data}) {
    AddSelections({data: data})
}


function QuestionSpecial({data}) {
    AddSelections({data: data})

    // let svgHeight = 650
    //     // Number(document.getElementById("chartSvg").attributes.height.textContent);
    // let svgWidth = 1280
    //     // Number(document.getElementById("chartSvg").attributes.width.textContent);
    //
    // let area = d3.select("#chartSvg")
    //     .append("g")
    //
    // area.append("rect")
    //     .attr("x", 48 / 2)
    //     .attr("y", 48 / 2)
    //     .attr("width", 448)
    //     .attr("height", 448)
    //     .style("opacity", "0.4")
    //     .style("stroke", "red")
    //
    // area.append("text")
    //     .attr("text-anchor", "start")
    //     .attr("x", 48 + 6)
    //     .attr("y", 224)
    //     .attr("dy", ".35em")
    //     .attr("transform", null)
    //     .text("area1")
}


function AddSelections({data}) {

    document.getElementById("problemDescription").innerText = "Test " + String((algorithmOrder - 1) * 15 + (mapOrder - 1) * 3 + problemOrder) + ": " + data["description"]

    let selectionsBox = document.getElementById("problemsSelectionBox")
    selectionsBox.innerHTML = ""

    for (let i = 1; i <= data["selectionsNumber"]; i++) {
        let selectionsDivider = document.createElement("div");
        selectionsDivider.setAttribute("class", "selectionsDivider");
        selectionsDivider.setAttribute("id", `selectionsDivider${i}`);
        // selectionsDivider.setAttribute("class", "");

        let selectionsLabel = document.createElement("label")
        selectionsLabel.setAttribute("for", `selections${i}Text`)
        // selectionsLabel.setAttribute("class", "tm-q-choice tm-q-choice-2-col")

        let selectionInput = document.createElement("input")
        selectionInput.setAttribute("type", "radio")
        selectionInput.setAttribute("id", `selections${i}Text`)
        selectionInput.setAttribute("name", `selections`)
        selectionInput.setAttribute("class", "with-gap")
        selectionInput.setAttribute("value", `${i}`)
        // selectionInput.setAttribute("style", "width: 15px; height: 15px;font-size: 12px")

        // let selectionsLabelText =
        let selectionsLabelSpan = document.createElement("span")
        selectionsLabelSpan.setAttribute("style", "font-size:18px")

        let selectionsLabelSpanText = document.createTextNode(`${String.fromCharCode(i + 64)}: ${data["selections"][String(i)]}`)

        selectionsLabelSpan.appendChild(selectionsLabelSpanText)

        selectionsLabel.appendChild(selectionInput)
        selectionsLabel.appendChild(selectionsLabelSpan)

        selectionsDivider.appendChild(selectionsLabel)

        selectionsBox.appendChild(selectionsDivider)
    }
}

/*
single selection sample:

<div class="selectionsDivider">
    <input type="radio" id="selections1Text" name="selections" class="selections" value="1">
    <label for="selections1Text">none</label>
</div>

* */