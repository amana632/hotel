from main import db
from flask_marshmallow import Marshmallow

from main import ma
class Order(db.Model):                                                                
    order_id = db.Column(db.Integer,unique=True, primary_key=True)                                        
    item_id = db.Column(db.Integer, nullable=False) 
    quantity = db.Column(db.Integer, nullable=False)                                                            
    price = db.Column(db.Float, nullable=False)     
    user_id = db.Column(db.Integer, nullable=False)  
    hotel_id = db.Column(db.Integer, nullable=False)                                                                                            
    waiter_id = db.Column(db.Integer, nullable=False)                                          

    def __init__(self, order_id, item_id, quantity, price, user_id, hotel_id, waiter_id):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity
        self.price = price
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.waiter_id = waiter_id



class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('order_id', 'item_id', 'quantity', 'price', 'user_id', 'hotel_id', 'waiter_id')


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class Cook(db.Model):
    cook_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable= False)
    cook_name = db.Column(db.String(20))
    order_id =db.Column(db.Integer)

    def __init__(self,cook_id, hotel_id,cook_name,order_id):
        self.hotel_id = hotel_id
        self.order_id= order_id
        self.cook_name= cook_name
        self.cook_id= cook_id
	


class CookSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('cook_id','hotel_id','cook_name','order_id' )


cook_schema = CookSchema()
cooks_schema = CookSchema(many=True)

class Waiter(db.Model):
    waiter_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable= False)
    waiter_name = db.Column(db.String(20))
    waiter_contact = db.Column(db.Integer)
    waiter_free = db.Column(db.Boolean)
    order_id =db.Column(db.Integer)

    def __init__(self,waiter_id, hotel_id,waiter_name,waiter_contact, waiter_free,order_id):
        self.hotel_id = hotel_id
        self.waiter_name = waiter_name
        self.waiter_contact= waiter_contact
        self.waiter_free= waiter_free
        self.order_id= order_id
        self.userfirstname= userfirstname
	


class WaiterSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'waiter_name','waiter_contact','waiter_free','order_id','waiter_id' )


waiter_schema = WaiterSchema()
waiters_schema = WaiterSchema(many=True)

class Hotels(db.Model):
    hotel_id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(20))
    hotel_address = db.Column(db.String(80))
    hotel_phone = db.Column(db.Integer)
    hotel_email = db.Column(db.String(50), unique=True)
    hotel_lat = db.Column(db.Float)
    hotel_long = db.Column(db.Float)
    hotel_capacity = db.Column(db.Integer)
    hotel_open = db.Column(db.String)
    hotel_close = db.Column(db.String)
    hotel_desc = db.Column(db.String(200))
    hotel_stars = db.Column(db.Float)
    hotel_menupic = db.Column(db.String(2000))
    hotel_hotelpic = db.Column(db.String(2000))
    hotel_avgcost = db.Column(db.Float)
    hotel_moreinfo = db.Column(db.String(2000))

    def __init__(self,hotel_id, hotel_name,hotel_address,hotel_open,hotel_close,hotel_desc,hotel_stars,hotel_menupic, hotel_hotelpic,hotel_avgcost,hotel_moreinfo,hotel_phone, hotel_email,hotel_lat, hotel_long,hotel_capacity):
        self.hotel_id= hotel_id
        self.hotel_name = hotel_name
        self.hotel_address  = hotel_address
        self.hotel_open= hotel_open
        self.hotel_close= hotel_close
        self.hotel_desc= hotel_desc
        self.hotel_stars= hotel_stars
        self.hotel_menupic= hotel_menupic
        self.hotel_hotelpic = hotel_hotelpic
        self.hotel_avgcost  = hotel_avgcost
        self.hotel_moreinfo= hotel_moreinfo
        self.hotel_phone= hotel_phone
        self.hotel_email= hotel_email
        self.hotel_lat= hotel_lat
        self.hotel_long= hotel_long
        self.hotel_capacity= hotel_capacity
        


class HotelsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'hotel_name','hotel_address','hotel_open','hotel_moreinfo','hotel_phone', 'hotel_email','hotel_lat', 'hotel_long','hotel_capacity', 'hotel_desc','hotel_stars','hotel_menupic','hotel_close','hotel_hotelpic','hotel_avgcost')


hotels_schema = HotelsSchema()
hotelss_schema = HotelsSchema(many=True)



class Trans(db.Model):                                                                
    trans_id = db.Column(db.Integer,unique=True, primary_key=True)                                        
    user_id = db.Column(db.Integer, nullable=False)                                    
    hotel_id = db.Column(db.Integer, nullable=False)                                      
    total = db.Column(db.Float)                       
    coupon_disc = db.Column(db.Integer)                       
    trans_date  = db.Column(db.Date, nullable=False)      

    def __init__(self,trans_id, user_id, hotel_id, total, coupon_disc, trans_date):
        self.trans_id = trans_id
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.total = total
        self.coupon_disc = coupon_disc
        self.trans_date = trans_date


class TransSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('trans_id', 'user_id', 'hotel_id', 'total', 'coupon_disc', 'trans_date')


trans_schema = TransSchema()
transs_schema = TransSchema(many=True)


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    userfirstname = db.Column(db.String(20))
    userlastname = db.Column(db.String(20))
    userphone = db.Column(db.Integer)
    username = db.Column(db.String(20), unique=True)
    userpass = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)

    def __init__(self,userid, userfirstname,userlastname,userphone, username,userpass, email):
        self.userlastname= userlastname
        self.username = username
        self.email = email
        self.userid= userid
        self.userphone= userphone
        self.userpass= userpass
        self.userfirstname= userfirstname
	


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('userid', 'userfirstname','userlastname','userphone','username','userpass' ,'email' )


user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Tables(db.Model):
    tables_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable= False)
    no_of_seats = db.Column(db.Integer)
    reserved =db.Column(db.Boolean)

    def __init__(self,tables_id, hotel_id,no_of_seats,reserved):
        self.hotel_id = hotel_id
        self.tables_id= tables_id
        self.no_of_seats= no_of_seats
        self.reserved= reserved
	


class TablesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('tables_id','hotel_id','no_of_seats','reserved' )


tables_schema = TablesSchema()
tabless_schema = TablesSchema(many=True)


class Menu(db.Model):                                                                
    menu_id = db.Column(db.Integer,unique=True, primary_key=True)                                        
    name = db.Column(db.String, nullable=False)                                    
    hotel_id = db.Column(db.Integer, nullable=False)                                      
    price = db.Column(db.Float)                       
    available = db.Column(db.Boolean)                       
    discounted  = db.Column(db.String)      
    bestseller  = db.Column(db.String)      

    def __init__(self, menu_id, name, hotel_id, price, available, discounted, bestseller):
        self.menu_id = menu_id
        self.name = name
        self.hotel_id = hotel_id
        self.price = price
        self.available = available
        self.discounted = discounted
        self.bestseller = bestseller


class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('menu_id', 'name', 'hotel_id', 'price', 'available', 'discounted', 'bestseller')


menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)
