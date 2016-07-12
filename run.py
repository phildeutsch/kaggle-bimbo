from models import *

# print("Loading data")
# import data
#
# print("Predicting most common demand")
# most_common.predict(data.train, data.test)
#
# print("predicting most common demand by product")
# average_demand_by_product.predict(data.train, data.test)

# Average demand by product, but using SQLAlchemy
average_demand_by_product_2()

# Use the average by product and store if available
average_demand_by_product_store()
