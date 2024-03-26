from flask import Flask, redirect, url_for, abort
import pandas as pd
import pm4py

app = Flask(__name__)
@app.route("/")
def hello():
    print("$$$$$$$$$$")
    return "Hello, World!\n"

    

@app.route("/process")
def processMining():
    df = pm4py.format_dataframe(pd.read_csv("running-example.csv", sep=';'), 
                                case_id="case_id", activity_key="activity", timestamp_key="timestamp", timest_format="%Y-%m-%d %H:%M:%S%z")
    bpmn_model = pm4py.discovery.discover_bpmn_inductive(df)
    return pm4py.view_bpmn(bpmn_model)

@app.route("/filter")
def import_csv():
    print("hello")
    file_path = "running-example.csv"
    print("file_path: ", file_path)
    event_log = pd.read_csv(file_path, sep=';')
    event_log = pm4py.format_dataframe(event_log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
    start_activities = pm4py.get_start_activities(event_log)
    end_activities = pm4py.get_end_activities(event_log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))
    return end_activities


if __name__ == "__main__":
    app.run(debug=True)
