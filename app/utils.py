import pandas as pd

def get_color_list():
    df = pd.read_csv("./app/data/list.csv")
    data = []
    df = df.values.tolist()
    for r in df:
        data.append(r[0])
    return data