from main import db
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.sqlite import BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, VARCHAR
from datetime import datetime
from main import ma

class UserDetails(db.Model):
    __tablename__ = 'UserDetails'
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(255))
    user_type = db.Column(db.String(255))

    def __init__(self, user_id, user_name, password, name, phone, email, user_type):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.user_type = user_type

class UserDetailsSchema(ma.Schema):
    class Meta:
         # Fields to expose
        fields = ('user_id', 'user_name', 'name', 'phone', 'email', 'type')

user_details = UserDetails()
users_details = UserDetails(many = True)



class Table(db.Model):
    __tablename__ = 'Table'
    hotel_id = db.Column(db.Integer)
    table_id = db.Column(db.Integer,primary_key = True)
    status = db.Column(db.Boolean)

    def __init__(self, hotel_id, table_id, status):
        self.hotel_id = hotel_id
        self.table_id = table_id
        self.status = status
            
class TableSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'table_id', 'status')

table = Table()
tables = Table(many = True)


class Payment(db.Model):
    __tablename__ = 'Payment'
    hotel_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer,primary_key = True)
    transaction_id = db.Column(db.String(255))
    date_time=db.Column(db.dateTime)
    amount = db.Column(db.Float(10))
    mode = db.Column(db.String)

    def __init__(self, hotel_id, user_id, transaction_id, date_time, amount, mode):
        self.hotel_id = hotel_id
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.date_time=db.Column(db.dateTime)
        self.amount = amount
        self.mode = mode

class Payment(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id','user_id','transaction_id', 'date_time','amount','mode')

Payment = Payment()
Payments = Payment(many = True)




class HotelDetail(db.Model):
    __tablename__='Hotel'
    hotel_id = db.Column(db.Integer,primary_key=True)
    hotel_name = db.Column(db.String(225))
    hotel_address = db.Column(db.String(225))
                                            #hotel_menu=JSON kaise hoga???
    no_waiter = db.Column(db.Integer)

    def __init__(self, hotel_id, hotel_name, hotel_address):
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.hotel_address=hotel_address
        
class HotelDetails(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'user_id', 'transaction_id', 'amount', 'mode')

HotelDetail = HotelDetail()
HotelDetails= HotelDetail(many=True)

class Menu(db.Model):
    __tablename__='Menu'
    menu_id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    item_price = db.Column(db.float(10))
    item_type = db.Column(db.String(225))
    item_status = db.Column(db.Boolean)

    def __init__(self,menu_id,item_name,item_id,item_price,item_type,item_status):
        self.menu_id = menu_id
        self.item_name = item_name
        self.item_id = item_id
        self.item_price = item_price
        self.item_type = item_type
        self.item_status = item_status
           
class Menu(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('menu_id', 'item_name', 'item_id', 'item_price', 'item_type', 'item_status')

Menu = Menu()
Menus = Menu(many = True)

class Waiter(db.Model):

    __tablename__ = 'Waiter'
    waiter_id = db.Column(db.Integer,primary_key=True)
    hotel_id = db.Column(db.Integer)
    order_id = db.Column(db.Integer)
    order_status = db.Column(db.Boolean)
    transaction_id = db.Column(db.String(225))

    def __init__(self,waiter_id,hotel_id,order_id,order_status,transaction_id):
        self.waiter_id = waiter_id
        self.hotel_id = hotel_id
        self.order_id = order_id
        self.order_status = order_status
        self.transaction_id = transaction_id
           
class Menu(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('waiter_id', 'hotel_id', 'order_id', 'order_status', 'transaction_id')

Waiter = Waiter()
Waiters = Waiter(many=True)
