from main import db
from flask_marshmallow import Marshmallow

from main import ma

class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    user_type = db.Column(db.String(255))

    def __init__(self, user_name, password, name, phone, email, user_type):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.user_type = user_type

class UserSchema(ma.Schema):
    class Meta:
         # Fields to expose
        fields = ('user_id', 'user_name', 'password', 'name', 'phone', 'email', 'user_type')

user_schema = UserSchema()
users_schema = UserSchema(many=True)



class Table(db.Model):
    __tablename__ = 'Table'
    hotel_id = db.Column(db.Integer)
    table_id = db.Column(db.Integer,primary_key = True)
    status = db.Column(db.Boolean)

    def __init__(self, hotel_id, status):
        self.hotel_id = hotel_id
        self.status = status
            
class TableSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'table_id', 'status')

table_schema = TableSchema()
tables_schema = TableSchema(many=True)


class Payment(db.Model):
    __tablename__ = 'Payment'
    hotel_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    payment_id = db.Column(db.Integer, primary_key = True)
    date_time =  db.Column(db.DateTime)
    amount = db.Column(db.Float)
    mode = db.Column(db.String)
    transaction_id = db.Column(db.Integer)

    def __init__(self, hotel_id, user_id, date_time, amount, mode, transaction_id):
        self.hotel_id = hotel_id
        self.user_id = user_id
        self.date_time= date_time
        self.amount = amount
        self.mode = mode
        self.transaction_id = transaction_id

class PaymentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'user_id', 'payment_id', 'date_time', 'amount', 'mode', 'transaction_id')

payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)




class Hotel(db.Model):
    __tablename__='Hotel'
    hotel_id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    hotel_name = db.Column(db.String(225))
    hotel_address = db.Column(db.String(225))
    contact = db.Column(db.String(225)) 
    hotel_lat = db.Column(db.Float)
    hotel_long = db.Column(db.Float)
    opening_time = db.Column(db.String(255))
    closing_time = db.Column(db.String(255))
    hotel_desc = db.Column(db.String)
    no_waiter = db.Column(db.Integer)
    no_twoseater = db.Column(db.Integer)
    no_fourseater = db.Column(db.Integer)
    no_sixseater = db.Column(db.Integer)
    no_eightseater = db.Column(db.Integer)
  

    def __init__(self, user_id, hotel_name, hotel_address, contact, hotel_lat, hotel_long, opening_time, closing_time, hotel_desc, no_waiter, no_twoseater, no_fourseater, no_sixseater, no_eightseater):
        self.user_id = user_id
        self.hotel_name = hotel_name
        self.hotel_address = hotel_address
        self.contact = contact
        self.hotel_lat = hotel_lat
        self.hotel_long = hotel_long
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.hotel_desc = hotel_desc
        self.no_waiter = no_waiter
        self.no_twoseater = no_twoseater
        self.no_fourseater = no_fourseater
        self.no_sixseater = no_sixseater
        self.no_eightseater = no_eightseater
        
class HotelSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'user_id', 'hotel_name', 'hotel_address', 'contact', 'hotel_lat', 'hotel_long', 'opening_time', 'closing_time', 'hotel_desc', 'no_waiter', 'no_twoseater', 'no_fourseater', 'no_sixseater', 'no_eightseater')

hotel_schema = HotelSchema()
hotels_schema= HotelSchema(many=True)

class Menu(db.Model):
    __tablename__='Menu'
    menu_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer)
    item_name = db.Column(db.String(255))
    item_id = db.Column(db.Integer)
    item_price = db.Column(db.Float)
    item_type = db.Column(db.String(225))
    item_status = db.Column(db.Boolean)

    def __init__(self, hotel_id, item_name, item_id, item_price, item_type, item_status):
        self.hotel_id = hotel_id
        self.item_name = item_name
        self.item_id = item_id
        self.item_price = item_price
        self.item_type = item_type
        self.item_status = item_status
           
class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('menu_id', 'hotel_id', 'item_name', 'item_id', 'item_price', 'item_type', 'item_status')

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)

class Waiter(db.Model):

    __tablename__ = 'Waiter'
    waiter_id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    hotel_id = db.Column(db.Integer)
    order_id = db.Column(db.Integer)
    waiter_status = db.Column(db.Boolean)
    transaction_id = db.Column(db.Integer)

    def __init__(self, user_id, hotel_id, order_id, waiter_status, transaction_id):
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.order_id = order_id
        self.waiter_status = waiter_status
        self.transaction_id = transaction_id
           
class WaiterSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('waiter_id', 'user_id', 'hotel_id', 'order_id', 'waiter_status', 'transaction_id')

waiter_schema = WaiterSchema()
waiters_schema = WaiterSchema(many=True)


class Order(db.Model):

    __tablename__ = 'Order'
    order_id = db.Column(db.Integer,primary_key=True)
    item_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    waiter_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    booking_id = db.Column(db.Integer)


    def __init__(self, item_id, quantity, price, waiter_id, user_id, booking_id):
        self.item_id = item_id
        self.quantity = quantity
        self.price = price
        self.waiter_id = waiter_id   
        self.user_id = user_id   
        self.booking_id = booking_id   

class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('order_id', 'item_id', 'quantity', 'price', 'waiter_id', 'user_id', 'booking_id')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)



class Transaction(db.Model):
    __tablename__ = 'Transaction'
    
    table_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    waiter_id = db.Column(db.Integer)
    hotel_id = db.Column(db.Integer)
    transaction_id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    order_id = db.Column(db.Integer)
    date_time =  db.Column(db.DateTime)
    booking_id = db.Column(db.Integer)



    def __init__(self, table_id, user_id, waiter_id, hotel_id, cost, order_id, date_time, booking_id):
        self.table_id = table_id
        self.user_id = user_id
        self.waiter_id = waiter_id
        self.hotel_id = hotel_id
        self.cost = cost
        self.order_id = order_id
        self.date_time = date_time
        self.booking_id = booking_id


class TransactionSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('table_id', 'user_id', 'waiter_id', 'hotel_id', 'transaction_id', 'cost', 'order_id', 'date_time', 'booking_id')

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)


class Booking(db.Model):
    __tablename__ = 'Booking'
    
    user_id = db.Column(db.Integer)
    hotel_id = db.Column(db.Integer)
    booking_id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer)
    waiter_id = db.Column(db.Integer)
    checkin = db.Column(db.Boolean)
    date_time =  db.Column(db.DateTime)
    
    def __init__(self, user_id, hotel_id, table_id, waiter_id, checkin, date_time):
        self.table_id = table_id
        self.user_id = user_id
        self.waiter_id = waiter_id
        self.hotel_id = hotel_id
        self.cost = cost
        self.order_id = order_id
        self.date_time = date_time


class BookingSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user_id', 'hotel_id', 'booking_id', 'table_id', 'waiter_id', 'checkin', 'date_time')

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

class Chef(db.Model):

    __tablename__ = 'Chef'
    chef_id = db.Column(db.Integer,primary_key=True)
    hotel_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    order_id = db.Column(db.Integer)
    status = db.Column(db.Boolean)

    def __init__(self, hotel_id, user_id, order_id, status):
        self.hotel_id = item_id
        self.user_id = user_id
        self.order_id = order_id
        self.status = status
           
class ChefSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('chef_id', 'hotel_id', 'user_id', 'order_id', 'status')

chef_schema = ChefSchema()
chefs_schema = ChefSchema(many=True)