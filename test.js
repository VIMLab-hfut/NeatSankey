// 节点布局算法最终生成的节点布局会包含三个内容：links, level, processingResult
// links对应节点布局算法中最后生成的links_html列表，它是一个一维数组，包含了当前桑基图全部的连边信息
// level是一个二维数组，直接来源于最后生成的level_html列表，本应只包含每层的节点存在信息，由下方result来进一步指明各个节点在当前层的顺序关系
// 现为简化算法，直接将result包含的顺序统筹到level中，故result的内容直接简化为一个从1开始、增长至当前节点总数的顺序数组
// 因此，节点布局算法只需生成两个列表内容：level_html, links_html

var links = [
{
    'source': 'Agricultural Energy Use',
    'target': 'Carbon Dioxide',
    'value': '1.4'
}, {'source': 'Agriculture', 'target': 'Agriculture Soils', 'value': '5.2'}, {
    'source': 'Agriculture',
    'target': 'Livestock and Manure',
    'value': '5.4'
}, {'source': 'Agriculture', 'target': 'Other Agriculture', 'value': '1.7'}, {
    'source': 'Agriculture',
    'target': 'Rice Cultivation',
    'value': '1.5'
}, {
    'source': 'Agriculture Soils',
    'target': 'dummy->Agriculture Soils->Nitrous Oxide->V2',
    'value': '5.2'
}, {
    'source': 'Livestock and Manure',
    'target': 'dummy->Livestock and Manure->Methane->V2',
    'value': '5.1'
}, {
    'source': 'Livestock and Manure',
    'target': 'dummy->Livestock and Manure->Nitrous Oxide->V2',
    'value': '0.3'
}, {
    'source': 'Other Agriculture',
    'target': 'dummy->Other Agriculture->Methane->V2',
    'value': '1.4'
}, {
    'source': 'Other Agriculture',
    'target': 'dummy->Other Agriculture->Nitrous Oxide->V2',
    'value': '0.3'
}, {'source': 'Rice Cultivation', 'target': 'dummy->Rice Cultivation->Methane->V2', 'value': '1.5'}, {
    'source': 'Air',
    'target': 'Carbon Dioxide',
    'value': '1.7'
}, {
    'source': 'Aluminium Non-Ferrous Metals',
    'target': 'Carbon Dioxide',
    'value': '1.0'
}, {'source': 'Aluminium Non-Ferrous Metals', 'target': 'HFCs - PFCs', 'value': '0.2'}, {
    'source': 'Cement',
    'target': 'Carbon Dioxide',
    'value': '5.0'
}, {'source': 'Chemicals', 'target': 'Carbon Dioxide', 'value': '3.4'}, {
    'source': 'Chemicals',
    'target': 'HFCs - PFCs',
    'value': '0.5'
}, {'source': 'Chemicals', 'target': 'Nitrous Oxide', 'value': '0.2'}, {
    'source': 'Coal Mining',
    'target': 'Carbon Dioxide',
    'value': '0.1'
}, {'source': 'Coal Mining', 'target': 'Methane', 'value': '1.2'}, {
    'source': 'Commercial Buildings',
    'target': 'Carbon Dioxide',
    'value': '6.3'
}, {
    'source': 'Deforestation',
    'target': 'dummy->Deforestation->Carbon Dioxide->V2',
    'value': '10.9'
}, {
    'source': 'Electricity and heat',
    'target': 'Agricultural Energy Use',
    'value': '0.4'
}, {
    'source': 'Electricity and heat',
    'target': 'Aluminium Non-Ferrous Metals',
    'value': '0.4'
}, {'source': 'Electricity and heat', 'target': 'Cement', 'value': '0.3'}, {
    'source': 'Electricity and heat',
    'target': 'Chemicals',
    'value': '1.3'
}, {
    'source': 'Electricity and heat',
    'target': 'Commercial Buildings',
    'value': '5.0'
}, {'source': 'Electricity and heat', 'target': 'Food and Tobacco', 'value': '0.5'}, {
    'source': 'Electricity and heat',
    'target': 'Iron and Steel',
    'value': '1.0'
}, {'source': 'Electricity and heat', 'target': 'Machinery', 'value': '1.0'}, {
    'source': 'Electricity and heat',
    'target': 'Oil and Gas Processing',
    'value': '0.4'
}, {'source': 'Electricity and heat', 'target': 'Other Industry', 'value': '2.7'}, {
    'source': 'Electricity and heat',
    'target': 'Pulp - Paper and Printing',
    'value': '0.6'
}, {
    'source': 'Electricity and heat',
    'target': 'Residential Buildings',
    'value': '5.2'
}, {'source': 'Electricity and heat', 'target': 'T and D Losses', 'value': '2.2'}, {
    'source': 'Electricity and heat',
    'target': 'Unallocated Fuel Combustion',
    'value': '2.0'
}, {'source': 'Food and Tobacco', 'target': 'Carbon Dioxide', 'value': '1.0'}, {
    'source': 'Iron and Steel',
    'target': 'Carbon Dioxide',
    'value': '4.0'
}, {'source': 'Machinery', 'target': 'Carbon Dioxide', 'value': '1.0'}, {
    'source': 'Oil and Gas Processing',
    'target': 'Carbon Dioxide',
    'value': '3.6'
}, {'source': 'Oil and Gas Processing', 'target': 'Methane', 'value': '2.8'}, {
    'source': 'Other Industry',
    'target': 'Carbon Dioxide',
    'value': '6.6'
}, {'source': 'Other Industry', 'target': 'HFCs - PFCs', 'value': '0.4'}, {
    'source': 'Pulp - Paper and Printing',
    'target': 'Carbon Dioxide',
    'value': '1.1'
}, {'source': 'Residential Buildings', 'target': 'Carbon Dioxide', 'value': '10.2'}, {
    'source': 'T and D Losses',
    'target': 'Carbon Dioxide',
    'value': '2.2'
}, {
    'source': 'Unallocated Fuel Combustion',
    'target': 'Carbon Dioxide',
    'value': '3.0'
}, {
    'source': 'Unallocated Fuel Combustion',
    'target': 'Methane',
    'value': '0.4'
}, {'source': 'Unallocated Fuel Combustion', 'target': 'Nitrous Oxide', 'value': '0.4'}, {
    'source': 'Energy',
    'target': 'Electricity and heat',
    'value': '23'
}, {'source': 'Energy', 'target': 'Fugitive Emissions', 'value': '4.5'}, {
    'source': 'Energy',
    'target': 'Industry',
    'value': '14.3'
}, {'source': 'Energy', 'target': 'Other Fuel Combustion', 'value': '9.1'}, {
    'source': 'Energy',
    'target': 'Transportation',
    'value': '14.7'
}, {'source': 'Fugitive Emissions', 'target': 'Coal Mining', 'value': '1.3'}, {
    'source': 'Fugitive Emissions',
    'target': 'Oil and Gas Processing',
    'value': '3.2'
}, {'source': 'Industry', 'target': 'Aluminium Non-Ferrous Metals', 'value': '0.4'}, {
    'source': 'Industry',
    'target': 'Cement',
    'value': '1.9'
}, {'source': 'Industry', 'target': 'Chemicals', 'value': '1.4'}, {
    'source': 'Industry',
    'target': 'Food and Tobacco',
    'value': '0.5'
}, {'source': 'Industry', 'target': 'Iron and Steel', 'value': '3.0'}, {
    'source': 'Industry',
    'target': 'Oil and Gas Processing',
    'value': '2.8'
}, {'source': 'Industry', 'target': 'Other Industry', 'value': '3.8'}, {
    'source': 'Industry',
    'target': 'Pulp - Paper and Printing',
    'value': '0.5'
}, {
    'source': 'Other Fuel Combustion',
    'target': 'Agricultural Energy Use',
    'value': '1.0'
}, {
    'source': 'Other Fuel Combustion',
    'target': 'Commercial Buildings',
    'value': '1.3'
}, {
    'source': 'Other Fuel Combustion',
    'target': 'Residential Buildings',
    'value': '5.0'
}, {
    'source': 'Other Fuel Combustion',
    'target': 'Unallocated Fuel Combustion',
    'value': '1.8'
}, {'source': 'Transportation', 'target': 'Air', 'value': '1.7'}, {
    'source': 'Transportation',
    'target': 'Rail - Ship and Other Transport',
    'value': '2.5'
}, {'source': 'Transportation', 'target': 'Road', 'value': '10.5'}, {
    'source': 'Harvest / Management',
    'target': 'dummy->Harvest / Management->Carbon Dioxide->V2',
    'value': '1.3'
}, {
    'source': 'Industrial Processes',
    'target': 'dummy->Industrial Processes->Aluminium Non-Ferrous Metals->V1',
    'value': '0.4'
}, {
    'source': 'Industrial Processes',
    'target': 'dummy->Industrial Processes->Cement->V1',
    'value': '2.8'
}, {
    'source': 'Industrial Processes',
    'target': 'dummy->Industrial Processes->Chemicals->V1',
    'value': '1.4'
}, {
    'source': 'Industrial Processes',
    'target': 'dummy->Industrial Processes->Other Industry->V1',
    'value': '0.5'
}, {'source': 'Land Use Change', 'target': 'Deforestation', 'value': '10.9'}, {
    'source': 'Land Use Change',
    'target': 'Harvest / Management',
    'value': '1.3'
}, {
    'source': 'Landfills',
    'target': 'dummy->Landfills->Methane->V2',
    'value': '1.7'
}, {'source': 'Rail - Ship and Other Transport', 'target': 'Carbon Dioxide', 'value': '2.5'}, {
    'source': 'Road',
    'target': 'Carbon Dioxide',
    'value': '10.5'
}, {'source': 'Waste', 'target': 'Landfills', 'value': '1.7'}, {
    'source': 'Waste',
    'target': 'Waste water - Other Waste',
    'value': '1.5'
}, {
    'source': 'Waste water - Other Waste',
    'target': 'dummy->Waste water - Other Waste->Methane->V2',
    'value': '1.2'
}, {
    'source': 'Waste water - Other Waste',
    'target': 'dummy->Waste water - Other Waste->Nitrous Oxide->V2',
    'value': '0.3'
}, {
    'source': 'dummy->Industrial Processes->Aluminium Non-Ferrous Metals->V1',
    'target': 'Aluminium Non-Ferrous Metals',
    'value': '0.4'
}, {
    'source': 'dummy->Industrial Processes->Cement->V1',
    'target': 'Cement',
    'value': '2.8'
}, {
    'source': 'dummy->Industrial Processes->Chemicals->V1',
    'target': 'Chemicals',
    'value': '1.4'
}, {
    'source': 'dummy->Industrial Processes->Other Industry->V1',
    'target': 'Other Industry',
    'value': '0.5'
}, {
    'source': 'dummy->Agriculture Soils->Nitrous Oxide->V2',
    'target': 'Nitrous Oxide',
    'value': '5.2'
}, {
    'source': 'dummy->Livestock and Manure->Methane->V2',
    'target': 'Methane',
    'value': '5.1'
}, {
    'source': 'dummy->Livestock and Manure->Nitrous Oxide->V2',
    'target': 'Nitrous Oxide',
    'value': '0.3'
}, {
    'source': 'dummy->Other Agriculture->Methane->V2',
    'target': 'Methane',
    'value': '1.4'
}, {
    'source': 'dummy->Other Agriculture->Nitrous Oxide->V2',
    'target': 'Nitrous Oxide',
    'value': '0.3'
}, {
    'source': 'dummy->Rice Cultivation->Methane->V2',
    'target': 'Methane',
    'value': '1.5'
}, {
    'source': 'dummy->Deforestation->Carbon Dioxide->V2',
    'target': 'Carbon Dioxide',
    'value': '10.9'
}, {
    'source': 'dummy->Harvest / Management->Carbon Dioxide->V2',
    'target': 'Carbon Dioxide',
    'value': '1.3'
}, {
    'source': 'dummy->Landfills->Methane->V2',
    'target': 'Methane',
    'value': '1.7'
}, {
    'source': 'dummy->Waste water - Other Waste->Methane->V2',
    'target': 'Methane',
    'value': '1.2'
}, {'source': 'dummy->Waste water - Other Waste->Nitrous Oxide->V2', 'target': 'Nitrous Oxide', 'value': '0.3'}]

