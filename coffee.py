import plotly.express as px
import numpy as np
import csv

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

    return {"x": coffee_in_ml, "y": sleep_in_hours}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Coffee and Sleep is --> ", correlation[0, 1])

def setup():
    data_path = "coffee.csv"
    data_source = getDataSource(data_path)

    plotFigure(data_path)
    findCorrelation(data_source)

setup()
