import pandas as pd
from models import most_common, average_demand_by_product

print("Loading data")
import data

print("Predicting most common demand")
most_common.predict(data.train, data.test)

print("predicting most common demand by product")
average_demand_by_product.predict(data.train, data.test)
