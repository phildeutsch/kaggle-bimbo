# exec(open("connect_db.py").read(), globals())

import pandas as pd
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

db = sql.create_engine('postgresql+pg8000://Philipp.Deutsch:postgres@localhost/bimbo')
db.echo = False

Base = declarative_base()

class Store(Base):
    __tablename__ = 'town_state'

    store_id = sql.Column(sql.String, primary_key=True)
    town = sql.Column(sql.String)
    state = sql.Column(sql.String)

    def __repr__(self):
        return "<Store(id='%s', town='%s', state='%s')>" % (
            self.store_id, self.town, self.state)

class Client(Base):
    __tablename__ = 'clients_dedupe'

    client_id = sql.Column(sql.String, primary_key=True)
    client_name = sql.Column(sql.String)

    def __repr__(self):
        return "<Client(id='%s', name='%s')>" % (
            self.client_id, self.client_name)

class Product(Base):
    __tablename__ = 'products'

    product_id = sql.Column(sql.String, primary_key=True)
    product_name = sql.Column(sql.String)

    def __repr__(self):
        return "<Product(id='%s', name='%s')>" % (
            self.product_id, self.product_name)

class Train(Base):
    __tablename__ = 'train'

    week = sql.Column(sql.Integer)
    store_id = sql.Column(sql.String)
    channel_id = sql.Column(sql.String)
    route_id = sql.Column(sql.String)
    client_id = sql.Column(sql.Integer)
    product_id = sql.Column(sql.String)
    sales_vol = sql.Column(sql.Integer)
    sales_val = sql.Column(sql.Numeric)
    returns_vol = sql.Column(sql.Integer)
    returns_val = sql.Column(sql.Numeric)
    demand = sql.Column(sql.Integer)
    id = sql.Column(sql.Integer, primary_key=True)

class Test(Base):
    __tablename__ = 'test'

    id = sql.Column(sql.Integer, primary_key=True)
    week = sql.Column(sql.Integer)
    store_id = sql.Column(sql.String)
    channel_id = sql.Column(sql.String)
    route_id = sql.Column(sql.String)
    client_id = sql.Column(sql.Integer)
    product_id = sql.Column(sql.String)

Session = sql.orm.sessionmaker(bind=db)
session = Session()

#stores = session.query(Store).limit(10)
#df = pd.read_sql(stores.statement, stores.session.bind)
