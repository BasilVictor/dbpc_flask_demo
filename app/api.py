from app import app
from flask import request, jsonify, make_response
import pandas as pd
import time, csv, datetime

@app.route("/api/get_description/<color>", methods=['GET'])
def get_color_description(color):

    time.sleep(3)
    df = pd.read_csv("./app/data/list.csv")
    df = df[df['Colors'] == color]
    data = ""
    if(len(df.values) > 0):
        data = df.values[0][1]

    res = make_response(
        jsonify(
            {
                "status":200,
                "message":"Fetched List",
                "data":data
            }
        )
    )

    return res

@app.route("/api/submit_data", methods=['POST'])
def submit_data():

    req = request.get_json()
    print(req)

    with open("./app/data/data_container.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([req["name"], req["color"], datetime.datetime.now()])
        f.close()


    res = make_response(
        jsonify(
            {
                "status":200,
                "message":"Stored Data"
            }
        )
    )

    return res