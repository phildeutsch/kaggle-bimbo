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
    query = session.query(Test.id, Test.product_id, Test.store_id)
    base = pd.read_sql(query.statement, query.session.bind)
    base['demand'] = most_common

    # Get the average demand by product
    query = (
        session.query(Train.product_id, func.avg(Train.demand).label('demand_product')).
        group_by(Train.product_id)
    )
    byproduct = pd.read_sql(query.statement, query.session.bind)

    # Get the average demand by product and store
    query = (
        session.query(Train.product_id, Train.store_id, func.avg(Train.demand).label('demand_product_store')).
        group_by(Train.product_id, Train.store_id)
    )
    byproductstore = pd.read_sql(query.statement, query.session.bind)

    # merge product average
    submission = pd.merge(base, byproductstore, on=['product_id', 'store_id'], how='left')
    submission = pd.merge(submission, byproduct, on='product_id', how='left')

    # Overwrite generic prediction if we have a better product prediction
    submission['demand'][-np.isnan(submission.demand_product)] = \
        submission['demand_product'][-np.isnan(submission.demand_product)]
    submission['demand'][-np.isnan(submission.demand_product_store)] = \
        submission['demand_product_store'][-np.isnan(submission.demand_product_store)]

    # Delete columns we don't need, reorder and rename
    submission.drop(['product_id', 'store_id', 'demand_product', 'demand_product_store'], axis=1, inplace=True)
    submission.sort_values(by='id', inplace=True)
    submission.columns = ['id', 'Demanda_uni_equil']

    # write file
    submission.to_csv('submissions/avg_demand_by_product_store.csv', index=False)
