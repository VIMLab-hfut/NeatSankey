// in this algorithm, we will use the links, level, result which should be defined at first in html file

function bundlingMethod(data) {
    const zoom = width / (level[level.length - 1][0].x + 36 - level[0][0].x)
    const bundlingPercent = 0.2

    for (let i = 0; i < level.length - 1; i++) {
    // at this cycle, we just do the pushing operation
    // after this, we take the baseLine one by one

        // Step1. choose which direction will be bundled
        // in this part, we will use the list "level" to judge the bundling direction

        // we have {level.length} layers and {level.length-1} gaps
        // every gap use the direction which depends on the nums of nodes between two layers to bundle
        let bundlingFromSource = true
        level[i].length < level[i + 1].length
            ? bundlingFromSource = true
            : bundlingFromSource = false

        if (bundlingFromSource) {
            // bundling From Source

            let startNodeIndex = 0
            let endNodeIndex = 0
            level.forEach(element => {
                    if (level.indexOf(element) < i) startNodeIndex += element.length
                    if (level.indexOf(element) <= i) endNodeIndex += element.length
                }
            )

            for (let pointerOfLevel = startNodeIndex; pointerOfLevel < endNodeIndex; pointerOfLevel++) {

                // Step2.
                // prepare for redrawing the path
                // cycling in the sourceLinks list of current node to find the baseLine
                let nodeList = [];
                for (let t = 0; t < data.nodes[pointerOfLevel].sourceLinks.length; t++)
                    // check all the info on this node at once
                    // we will make slice about it later
                    nodeList.push({
                        linkName: data.nodes[pointerOfLevel].sourceLinks[t].source.name + '-' + data.nodes[pointerOfLevel].sourceLinks[t].target.name,
                        source: {
                            name: data.nodes[pointerOfLevel].sourceLinks[t].source.name,
                            x: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].source.x * 1000) / 1000, // node left line position
                            y: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].source.y * 1000) / 1000, // node top line position
                            dx: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].source.dx * 1000) / 1000, // node width
                            dy: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].source.dy * 1000) / 1000, // node height
                        },
                        target: {
                            name: data.nodes[pointerOfLevel].sourceLinks[t].target.name,
                            x: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].target.x * 1000) / 1000, // node left line position
                            y: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].target.y * 1000) / 1000, // node top line position
                            dx: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].target.dx * 1000) / 1000, // node width
                            dy: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].target.dy * 1000) / 1000, // node height
                        },
                        dy: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].dy * 1000) / 1000, // stoke-width
                        sy: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].sy * 1000) / 1000, // distance to sourceNode's top line
                        ty: Math.floor(data.nodes[pointerOfLevel].sourceLinks[t].ty * 1000) / 1000, // distance to targetNode's top line
                        value: data.nodes[pointerOfLevel].sourceLinks[t].value,
                        directionAngle: Math.atan(
                            (data.nodes[pointerOfLevel].sourceLinks[t].ty + data.nodes[pointerOfLevel].sourceLinks[t].target.y
                                - data.nodes[pointerOfLevel].sourceLinks[t].sy - data.nodes[pointerOfLevel].sourceLinks[t].source.y)
                            / (data.nodes[pointerOfLevel].sourceLinks[t].target.x - data.nodes[pointerOfLevel].sourceLinks[t].source.x)
                        ),
                        // directionAngle is radians, so we will keep use radian as the unit:
                        // 30 degrees == 0.523599 radians;
                        // 10 degrees == 0.174533 radians;
                        // 1 radians == 57.29578 radians;
                    })


                // when starts a new cycle, we start from the place which we finished before
                // at the same time, the list: nodeList[{}] shares the same order with data.nodes[pointerOfLevel].sourceLinks[{}]
                let linkSequence = 0
                while (linkSequence < nodeList.length && nodeList.length !== 0) {

                    // we set a brand new baseLine each time
                    let beginningNode = undefined
                    let endingNode = undefined

                    // Step3. clustering by angle
                    while (linkSequence < nodeList.length) {
                        // only have effect on current node once

                        // choose the first node as the beginningNode and search for the endingNode
                        beginningNode === undefined
                            ? beginningNode = linkSequence
                            : ""

                        endingNode = linkSequence

                        if (Math.abs(nodeList[endingNode].directionAngle - nodeList[beginningNode].directionAngle) > 0.323599) {
                            // once this cycle break, we can get a cluster from [beginningNode to endingNode]
                            // and at the same time, pointer linkSequence have arrived at the beginningNode in next cluster
                            endingNode--
                            break
                        }

                        linkSequence++
                    }

                    // Step4. find the baseLine for this cluster
                    // find a line which can actually represent the direction for this cluster
                    // 30degrees == 0.523599radians; 90degrees == 1.570796radians; 1radians == 57.29578;
                    let baseLine = undefined
                    let maxAngle = (nodeList[beginningNode].directionAngle + nodeList[endingNode].directionAngle) / 2 + 0.274533
                    let minAngle = (nodeList[beginningNode].directionAngle + nodeList[endingNode].directionAngle) / 2 - 0.274533

                    for (let t = beginningNode; t <= endingNode; t++) {
                        if (nodeList[t].directionAngle >= minAngle && nodeList[t].directionAngle <= maxAngle)
                            baseLine === undefined
                                ? baseLine = data.nodes[pointerOfLevel].sourceLinks[t]
                                : baseLine.dy < nodeList[t].dy
                                    ? baseLine = data.nodes[pointerOfLevel].sourceLinks[t]
                                    : ""
                    }


                    // Step5.
                    // remove the original paths and redraw the bundled path
                    if (baseLine === "" || baseLine === undefined)
                        // no links behind this node here and start next cycle
                        console.log("no links here or no standard lines")
                    else {
                        let baseLineColor = document.getElementsByName(baseLine.source.name + "-" + baseLine.target.name)[0].style.stroke
                        document.getElementsByName(baseLine.source.name + "-" + baseLine.target.name)[0].style.strokeOpacity = "0.4"

                        // 5.1 we do the redrawing actions first
                        // 5.1.1 check data
                        for (let t = beginningNode; t <= endingNode; t++) {
                            // we redraw these links
                            let currentSourceNode = baseLine.source.sourceLinks[t].source
                            let currentTargetNode = baseLine.source.sourceLinks[t].target
                            let currentLineName = currentSourceNode.name + "-" + currentTargetNode.name
                            let currentLine = document.getElementsByName(currentLineName)

                            // nodeList是有序的！且其顺序正好与baseLine.source的sourceLinks的顺序完全一致
                            // 所以完全可以直接采用
                            for (let j = 0; j < currentLine.length; j++) {
                                let nodeDistance = currentTargetNode.y - baseLine.target.y // the x(r) of expression
                                const lorentzianA = 1
                                const lorentzianB = 100
                                nodeDistance = 1 - lorentzianA / (nodeDistance * nodeDistance + lorentzianB)　// the x(x) of expression
                                let originalLineWidth = nodeList[t].dy // the y of expression

                                // change the math expression here
                                const alpha1 = (level[i + 1][0].x -  level[i][0].x) * zoom * bundlingPercent;

                                const beta1 = 0.;

                                // the distance to target
                                // to ensure that the dist is positive, do abs() function to nodeDistance
                                let dist1 = 0
                                nodeDistance > 0
                                    ? dist1 = alpha1 * nodeDistance + beta1 * originalLineWidth
                                    : dist1 = alpha1 * Math.abs(nodeDistance) + beta1 * originalLineWidth

                                let minimalBundledLineWidth = 8

                                let remainingWidth = nodeList[t].dy

                                if (remainingWidth > minimalBundledLineWidth) {
                                    for (; remainingWidth > 0; remainingWidth = remainingWidth - minimalBundledLineWidth) {
                                        // first part of a line which starts from the source node
                                        // and continue to catch the baseline
                                        addLinksFromSource({
                                            path: linkPathGeneratorFromSource({
                                                source: baseLine.source,
                                                target: {
                                                    name: baseLine.source.name,
                                                    x: baseLine.source.x + dist1 + baseLine.source.dx,
                                                    y: linkYSearchFromSource({
                                                        source: baseLine.source,
                                                        target: baseLine.target,
                                                        dy: baseLine.dy,
                                                        ty: baseLine.ty,
                                                        sy: baseLine.sy,
                                                        transformX: 0,
                                                        transformY: 0,//-nodeList[t].dy / 2 + baseLine.dy / 2,
                                                    }, baseLine.source.x + dist1 + baseLine.source.dx), // 在绑线上搜索dist所截下的对应x坐标下的Y坐标
                                                    dx: baseLine.source.dx,
                                                    dy: baseLine.source.dy,
                                                },
                                                dy: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                                ty: 0,
                                                sy: nodeList[t].sy + nodeList[t].dy - remainingWidth,
                                            }),
                                            strokeWidth: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                            name: currentLineName + "-G1",
                                            title: currentLineName + "-G1",
                                        }, true, baseLineColor)


                                        addLinksFromSource({
                                            path: linkPathGeneratorFromSource({
                                                source: {
                                                    name: nodeList[t].source.name,
                                                    x: baseLine.source.x + dist1,
                                                    y: linkYSearchFromSource({
                                                        // currentLineName: currentLineName,
                                                        source: baseLine.source,
                                                        target: baseLine.target,
                                                        dy: baseLine.dy,
                                                        ty: baseLine.ty,
                                                        sy: baseLine.sy,
                                                        transformX: 0,
                                                        transformY: 0,//-nodeList[t].dy / 2 + baseLine.dy / 2,//nodeList[t+nodeNumberAdder].sy - baseLine.sy,
                                                    }, baseLine.source.x + dist1 + baseLine.source.dx), // 在绑线上搜索dist所截下的对应x坐标下的Y坐标
                                                    dx: nodeList[t].source.dx,
                                                    dy: nodeList[t].source.dy,
                                                },
                                                target: nodeList[t].target,
                                                dy: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                                ty: nodeList[t].ty + nodeList[t].dy - remainingWidth,
                                                sy: 0,
                                            }),
                                            strokeWidth: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                            name: currentLineName + "-G2",
                                            title: currentLineName + "-G2"
                                        }, true, baseLineColor)
                                    }
                                } else {
                                    addLinksFromSource({
                                        path: linkPathGeneratorFromSource({
                                            source: baseLine.source,
                                            target: {
                                                name: baseLine.source.name,
                                                x: baseLine.source.x + dist1 + baseLine.source.dx,
                                                y: linkYSearchFromSource({
                                                    source: baseLine.source,
                                                    target: baseLine.target,
                                                    dy: baseLine.dy,
                                                    ty: baseLine.ty,
                                                    sy: baseLine.sy,
                                                    transformX: 0,
                                                    transformY: 0,//-nodeList[t].dy / 2 + baseLine.dy / 2,
                                                }, baseLine.source.x + dist1 + baseLine.source.dx), // 在绑线上搜索dist所截下的对应x坐标下的Y坐标
                                                dx: baseLine.source.dx,
                                                dy: baseLine.source.dy,
                                            },
                                            dy: nodeList[t].dy,
                                            ty: 0,
                                            sy: nodeList[t].sy,
                                        }),
                                        strokeWidth: nodeList[t].dy,
                                        name: currentLineName + "-G1",
                                        title: currentLineName + "-G1",
                                    }, true, baseLineColor)


                                    // second line, which will be divided and point to the real target
                                    addLinksFromSource({
                                        path: linkPathGeneratorFromSource({
                                            source: {
                                                name: nodeList[t].source.name,
                                                x: baseLine.source.x + dist1,
                                                y: linkYSearchFromSource({
                                                    source: baseLine.source,
                                                    target: baseLine.target,
                                                    dy: baseLine.dy,
                                                    ty: baseLine.ty,
                                                    sy: baseLine.sy,
                                                    transformX: 0,
                                                    transformY: 0,
                                                }, baseLine.source.x + dist1 + baseLine.source.dx), // 在绑线上搜索dist所截下的对应x坐标下的Y坐标
                                                dx: nodeList[t].source.dx,
                                                dy: nodeList[t].source.dy,
                                            },
                                            target: nodeList[t].target,
                                            dy: nodeList[t].dy,
                                            ty: nodeList[t].ty,
                                            sy: 0,
                                        }),
                                        strokeWidth: nodeList[t].dy,
                                        name: currentLineName + "-G2",
                                        title: currentLineName + "-G2"
                                    }, true, baseLineColor)
                                }

                                // 5.2 do remove to original paths
                                currentLine[j].remove()
                                if (j >= 1) t++
                            }

                            function linkPathGeneratorFromSource(d) {
                                let curvature = 0.5;

                                function link(d) {
                                    const x0 = d.source.x + d.source.dx;
                                    const x1 = d.target.x;
                                    const x2 = Math.floor((x0 * (1 - curvature) + x1 * curvature) * 1000) / 1000;
                                    const x3 = Math.floor((x0 * curvature + x1 * (1 - curvature)) * 1000) / 1000;
                                    const y0 = Math.floor((d.source.y + d.sy + d.dy / 2) * 1000) / 1000;
                                    const y1 = Math.floor((d.target.y + d.ty + d.dy / 2) * 1000) / 1000;
                                    return "M" + x0 + "," + y0 + "C" + x2 + "," + y0 + " " + x3 + "," + y1 + " " + x1 + "," + y1;
                                }

                                return link(d)
                            }

                            // 求解这条曲线所截点的Y坐标，用中值来搜索
                            function linkYSearchFromSource(firstLine, positionXS) {
                                let curvature = 0.5;
                                // 还原原先的控制线与端点
                                const x0 = firstLine.source.x + firstLine.source.dx; // 起始点 x
                                const x3 = firstLine.target.x; // 终点 x
                                const xi = d3.interpolateNumber(x0, x3);
                                const x1 = xi(curvature); // 控制点1 x
                                const x2 = xi(1 - curvature); // 控制点2 x
                                const y0 = firstLine.source.y + firstLine.sy + firstLine.dy / 2// + firstLine.transformY;
                                const y3 = firstLine.target.y + firstLine.ty + firstLine.dy / 2// + firstLine.transformY;
                                const y1 = y0;
                                const y2 = y3;

                                let max = 1
                                let min = 0
                                let t = 0.5 // search starts from the middle, 50% per time
                                let positionX = 0
                                let positionY = 0
                                // 进行search
                                while (true) {
                                    positionX =
                                        x0 * (1 - t) * (1 - t) * (1 - t)
                                        + 3 * x1 * t * (1 - t) * (1 - t)
                                        + 3 * x2 * t * t * (1 - t)
                                        + x3 * t * t * t

                                    if (positionX - positionXS < 0.00001 && positionXS - positionX < 0.00001) {
                                        positionY =
                                            y0 * (1 - t) * (1 - t) * (1 - t)
                                            + 3 * y1 * t * (1 - t) * (1 - t)
                                            + 3 * y2 * t * t * (1 - t)
                                            + y3 * t * t * t
                                        break
                                    } else {
                                        if (positionX > positionXS)
                                            max = t
                                        else if (positionX < positionXS)
                                            min = t
                                        t = (max + min) / 2
                                    }
                                }

                                return positionY
                            }

                            function addLinksFromSource(pathData, isRealLine, baseLineColor) {
                                if (isRealLine === true) // the line that point to the real node
                                    svg.append("g")
                                        .append("path")
                                        .attr("class", "link")
                                        .attr("d", pathData.path)
                                        .attr("name", pathData.name)
                                        .style("stroke-width", Math.max(1, pathData.strokeWidth))
                                        .style("stroke", baseLineColor)
                                        .append("title")
                                        .text(pathData.title)
                                else {// the line that point to the baseLine node
                                    svg.append("g")
                                        .append("path")
                                        .attr("class", "link")
                                        .attr("d", pathData.path)
                                        .attr("name", pathData.name)
                                        .attr("transform", `translate(${pathData.transformX}, ${pathData.transformY})`)
                                        .style("stroke-width", Math.max(1, pathData.strokeWidth))
                                        .style("clip-path", pathData.clipPath)
                                        .style("stroke", baseLineColor)
                                        .append("title")
                                        .text(pathData.title)
                                }
                            }
                        }
                    }
                }
            }
        } else {
            let startNodeIndex = 0
            let endNodeIndex = 0
            level.forEach(element => {
                if (level.indexOf(element) <= i) startNodeIndex += element.length
                if (level.indexOf(element) <= i + 1) endNodeIndex += element.length
            })

            for (let pointerOfLevel = startNodeIndex; pointerOfLevel < endNodeIndex; pointerOfLevel++) {
                // Step2.
                // prepare for redrawing the path
                // cycling in the targetLinks list of current node to find the baseLine
                let nodeList = [];
                for (let t = 0; t < data.nodes[pointerOfLevel].targetLinks.length; t++)
                    // check all the info on this node at once
                    // we will make slice about it later
                    nodeList.push({
                        linkName: data.nodes[pointerOfLevel].targetLinks[t].source.name + '-' + data.nodes[pointerOfLevel].targetLinks[t].target.name,
                        source: {
                            name: data.nodes[pointerOfLevel].targetLinks[t].source.name,
                            x: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].source.x * 1000) / 1000, // node left line position
                            y: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].source.y * 1000) / 1000, // node top line position
                            dx: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].source.dx * 1000) / 1000, // node width
                            dy: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].source.dy * 1000) / 1000, // node height
                        },
                        target: {
                            name: data.nodes[pointerOfLevel].targetLinks[t].target.name,
                            x: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].target.x * 1000) / 1000, // node left line position
                            y: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].target.y * 1000) / 1000, // node top line position
                            dx: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].target.dx * 1000) / 1000, // node width
                            dy: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].target.dy * 1000) / 1000, // node height
                        },
                        dy: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].dy * 1000) / 1000, // stoke-width
                        sy: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].sy * 1000) / 1000, // distance to sourceNode's top line
                        ty: Math.floor(data.nodes[pointerOfLevel].targetLinks[t].ty * 1000) / 1000, // distance to targetNode's top line
                        value: data.nodes[pointerOfLevel].targetLinks[t].value,
                        directionAngle: Math.atan(
                            (data.nodes[pointerOfLevel].targetLinks[t].ty + data.nodes[pointerOfLevel].targetLinks[t].target.y
                                - data.nodes[pointerOfLevel].targetLinks[t].sy - data.nodes[pointerOfLevel].targetLinks[t].source.y)
                            / (data.nodes[pointerOfLevel].targetLinks[t].target.x - data.nodes[pointerOfLevel].targetLinks[t].source.x)
                        ),
                        // directionAngle is radians, so we will keep use radian as the unit:
                        // 30 degrees == 0.523599 radians;
                        // 10 degrees == 0.174533 radians;
                        // 1 radians == 57.29578 radians;
                    })

                // when starts a new cycle, we start from the place which we finished before
                // at the same time, the list: nodeList[{}] shares the same order with data.nodes[pointerOfLevel].sourceLinks[{}]
                let linkSequence = 0
                while (linkSequence < nodeList.length - 1 && nodeList.length !== 0) {

                    // we set a brand new baseLine each time
                    let beginningNode = undefined
                    let endingNode = undefined

                    // Step3. clustering by angle
                    while (true) {
                        // only have effect on current node once

                        // choose the first node as the beginningNode and search for the endingNode
                        beginningNode === undefined
                            ? beginningNode = linkSequence
                            : ""

                        endingNode = linkSequence

                        if (Math.abs(nodeList[endingNode].directionAngle - nodeList[beginningNode].directionAngle) > 0.323599) {
                            // once this cycle break, we can get a cluster from [beginningNode 4to endingNode]
                            // and at the same time, pointer linkSequence have arrived at the beginningNode in next cluster
                            endingNode--
                            break
                        }

                        // current "endingNode" may not be the really endingNode
                        if (linkSequence < nodeList.length - 1)
                            linkSequence++
                        else
                            break // we have arrived at the last node
                    }

                    // Step4. find the baseLine for this cluster
                    // find a line which can actually represent the direction for this cluster
                    // 30degrees == 0.523599radians; 90degrees == 1.570796radians; 1radians == 57.29578;
                    let baseLine = undefined
                    let maxAngle = (nodeList[beginningNode].directionAngle + nodeList[endingNode].directionAngle) / 2 + 0.274533
                    let minAngle = (nodeList[beginningNode].directionAngle + nodeList[endingNode].directionAngle) / 2 - 0.274533

                    for (let t = beginningNode; t <= endingNode; t++) {
                        if (nodeList[t].directionAngle >= minAngle && nodeList[t].directionAngle <= maxAngle)
                            baseLine === undefined
                                ? baseLine = data.nodes[pointerOfLevel].targetLinks[t]
                                : baseLine.dy < nodeList[t].dy
                                    ? baseLine = data.nodes[pointerOfLevel].targetLinks[t]
                                    : ""
                    }

                    // Step5.
                    // remove the original paths and redraw the bundled path
                    if (baseLine === "" || baseLine === undefined)
                        // no links behind this node here and start next cycle
                        console.log("no links here or no standard lines")
                    else {
                        let baseLineColor = document.getElementsByName(baseLine.source.name + "-" + baseLine.target.name)[0].style.stroke
                        document.getElementsByName(baseLine.source.name + "-" + baseLine.target.name)[0].style.strokeOpacity = "0.4"


                        // 5.1 we do the redrawing actions first
                        // 5.1.1 check data
                        for (let t = beginningNode; t <= endingNode; t++) {
                            // we redraw these links
                            let currentSourceNode = baseLine.target.targetLinks[t].source
                            let currentTargetNode = baseLine.target.targetLinks[t].target
                            let currentLineName = currentSourceNode.name + "-" + currentTargetNode.name
                            let currentLine = document.getElementsByName(currentLineName)

                            // nodeList has an order which is same to targetLinks
                            for (let j = 0; j < currentLine.length; j++) {
                                const lorentzianA = 1
                                const lorentzianB = 100
                                let nodeDistance = currentTargetNode.y - baseLine.target.y // the x(r) of expression
                                nodeDistance = 1 - lorentzianA / (nodeDistance * nodeDistance + lorentzianB)　// the x(x) of expression
                                let originalLineWidth = nodeList[t].dy // the y of expression

                                let alpha1 = (level[i + 1][0].x -  level[i][0].x - 36) * zoom * (1 - bundlingPercent)
                                const beta1 = 0.;

                                // the distance to target
                                // to ensure that the dist1 is positive, do abs() function to nodeDistance
                                let dist1 = 0
                                nodeDistance > 0
                                    ? dist1 = alpha1 * nodeDistance + beta1 * originalLineWidth
                                    : dist1 = alpha1 * Math.abs(nodeDistance) + beta1 * originalLineWidth

                                let remainingWidth = nodeList[t].dy

                                let minimalBundledLineWidth = 8

                                // find out where two line was combined
                                let tempY = linkYSearchFromTarget({
                                    source: baseLine.source,
                                    target: baseLine.target,
                                    dy: baseLine.dy,
                                    ty: baseLine.ty,
                                    sy: baseLine.sy,
                                    transformX: 0,
                                    transformY: +nodeList[t].dy / 2 - baseLine.dy / 2,
                                }, baseLine.source.x + dist1 + baseLine.source.dx)
                                if (remainingWidth > minimalBundledLineWidth) {

                                    for (; remainingWidth > 0; remainingWidth = remainingWidth - minimalBundledLineWidth) {
                                        // add links actions, which is opposite to the above one
                                        addLinksFromTarget({
                                            path: linkPathGeneratorFromTarget({
                                                source: nodeList[t].source,
                                                target: {
                                                    name: baseLine.source.name,
                                                    x: baseLine.source.x + dist1 + baseLine.source.dx,
                                                    y: tempY,
                                                    dx: baseLine.source.dx,
                                                    dy: baseLine.source.dy,
                                                },
                                                dy: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                                ty: 0,
                                                sy: nodeList[t].sy + nodeList[t].dy - remainingWidth
                                            }),
                                            strokeWidth: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                            name: `${nodeList[t].source.name}-${nodeList[t].target.name}-G1`,
                                            title: `${nodeList[t].source.name}-${nodeList[t].target.name}-G1`,
                                        }, true, baseLineColor) // first line, which shows with the baseline


                                        addLinksFromTarget({
                                            path: linkPathGeneratorFromTarget({
                                                source: {
                                                    name: baseLine.source.name,
                                                    x: baseLine.source.x + dist1,
                                                    y: tempY,
                                                    dx: baseLine.source.dx,
                                                    dy: baseLine.source.dy,
                                                },
                                                target: nodeList[t].target,
                                                //baseLine.target,
                                                dy: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                                ty: nodeList[t].ty + nodeList[t].dy - remainingWidth,
                                                sy: 0,
                                            }),
                                            strokeWidth: remainingWidth < minimalBundledLineWidth ? remainingWidth : minimalBundledLineWidth,
                                            name: `${nodeList[t].source.name}-${nodeList[t].target.name}-G2`,
                                            title: `${nodeList[t].source.name}-${nodeList[t].target.name}-G2`,
                                        }, true, baseLineColor)
                                    }
                                } else {
                                    // add links actions, which is opposite to the above one
                                    addLinksFromTarget({
                                        path: linkPathGeneratorFromTarget({
                                            source: nodeList[t].source,
                                            target: {
                                                name: baseLine.source.name,
                                                x: baseLine.source.x + dist1 + baseLine.source.dx,
                                                y: tempY,
                                                dx: baseLine.source.dx,
                                                dy: baseLine.source.dy,
                                            },
                                            dy: nodeList[t].dy,
                                            sy: nodeList[t].sy,
                                            ty: 0
                                        }),
                                        strokeWidth: nodeList[t].dy,
                                        name: `${nodeList[t].source.name}-${nodeList[t].target.name}-G1`,
                                        title: `${nodeList[t].source.name}-${nodeList[t].target.name}-G1`,
                                    }, true, baseLineColor) // first line, which shows with the baseline


                                    addLinksFromTarget({
                                        path: linkPathGeneratorFromTarget({
                                            source: {
                                                name: baseLine.source.name,
                                                x: baseLine.source.x + dist1,
                                                y: tempY,
                                                dx: baseLine.source.dx,
                                                dy: baseLine.source.dy,
                                            },
                                            target: nodeList[t].target,
                                            //baseLine.target,
                                            dy: nodeList[t].dy,
                                            sy: 0,
                                            ty: nodeList[t].ty
                                        }),
                                        strokeWidth: nodeList[t].dy,
                                        name: `${nodeList[t].source.name}-${nodeList[t].target.name}-G2`,
                                        title: `${nodeList[t].source.name}-${nodeList[t].target.name}-G2`,
                                    }, true, baseLineColor)
                                }

                                // 5.2 do remove to original paths
                                currentLine[j].remove()
                                if (j >= 1) t++
                            }

                            // 求解这条曲线所截点的Y坐标，用中值来搜索
                            function linkYSearchFromTarget(firstLine, positionXS) {
                                let curvature = 0.5;
                                // 还原原先的控制线与端点
                                const x0 = firstLine.source.x + firstLine.source.dx;
                                const x3 = firstLine.target.x;
                                const xi = d3.interpolateNumber(x0, x3);
                                const x1 = xi(curvature);
                                const x2 = xi(1 - curvature);
                                const y0 = firstLine.source.y + firstLine.sy + firstLine.dy / 2
                                const y3 = firstLine.target.y + firstLine.ty + firstLine.dy / 2
                                const y1 = y0;
                                const y2 = y3;

                                let max = 1
                                let min = 0
                                let t = 0.5 // search starts from the middle, 50% per time
                                let positionX = 0
                                let positionY = 0
                                // 进行search
                                while (true) {
                                    positionX =
                                        x0 * (1 - t) * (1 - t) * (1 - t)
                                        + 3 * x1 * t * (1 - t) * (1 - t)
                                        + 3 * x2 * t * t * (1 - t)
                                        + x3 * t * t * t

                                    if (positionX - positionXS < 0.00001 && positionXS - positionX < 0.00001) {
                                        positionY =
                                            y0 * (1 - t) * (1 - t) * (1 - t)
                                            + 3 * y1 * t * (1 - t) * (1 - t)
                                            + 3 * y2 * t * t * (1 - t)
                                            + y3 * t * t * t
                                        break
                                    } else {
                                        if (positionX > positionXS)
                                            max = t
                                        else if (positionX < positionXS)
                                            min = t
                                        t = (max + min) / 2
                                    }
                                }

                                return positionY
                            }

                            function linkPathGeneratorFromTarget(d) {
                                let curvature = 0.5;

                                function link(d) {
                                    const x0 = d.source.x + d.source.dx;
                                    const x1 = d.target.x;
                                    const x2 = Math.floor((x0 * (1 - curvature) + x1 * curvature) * 1000) / 1000;
                                    const x3 = Math.floor((x0 * curvature + x1 * (1 - curvature)) * 1000) / 1000;
                                    const y0 = Math.floor((d.source.y + d.sy + d.dy / 2) * 1000) / 1000;
                                    const y1 = Math.floor((d.target.y + d.ty + d.dy / 2) * 1000) / 1000;
                                    return "M" + x0 + "," + y0 + "C" + x2 + "," + y0 + " " + x3 + "," + y1 + " " + x1 + "," + y1;
                                }

                                return link(d)
                            }

                            function addLinksFromTarget(pathData, isRealLine, baseLineColor) {
                                if (isRealLine === true) // the line that point to the real node
                                    svg.append("g")
                                        .append("path")
                                        .attr("class", "link")
                                        .attr("d", pathData.path)
                                        .attr("name", pathData.name)
                                        .style("stroke-width", Math.max(1, pathData.strokeWidth))
                                        .style("stroke", baseLineColor)
                                        .append("title")
                                        .text(pathData.title)
                                else // the line that point to the baseLine node
                                    svg.append("g")
                                        .append("path")
                                        .attr("class", "link")
                                        .attr("d", pathData.path)
                                        .attr("name", pathData.name)
                                        .style("stroke-width", Math.max(1, pathData.strokeWidth))
                                        .style("clip-path", pathData.clipPath)
                                        .style("stroke", baseLineColor)
                                        .append("title")
                                        .text(pathData.title)
                            }

                        }
                    }
                }

            }
            console.log("--------one turn--------")
        }
    }
}

console.log("---------bundlingMethode Start!---------")
bundlingMethod(data)
console.log("---------bundlingMethode Over!---------")