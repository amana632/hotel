from flask import request, jsonify
from main import app
from main.model import Table, TableSchema, table_schema, tables_schema, User, user_schema, users_schema, UserSchema, payment_schema, payments_schema, Payment, PaymentSchema, Hotel, hotel_schema, hotels_schema, HotelSchema, Menu, menu_schema, menus_schema, MenuSchema, Waiter, WaiterSchema, waiter_schema, waiters_schema, Order, OrderSchema, order_schema, orders_schema, Transaction, TransactionSchema, transaction_schema, transactions_schema, Booking, BookingSchema, booking_schema, bookings_schema, Chef, ChefSchema, chef_schema, chefs_schema
from flask_marshmallow import Marshmallow
from main import db




@app.route("/")
def func():
    return "working"
    
# endpoint to create new hotels
@app.route("/hotels", methods=["POST"])
def add_hotels():
    user_id = request.form['user_id']
    hotel_name = request.form['hotel_name']
    hotel_pic = request.form['hotel_pic']
    hotel_address = request.form['hotel_address']
    hotel_email = request.form['hotel_email']
    contact = request.form['contact'] 
    hotel_lat = request.form['hotel_lat']
    hotel_long = request.form['hotel_long']
    opening_time = request.form['opening_time']
    closing_time = request.form['closing_time']
    hotel_desc = request.form['hotel_desc']
    special_monday = request.form['special_monday']
    special_tuesday = request.form['special_tuesday']
    special_wednesday = request.form['special_wednesday']
    special_thursday = request.form['special_thursday']
    special_friday = request.form['special_friday']
    special_saturday = request.form['special_saturday']
    special_sunday = request.form['special_sunday']
    bestsellers = request.form['bestsellers']
    no_waiter = request.form['no_waiter']
    no_twoseater = request.form['no_twoseater']
    no_fourseater = request.form['no_fourseater']
    no_sixseater = request.form['no_sixseater']
    no_eightseater = request.form['no_eightseater']

    new_hotel = Hotel(user_id, hotel_name, hotel_pic, hotel_address, hotel_email, contact, hotel_lat, hotel_long, opening_time, closing_time, hotel_desc, special_monday, special_tuesday, special_wednesday, special_thursday, special_friday, special_saturday, special_sunday, bestsellers, no_waiter, no_twoseater, no_fourseater, no_sixseater, no_eightseater)

    db.session.add(new_hotel)
    db.session.commit()
    return jsonify(a=new_hotel)

# endpoint to show all hotelss
@app.route("/hotels", methods=["GET"])
def get_hotels():
    all_hotels = Hotel.query.all()
    result = hotels_schema.dump(all_hotels)
    return jsonify(a=result.data)


# endpoint to get hotels detail by id
@app.route("/hotels/<hotel_id>", methods=["GET"])
def hotels_detail(hotel_id):
    hotels = Hotel.query.get(hotel_id)
    return jsonify(bestsellers=hotels.bestsellers,closing_time=hotels.closing_time,contact=hotels.contact,hotel_address=hotels.hotel_address,hotel_desc=hotels.hotel_desc, hotel_email=hotels.hotel_email,hotel_name=hotels.hotel_name,hotel_pic=hotels.hotel_pic,no_eightseater=hotels.no_eightseater, no_fourseater=hotels.no_fourseater, no_sixseater=hotels.no_sixseater, no_twoseater=hotels.no_twoseater,no_waiter=hotels.no_waiter, opening_time=hotels.opening_time, special_friday=hotels.special_friday, special_monday=hotels.special_monday, special_saturday=hotels.special_saturday, special_sunday=hotels.special_sunday, special_thursday=hotels.special_thursday, special_tuesday=hotels.special_tuesday, special_wednesday=hotels.special_wednesday,user_id= hotels.user_id)


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    user_name = request.form['username']
    password = request.form['password']
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    user_type = request.form['user_type']
    
    
    new_user = User(user_name, password, name, phone, email, user_type)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

# endpoint to check whether user is already is registered
@app.route("/isRegisteredUser/<phone>", methods=["GET"])
def isRegisteredUser(phone):
    data = User.query.filter_by(phone= phone).first()
    if data is not None:
        if (data.phone == phone) :
          
            return jsonify(a="True")
        else :
            return jsonify(a="False")
    else:
        return jsonify(a="not_registered")

# endpoint to check whether user is already is valid
@app.route("/isValidUser", methods=["GET"])
def isValidUser():
    phone = request.args['phone']
    password = request.args['password']
    user_type = request.args['user_type']

    data = User.query.filter_by(phone= phone).first()
    # return user_schema.jsonify(data)

    if(data.password == password and data.user_type == user_type) :
        return jsonify(a="True",b=data.user_id)
    else :
        return jsonify(a="False")


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(a=result.data)

# endpoint to give user id 
@app.route("/giveUserId/<phone>", methods=["GET"])
def giveUserId(phone):
    data = User.query.filter_by(phone= phone).first()
    return jsonify(a=data.user_id)
    

