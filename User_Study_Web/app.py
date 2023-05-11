# import mimetypes
# mimetypes.add_type('application/javascript', '.js')
# mimetypes.add_type('text/css', '.css')
import json

from flask import *
from problems import *
from mapData import *

import random
import string

# from flask import render_template

app = Flask(__name__)

# show the pic based on this order
MOrder = [
    "City of Oakland Budget Sankey Particles",
    "ilp_case_result",
    "product_2",
    "rCharts Examples Sankey Particles",
    "us-energy-consumption",
]


@app.route('/HelloWorld')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/originalILP')
def originalILP():  # put
    return render_template(r'backups/ilp_case_result_ilp.html')


@app.route('/')
def preInvestigation():
    return render_template(r'preInvestigation.html')


@app.route('/Investigation', methods=['GET', 'POST'])
def Investigation():
    return render_template(r'InvestigationBox.html')


@app.route('/problemsList')
def problems():  # put
    # print(request.values)
    print(request.args)

    returnInfo = problemsList[int(request.args["mapOrder"])][request.args["problemOrder"]]

    return returnInfo


@app.route('/pic')
def pic():
    picName = "logo.png"
    print(request.args)

    if int(request.args["algorithmOrder"]) == 1:
        # sugiyama
        picName = MOrder[int(request.args["mapOrder"]) - 1] + "_sugiyama.png"

    elif int(request.args["algorithmOrder"]) == 2:
        # ilp
        picName = MOrder[int(request.args["mapOrder"]) - 1] + "_ilp.png"

    else:
        # new method
        picName = MOrder[int(request.args["mapOrder"]) - 1] + "_ilp_ours.png"
    return send_file("static/img/" + picName, mimetype="image/gif")


@app.route("/susInvestigation")
def sus():
    return render_template("SUS.html")


@app.route("/specialPic")
def singlePic():
    return send_file("static/img/ilp_case_result_ilp_ours.png")


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


@app.route('/saveData', methods=["POST"])
def save():
    # result = []
    # for i in request.values:
    #     result.append({i, request.values[i]})

    uname = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    with open(uname + ".txt", "w") as f:
        for i in request.values:
            f.write(i + ": " + request.values[i] + "\n")

    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
