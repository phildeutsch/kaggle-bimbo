from collections import Counter
import numpy as np
import pandas as pd

exec(open("connect_db.py").read(), globals())

def predict():
    # Get the most common occurence of Demanda_uni_equil
    query = (
        session.query(Train.demand, func.count(Train.demand).label('count')).
        group_by(Train.demand).order_by(-func.count(Train.demand)).limit(1)
    )
    df = pd.read_sql(query.statement, query.session.bind)
    most_common = df['demand'].iloc[0]

    # Predict the most common value throughout
    query = session.query(Test.id, Test.product_id)
    submission = pd.read_sql(query.statement, query.session.bind)
    submission['demand'] = most_common

    # Get the average demand by product
    query = (
        session.query(Train.product_id, func.avg(Train.demand).label('demand_product')).
        group_by(Train.product_id)
    )
    byproduct = pd.read_sql(query.statement, query.session.bind)

    # merge product average
    submission = pd.merge(
                    submission, byproduct, on='product_id', how='left')

    # Overwrite generic prediction if we have a better product prediction
    submission['demand'][-np.isnan(submission.demand_product)] = \
        submission['demand_product'][-np.isnan(submission.demand_product)]

    # Delete columns we don't need
    submission.drop(['product_id', 'demand_product'], axis=1, inplace=True)

    # write file
    submission.to_csv('submissions/avg_demand_by_product2.csv', index=False)
