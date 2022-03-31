import json


def csv_processing():
    with open("crime.csv", 'r') as f:
        content = f.readlines()

    print(content)

    nodes = []
    links = []

    for i in content:
        if content.index(i) == 0:
            continue
        else:
            line = i.split(',')
            if line[0] not in nodes:
                nodes.append({"name": line[0]})
            if line[1] not in nodes:
                nodes.append({"name": line[1]})

            links.append({"source": line[0], "target": line[1], "value": line[2].replace("\n", "")})
            # print(i, )
            # pass
    return {
        "nodes": nodes,
        "links": links
    }

# result = csv_processing()
#
# with open("dataset/crime.json", "w") as f:
#     f.write(json.dumps(result))


def json_reprocessing():
    wrong_result = [
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Capital Improvement Projects"
            },
            "value": 1.252
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "City Administrator"
            },
            "value": 16.1024
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "City Attorney"
            },
            "value": 4.9034
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "City Auditor"
            },
            "value": 1.9137
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "City Clerk"
            },
            "value": 1.9156
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "City Council"
            },
            "value": 4.1698
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Economic & Workforce Development"
            },
            "value": 4.8559
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Finance"
            },
            "value": 22.4377
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Fire"
            },
            "value": 124.7475
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Human Resources Management"
            },
            "value": 4.7713
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Human Services"
            },
            "value": 5.2234
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Information Technology"
            },
            "value": 10.2803
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Mayor"
            },
            "value": 2.549
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Non-Departmental"
            },
            "value": 77.2006
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Oakland Parks & Recreation"
            },
            "value": 15.662
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Oakland Public Library"
            },
            "value": 11.2828
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Oakland Public Works"
            },
            "value": 2.8819
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Planning & Building"
            },
            "value": 0.0454
        },
        {
            "source": {
                "name": "General Fund"
            },
            "target": {
                "name": "Police"
            },
            "value": 212.5089
        },
        {
            "source": {
                "name": "Business License Tax"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 71.5054
        },
        {
            "source": {
                "name": "Fines & Penalties"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 23.8335
        },
        {
            "source": {
                "name": "Grants & Subsidies"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 0.1194
        },
        {
            "source": {
                "name": "Interest Income"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 0.7405
        },
        {
            "source": {
                "name": "Interfund Transfers"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 14.9229
        },
        {
            "source": {
                "name": "Licenses & Permits"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 2.2107
        },
        {
            "source": {
                "name": "Miscellaneous Revenue"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 0.7493
        },
        {
            "source": {
                "name": "Parking Tax"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 10.2113
        },
        {
            "source": {
                "name": "Property Tax"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 169.3074
        },
        {
            "source": {
                "name": "Real Estate Transfer Tax"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 55.63
        },
        {
            "source": {
                "name": "Sales Tax"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 55.4251
        },
        {
            "source": {
                "name": "Service Charges"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 46.8456
        },
        {
            "source": {
                "name": "Transfers from Fund Balance"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 6.8025
        },
        {
            "source": {
                "name": "Transient Occupancy Tax"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 16.4
        },
        {
            "source": {
                "name": "Utility Consumption Tax"
            },
            "target": {
                "name": "General Fund"
            },
            "value": 50
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Capital Improvement Projects"
            },
            "value": 38.4343
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "City Administrator"
            },
            "value": 4.0636
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "City Attorney"
            },
            "value": 9.6838
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "City Clerk"
            },
            "value": 0.0675
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Economic & Workforce Development"
            },
            "value": 12.5926
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Finance"
            },
            "value": 13.5228
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Fire"
            },
            "value": 10.8653
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Housing & Community Development"
            },
            "value": 18.5454
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Human Resources Management"
            },
            "value": 1.9615
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Human Services"
            },
            "value": 62.6754
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Information Technology"
            },
            "value": 16.9423
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Mayor"
            },
            "value": 0.2937
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Non-Departmental"
            },
            "value": 263.7925
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Oakland Parks & Recreation"
            },
            "value": 10.5757
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Oakland Public Library"
            },
            "value": 17.5294
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Oakland Public Works"
            },
            "value": 156.8086
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Planning & Building"
            },
            "value": 27.1776
        },
        {
            "source": {
                "name": "Non-Discretionary"
            },
            "target": {
                "name": "Police"
            },
            "value": 23.6575
        },
        {
            "source": {
                "name": "Fines & Penalties"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 4.7521
        },
        {
            "source": {
                "name": "Gas Tax"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 7.0609
        },
        {
            "source": {
                "name": "Grants & Subsidies"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 58.1621
        },
        {
            "source": {
                "name": "Interest Income"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 0.1915
        },
        {
            "source": {
                "name": "Interfund Transfers"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 135.5091
        },
        {
            "source": {
                "name": "Internal Service Funds"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 74.2976
        },
        {
            "source": {
                "name": "Licenses & Permits"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 15.4548
        },
        {
            "source": {
                "name": "Local Tax"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 148.1487
        },
        {
            "source": {
                "name": "Miscellaneous Revenue"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 36.7525
        },
        {
            "source": {
                "name": "Parking Tax"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 8.6796
        },
        {
            "source": {
                "name": "Property Tax"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 4.2857
        },
        {
            "source": {
                "name": "Sales Tax"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 24.6465
        },
        {
            "source": {
                "name": "Service Charges"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 121.437
        },
        {
            "source": {
                "name": "Transfers from Fund Balance"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 45.3387
        },
        {
            "source": {
                "name": "Transient Occupancy Tax"
            },
            "target": {
                "name": "Non-Discretionary"
            },
            "value": 4.4727
        }
    ]

    result = []
    for i in wrong_result:
        result.append({"source": i["source"]["name"], "target": i["target"]["name"], "value": i["value"]})

    return result

print(json.dumps(json_reprocessing()))