# endpoint to add a new waiter
@app.route("/waiter", methods=["POST"])
def add_waiter():
    user_id = request.form['user_id']
    hotel_id = request.form['hotel_id']
    order_id = request.form['order_id']
    waiter_status = request.form['waiter_status']
    transaction_id = request.form['transaction_id']

    new_waiter = Waiter(user_id, hotel_id, order_id, waiter_status, transaction_id)

    db.session.add(new_waiter)
    db.session.commit()

    return jsonify(new_waiter)


# endpoint to add a new chef
@app.route("/chef", methods=["POST"])
def add_chef():
    hotel_id = request.form['hotel_id']
    user_id = request.form['user_id']
    order_id = request.form['order_id']
    status = request.form['status']

    new_chef = Chef(hotel_id, user_id, order_id, status)

    db.session.add(new_chef)
    db.session.commit()

    return jsonify(new_chef)

# endpoint to give id to tables
@app.route("/table", methods=["POST"])
def add_table():
    hotel_id = request.form['hotel_id']
    status = request.form['status']

    new_table = Table(hotel_id, status)

    db.session.add(new_table)
    db.session.commit()

    return jsonify(new_table)

#endpoint to post the menu
@app.route("/menu", methods=["POST"])
def add_menu():
    hotel_id = request.form['hotel_id']
    item_name = request.form['item_name']
    item_price = request.form['item_price']
    item_type = request.form['item_type']
    item_status = request.form['item_status']

    new_menu = Menu(hotel_id, item_name, item_price, item_type, item_status)

    db.session.add(new_menu)
    db.session.commit()

    return jsonify(new_menu)

#endpoint to make a booking
@app.route("/booking", methods=["POST"])
def make_booking():
    user_id = request.form['user_id']
    hotel_id = request.form['hotel_id']
    table_id = request.form['table_id']
    waiter_id = request.form['waiter_id']
    checkin = request.form['checkin']
    date_time =  request.form['date_time']

    new_booking = Booking(user_id, hotel_id, table_id, waiter_id, checkin, date_time)

    db.session.add(new_booking)
    db.session.commit()

    return jsonify(new_booking)

# endpoint to find hotel id corresponding to user id
@app.route("/hotelid/<user_id>", methods=["GET"])
def getHotelId(user_id):
    data = Hotel.query.filter_by(user_id= user_id).first()
    return jsonify(a=data.hotel_id)



# endpoint to find hotel id corrsponding to hotel name
@app.route("/hotelid/<hotel_name>", methods=["GET"])
def getHotelIdbyname(hotel_name):
    data = Hotel.query.filter_by(hotel_name= hotel_name).first()
    return jsonify(a=data.hotel_id)




# endpoint to get menu by id
@app.route("/menu/<hotel_id>", methods=["GET"])
def menus_detail(hotel_id):
    all_menus = Menu.query.filter_by(hotel_id= hotel_id).all()
    result = menus_schema.dump(all_menus)

    return jsonify(a=result.data)



# endpoint to show all menus
@app.route("/menus", methods=["GET"])
def get_menus():
    all_menus = Menu.query.all()
    result = menus_schema.dump(all_menus)
    return jsonify(a=result.data)


#waiter status ki api
@app.route("/waiter/<hotel_id>", methods=["GET"])
def waiter_detail(hotel_id):
    all_waiter = Waiter.query.filter_by(hotel_id= hotel_id).all()
    result = waiters_schema.dump(all_waiter)

    return jsonify(a=result.data)










#transaction ki api
@app.route("/transaction", methods=["POST"])
def make_transaction():
    table_id = request.form['table_id']
    user_id = request.form['user_id']
    waiter_id = request.form['waiter_id']
    hotel_id = request.form['hotel_id']
    cost = request.form['cost']
    order_id =  request.form['order_id']
    date_time =  request.form['date_time']
    booking_id =  request.form['booking_id']

    new_transaction = Transaction(table_id, user_id, waiter_id, hotel_id, cost, order_id, date_time, booking_id)

    db.session.add(new_transaction)
    db.session.commit()

    return jsonify(new_transaction)

#payment ki api
@app.route("/payment", methods=["POST"])
def make_payment():
    hotel_id = request.form['hotel_id']
    user_id = request.form['user_id']
    date_time =  request.form['date_time']
    amount =  request.form['amount']
    mode =  request.form['mode']
    transaction_id =  request.form['transaction_id']
 
    new_payment = Payment(hotel_id, user_id, date_time, amount, mode, transaction_id)

    db.session.add(new_payment)
    db.session.commit()

    return jsonify(new_payment)



#update ki apis


























#heatmap ki api
@app.route("/table/<hotel_id>", methods=["GET"])
def table_detail(hotel_id):
    all_table = Table.query.filter_by(hotel_id= hotel_id).all()
    result = tables_schema.dump(all_table)

    return jsonify(a=result.data)
