from flask import Flask, render_template, request, jsonify
import json

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

@app.route('/NewOrder')
def new_order():
  return render_template('new_order.html')

@app.route('/CallRequests')
def call_requests():
  return render_template('call_requests.html')

app.run(host='0.0.0.0', port=81)