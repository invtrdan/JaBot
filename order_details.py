from replit import db

# class Order:
#   def __init__(self, name, number, order, status):
#     self.name = name
#     self.number = number
#     self.order_number = order_number
#     self.order = order
#     self.status = status

def new_order(name, number, order_number, order, status="not started"):
  db[order_number] = name, number, order_number, order, status
  