var level = [
[{'name': 'Agriculture', 'size': 13.8}, {'name': 'Waste', 'size': 3.2}, {
    'name': 'Energy',
    'size': 65.6
}, {'name': 'Industrial Processes', 'size': 5.1}, {
    'name': 'Land Use Change',
    'size': 12.200000000000001
}], [{'name': 'Rice Cultivation', 'size': 1.5}, {'name': 'Other Agriculture', 'size': 1.7}, {
    'name': 'Landfills',
    'size': 1.7
}, {'name': 'Livestock and Manure', 'size': 5.3999999999999995}, {
    'name': 'Waste water - Other Waste',
    'size': 1.5
}, {'name': 'Agriculture Soils', 'size': 5.2}, {
    'name': 'Fugitive Emissions',
    'size': 4.5
}, {'name': 'Other Fuel Combustion', 'size': 9.1}, {
    'name': 'Electricity and heat',
    'size': 23.0
}, {'name': 'dummy->Industrial Processes->Chemicals->V1', 'size': 1.4}, {
    'name': 'Industry',
    'size': 14.3
}, {'name': 'dummy->Industrial Processes->Cement->V1', 'size': 2.8}, {
    'name': 'Transportation',
    'size': 14.7
}, {'name': 'Harvest / Management', 'size': 1.3}, {
    'name': 'Deforestation',
    'size': 10.9
}, {
    'name': 'dummy->Industrial Processes->Other Industry->V1',
    'size': 0.5
}, {
    'name': 'dummy->Industrial Processes->Aluminium Non-Ferrous Metals->V1',
    'size': 0.4
}], [{'name': 'dummy->Rice Cultivation->Methane->V2', 'size': 1.5}, {
    'name': 'dummy->Other Agriculture->Methane->V2',
    'size': 1.4
}, {'name': 'dummy->Livestock and Manure->Methane->V2', 'size': 5.1}, {
    'name': 'dummy->Landfills->Methane->V2',
    'size': 1.7
}, {
    'name': 'dummy->Waste water - Other Waste->Methane->V2',
    'size': 1.2
}, {
    'name': 'dummy->Other Agriculture->Nitrous Oxide->V2',
    'size': 0.3
}, {
    'name': 'dummy->Livestock and Manure->Nitrous Oxide->V2',
    'size': 0.3
}, {
    'name': 'dummy->Agriculture Soils->Nitrous Oxide->V2',
    'size': 5.2
}, {'name': 'dummy->Waste water - Other Waste->Nitrous Oxide->V2', 'size': 0.3}, {
    'name': 'Coal Mining',
    'size': 1.3
}, {'name': 'Unallocated Fuel Combustion', 'size': 3.8}, {
    'name': 'Oil and Gas Processing',
    'size': 6.4
}, {'name': 'Agricultural Energy Use', 'size': 1.4}, {
    'name': 'Commercial Buildings',
    'size': 6.3
}, {'name': 'Residential Buildings', 'size': 10.2}, {'name': 'Machinery', 'size': 1.0}, {
    'name': 'T and D Losses',
    'size': 2.2
}, {'name': 'Food and Tobacco', 'size': 1.0}, {
    'name': 'Iron and Steel',
    'size': 4.0
}, {'name': 'Pulp - Paper and Printing', 'size': 1.1}, {'name': 'Chemicals', 'size': 4.1}, {
    'name': 'Cement',
    'size': 5.0
}, {'name': 'Air', 'size': 1.7}, {'name': 'Rail - Ship and Other Transport', 'size': 2.5}, {
    'name': 'Road',
    'size': 10.5
}, {
    'name': 'dummy->Harvest / Management->Carbon Dioxide->V2',
    'size': 1.3
}, {'name': 'dummy->Deforestation->Carbon Dioxide->V2', 'size': 10.9}, {
    'name': 'Other Industry',
    'size': 7.0
}, {'name': 'Aluminium Non-Ferrous Metals', 'size': 1.2}], [{'name': 'Methane', 'size': 15.3}, {
    'name': 'Nitrous Oxide',
    'size': 6.7
}, {'name': 'Carbon Dioxide', 'size': 76.8}, {'name': 'HFCs - PFCs', 'size': 1.1}]]

let result = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    [1, 2, 3, 4]
]
