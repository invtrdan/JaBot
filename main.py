from flask import Flask, render_template, request, jsonify
import json

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

app.run(host='0.0.0.0', port=81)