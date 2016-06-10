import pandas as pd
import os

town_state = pd.read_csv('../Data/town_state.csv')
products = pd.read_csv('../Data/producto_tabla.csv')
clients = pd.read_csv('../Data/cliente_tabla.csv')
test = pd.read_csv('../Data/test.csv')
train = pd.read_csv('../Data/train.csv')
sample_submission = pd.read_csv('../Data/sample_submission.csv')

# Print first few lines of each table
town_state.head()
products.head()
clients.head()
test.head()
train.head()
sample_submission.head()
