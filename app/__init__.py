from flask import Flask, render_template, request, redirect
import json
import chat_bot

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("chat.html", status=True)


@app.route('/on')
def one():
    return 'Hello worldd'


@app.route('/client', methods=['POST'])
def client():
    data = request.get_json()
    print(data)
    if data['type'] == 'clientName':
        response = chat_bot.getInfo(data['value'])
        print(response)
        return json.dumps({'success': True, 'Type': 'clientName', 'data': response}), 200, {'ContentType': 'application/json'}

    elif data['type'] == 'clientSymptom':
        response = chat_bot.tree_to_code(data['value'])
        return json.dumps({'success': True, 'Type': 'clientSympom','data': response}), 200, {'ContentType': 'application/json'}

    elif data['type'] == 'clientSymptomList':
        symptom = data['value']
        response = chat_bot.getSymptomsList(symptom)
        return json.dumps({'success': True, 'Type': 'clientSymptomList','data': response}), 200, {'ContentType': 'application/json'}

    elif data['type'] == 'clientSymptomDetail':
        symptom_exp = data['symptomArr']
        noOfDays = data['noOfDays']

        response = chat_bot.getFinalResults(symptom_exp,noOfDays)
        return json.dumps({'success': True, 'Type': 'clientSymptomDetail','data': response}), 200, {'ContentType': 'application/json'}


