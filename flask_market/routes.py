from flask_market import app,db
from flask import render_template, redirect, url_for, flash, request
from flask_market.Model import Item,User
from flask_market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/market',methods=['GET','POST'])
@login_required
def market():
    purchase_form=PurchaseItemForm()
    selling_form=SellItemForm()
    if request.method=='POST':
        #purchase item logic
        purchased_item= request.form.get('purchased_item')
        p_item_object=Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object.price):
               p_item_object.buy(current_user)
               flash(f"Congratulation! you have purchased {p_item_object.name} for {p_item_object.price}",category="success")
            else:
                flash("Unfortunately you do not have enough money to purchase {p_item_object.name}",category="danger")
        #sell item logic
        sold_item = request.form.get('sold_item')
        s_item_object=Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulation! you have sold {s_item_object.name} to the shiv's market for {s_item_object.price}",category="success")
            else:
                flash("Unfortunately you were not able to sell the item {s_item_object.name} ",category="danger")
        return redirect(url_for('market'))

    if request.method== 'GET':        
       items=Item.query.filter_by(owner=None)
       owned_items=Item.query.filter_by(owner=current_user.id)
       return render_template("market.html",items=items,purchase_form=purchase_form,owned_items=owned_items,selling_form=selling_form)


@app.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(username=form.Username.data, email_address=form.email_address.data, passward=form.passward1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Your account has been created and you are logged in as {user_to_create.username}",category="success")
        return redirect(url_for('market'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error in creating the user :{err_msg}",category='danger')
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user=User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_passward_correction(attempted_passward=form.passward.data):
            login_user(attempted_user)
            flash(f'success you are logged in as:{attempted_user.username}',category='success')
            return redirect(url_for('market'))
        else:
            flash('username and passward do not match please try again',category='danger')
    return render_template('login.html',form=form) 

@app.route('/logout')
def logout():
    logout_user()
    flash(f"You have been logged out!",category='info')
    return redirect(url_for('home'))


