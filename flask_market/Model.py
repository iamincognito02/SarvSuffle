from flask_market import db, login_manager
from flask_market import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True,nullable=False)
    username=db.Column(db.String(length=15),nullable=False,unique=True)
    email_address=db.Column(db.String(length=50),unique=True,nullable=False)
    passward_hash=db.Column(db.String(length=10),nullable=False)
    budget=db.Column(db.Integer(),default=1000)
    items=db.relationship("Item",backref='owned_user',lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >=4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    @property
    def passward(self):
        return self.passward
    
    @passward.setter
    def passward(self,plain_text_passward):
        self.passward_hash=bcrypt.generate_password_hash(plain_text_passward).decode('utf-8')
    
    def check_passward_correction(self,attempted_passward):
        return bcrypt.check_password_hash(self.passward_hash,attempted_passward)
    
    def can_purchase(self,item_obj):
        return self.budget>=item_obj.price

    def can_sell(self,item_obj):
        return item_obj in self.items
            

    

class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=10),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False) 
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(length=200),nullable=False,unique=True)
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))
    
def __repr__(self):
   return f"Item {self.name}"

def buy(self,user):
    self.owner=user.id
    user.budget -= self.price
    db.session.commit()

def sell(self,user):
    self.owner=None
    user.budget += self.price
    db.session.commit()
