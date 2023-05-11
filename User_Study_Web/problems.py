problemsList = {
    1: {
        "1": {
            "questionNumber": 1,
            "selectionsNumber": 4,
            "description": "请选择下列哪条路径在上图中出现过？",
            "selections": {
                "1": "Local Tax -> General Fund -> Police",
                "2": "Internal Service Funds -> General Fund -> None-Departmental",
                "3": "Interfund Transfers -> Non-Discretionary -> City  Council",
                "4": "Property Tax -> Non-Discretionary -> City Auditor"
            }
        }, "2": {
            "questionNumber": 2,
            "selectionsNumber": 4,
            "description": "对于图中的节点'General Fund'，其未流向第三层的哪些节点？",
            "selections": {
                "1": "Finance",
                "2": "无",
                "3": "Housing & Community Development",
                "4": "Oakland Public Library"
            }
        }, "3": {
            "questionNumber": 3,
            "selectionsNumber": 4,
            "description": "对于第一层来说，哪个节点的值最大",
            "selections": {
                "1": "Property Tax",
                "2": "Interfund Transfers",
                "3": "Local Tax",
                "4": "Service Charges"
            }
        }
    }, 2: {
        "1": {
            "questionNumber": 1,
            "selectionsNumber": 4,
            "description": "请选择下列哪条路径在上图中出现过？",
            "selections": {
                "1": "Energy -> Transportation -> Air -> HFCs-PFCs",
                "2": "Industrial Process -> Landfills -> Aluminium Non-Ferrous Metals -> Methane",
                "3": "Industrial Process -> dummy Cement411 -> Cement -> Carbon Dioxide",
                "4": "Land Use Change -> Harvest / Management -> Other Industry -> Carbon Dioxide"
            }
        }, "2": {
            "questionNumber": 2,
            "selectionsNumber": 4,
            "description": "对于图中的节点'Chemicals'，其流入节点有哪些？",
            "selections": {
                "1": "Electricity and heat, Industry, Rice Cultivation",
                "2": "Electricity and heat, Industry, dummy Chemicals421",
                "3": "Transportation, Industry, dummy Chemicals421",
                "4": "Electricity and heat, Fugitive Emissions, dummy Chemicals421"
            }
        }, "3": {
            "questionNumber": 3,
            "selectionsNumber": 4,
            "description": "对于第三层来说，哪个节点的值最大？",
            "selections": {
                "1": "Road",
                "2": "Residential Buildings",
                "3": "Oil and Gas Processing",
                "4": "Other Industry"
            }
        }
    }, 3: {
        "1": {
            "questionNumber": 1,
            "selectionsNumber": 4,
            "description": "请选择下列哪条路径在上图中出现过？",
            "selections": {
                "1": "Total -> Human rights -> Working hours -> Cocoa mass",
                "2": "Total -> Human rights -> Packaging",
                "3": "Total -> Environment -> Land use -> Vegetables",
                "4": "Total -> Environment -> Climate change -> Coconut oil"
            }
        }, "2": {
            "questionNumber": 2,
            "selectionsNumber": 4,
            "description": "对于图中的节点'Environment'，以下哪个流入节点不是其流出节点？",
            "selections": {
                "1": "Land use",
                "2": "Packaging",
                "3": "climate change",
                "4": "Suffient wage"
            }
        }, "3": {
            "questionNumber": 3,
            "selectionsNumber": 4,
            "description": "对于第二、三、四层来说，哪个节点的值最大？",
            "selections": {
                "1": "Human rights",
                "2": "Environment",
                "3": "Land use",
                "4": "Coco butter"
            }
        }
    }, 4: {
        "1": {
            "questionNumber": 1,
            "selectionsNumber": 4,
            "description": "请选择下列哪条路径在上图中出现过？",
            "selections": {
                "1": "nvd3 -> scatterplot -> shinyapp -> Ramnath Vaidyanathan",
                "2": "d3 -> sankey -> tutorial -> Ramnath Vaidyanathan",
                "3": "dimple -> multiple -> blog post -> TimelyProtfolio",
                "4": "polychart -> custom -> standalone visualization -> TimelyProtfolio"
            }
        }, "2": {
            "questionNumber": 2,
            "selectionsNumber": 4,
            "description": "对于图中的节点'tutorial'，以下哪个流入节点不是其流入节点？",
            "selections": {
                "1": "sankey",
                "2": "line chart",
                "3": "custom",
                "4": "parallel coordinates"
            }
        }, "3": {
            "questionNumber": 3,
            "selectionsNumber": 4,
            "description": "对于第一层来说，哪个节点的值最大？",
            "selections": {
                "1": "d3",
                "2": "highcharts",
                "3": "polychart",
                "4": "dimple"
            }
        }
    }, 5: {
        "1": {
            "questionNumber": 1,
            "selectionsNumber": 4,
            "description": "请选择下列哪条路径在上图中出现过？",
            "selections": {
                "1": "Biomass -> dummy-Biomass-Industrial -> Residential -> Energy Services",
                "2": "Natural Gas -> dummy-Gas-Industrial -> Residential -> Rejected Energy",
                "3": "Coal -> Electricity-Generation -> Industry -> Energy Services",
                "4": "Nuclear -> Electricity-Generation -> dummy-Electricity-Generation-Rejected Energy -> Energy Services"
            }
        }, "2": {
            "questionNumber": 2,
            "selectionsNumber": 4,
            "description": "对于图中的节点'Industry'，以下哪个流入节点不是其流入节点？",
            "selections": {
                "1": "dummy-Petroleum-Industrial",
                "2": "dummy-Biomass-Industrial",
                "3": "dummy-Natural Gas-Residential",
                "4": "Electricity Generation"
            }
        }, "3": {
            "questionNumber": 3,
            "selectionsNumber": 4,
            "description": "请选出第三层中最大值对应的节点",
            "selections": {
                "1": "Transportation",
                "2": "Industrial",
                "3": "Residential",
                "4": "dummy-Electricity_Generation-Rejected Energy"
            }
        }
    }
}


def problemsReturns(problemsOrder):
    pass


def problemsData():
    pass
