from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import call_requests
import order_details

invoice_number = 0

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/InProgress')
def orders_in_progress():
  return render_template('orders_in_progress.html')

@app.route('/NewOrder', methods = ['POST','GET'])
def new_order():
  if request.method == 'POST':
    name = request.form['name']
    number = request.form['number']
    order_number = request.form['order_number']
    order = request.form['order']
    order_details.new_order(name, number, order_number, order)
  return render_template('new_order.html')

@app.route('/CallRequests')
def requests():
  return render_template('call_requests.html')

@app.route('/RequestCall', methods=["POST", "GET"])
def request_call():
  data = json.loads(request.data)
  print(data)
  # name = data["name"]
  # phone = data["phone"]
  # call_requests.add_request(name, phone)
  return {"message":"Received!"}

@app.route('/TrackOrder', methods=['GET'])
def track_order(name, order_number):
  order_details.track_order(name, order_number)
  return jsonify

@app.route('/JaBot')
def bot():
  return render_template('JaBot.html')

app.run(host='0.0.0.0', port=81)