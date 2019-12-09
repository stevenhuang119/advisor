import flask
import backend
import requests
import pandas as pd

from flask import request, abort, jsonify

class_data = pd.read_csv('backend/api/coursework.csv')
class_data.set_index('Course', inplace=True)

schedule_data = pd.read_csv('backend/static/WN2020.csv')

def make_schedule(dept, course):
    schedule = []

    print(dept)
    print(type(course))
    
    if dept == "EECS":
        df = schedule_data.loc[(schedule_data['Catalog Nbr'] == float(course))]

        for i, j in df.iterrows():
            comp = str(j.loc['Component'])
            mon = str(j.loc['M'])
            tues = str(j.loc['T'])
            wed = str(j.loc['W'])
            thur = str(j.loc['TH'])
            fri = str(j.loc['F'])
            time = str(j.loc['Time'])

            time_slot = comp + " "

            if mon != "nan":
                time_slot += mon + " "    

            if tues != "nan":
                time_slot += tues + " "

            if wed != "nan":
                time_slot += wed + " "

            if thur != "nan":
                time_slot += thur + " "

            if fri != "nan":
                time_slot += fri + " "
            
            time_slot += time

            schedule.append(time_slot)

    print(schedule)
    return schedule

@backend.app.route('/chatbot/', methods=['GET', 'POST'])
def chatbot():
    backend.MASTER_DIALOG_TOKEN = '40C0QYWuywZbF3AwFNNohraKgX8MotY'
    return flask.render_template("chatbot.html")

@backend.app.route('/_clinc_process')
def clinc_process():
    try:
        text =  request.args.get('text', 0, type=str)

        url = "https://api.clinc.ai/v1/query/"

        payload = {
            "query": text,
            "language": "en",
            "device": "Alexa",
            "lat": 42.2810237,
            "lon": -83.7467534,
            "time_offset": 300,
            "dialog": backend.MASTER_DIALOG_TOKEN
        }

        headers = {
            "Authorization": "app-key da5d9c7c2209566a349ff7ba2d74b530411bcfab",
            "Content-Type": "application/json"
        }

        resp = requests.post(url, json=payload, headers=headers)

        print(resp.json())

        print('DIALOG KEY:')
        print(resp.json()['dialog'])
        backend.MASTER_DIALOG_TOKEN = resp.json()['dialog']

        dept = "null"
        course = "null"
        review = "null"
        schedule = []

        if resp.json()['competency'] == 'course_info' and resp.json()['response']['slots']:
            course_ret = resp.json()['response']['slots'][0]['raw_value']['values'][0]['course_mapper']
            if course_ret != 'NULL':
                course_ar = course_ret.split()
                dept = course_ar[0] #eecs
                course = course_ar[1] #281

                review = class_data.loc[course_ret]['StudentReview']

                schedule = make_schedule(dept, course)

        ret = resp.json()['visuals']['formattedResponse']

        print("---------------------Clinc Process Finished--------------------------------")
        return jsonify(result = ret, dept = dept, course = course, review = review, schedule = schedule)


    except Exception as e:
        return str(e)