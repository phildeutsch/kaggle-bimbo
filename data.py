import pandas as pd
import os

NROWS = 1000
# NROWS = None

town_state = pd.read_csv('raw/town_state.csv')
products = pd.read_csv('raw/producto_tabla.csv')
clients = pd.read_csv('raw/cliente_tabla.csv')
test = pd.read_csv('raw/test.csv')
train = pd.read_csv('raw/train.csv', nrows=NROWS)
sample_submission = pd.read_csv('raw/sample_submission.csv')
