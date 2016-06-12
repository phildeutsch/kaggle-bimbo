import pandas as pd
import os
from config import *

try:
    NROWS
except NameError:
    NROWS = None

town_state = pd.read_csv('raw/town_state.csv', nrows=NROWS)
products = pd.read_csv('raw/producto_tabla.csv', nrows=NROWS)
clients = pd.read_csv('raw/cliente_tabla.csv', nrows=NROWS)
test = pd.read_csv('raw/test.csv', nrows=NROWS)
train = pd.read_csv('raw/train.csv', nrows=NROWS)
sample_submission = pd.read_csv('raw/sample_submission.csv', nrows=NROWS)
