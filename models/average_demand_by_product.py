from collections import Counter
import numpy as np

def predict(df_train, df_test):
    # Get the most common occurence of Demanda_uni_equil
    demand_vals = df_train['Demanda_uni_equil'].tolist()
    most_common = Counter(demand_vals).most_common(1)[0][0]

    # Predict the most common value throughout
    submission = df_test[['id', 'Producto_ID']]
    submission['Demanda_uni_equil'] = most_common

    # Get the average demand by product
    byproduct = (df_train.groupby('Producto_ID').
                    agg({'Demanda_uni_equil': 'mean'}))
    byproduct = byproduct.reset_index()
    byproduct = byproduct.rename(
                    columns={'Demanda_uni_equil': 'Product_Demand'})

    # merge product average
    submission = pd.merge(
                    submission, byproduct, on='Producto_ID', how='left')

    # Overwrite generic prediction if we have a better product prediction
    submission['Demanda_uni_equil'][-np.isnan(submission.Product_Demand)] = \
        submission['Product_Demand'][-np.isnan(submission.Product_Demand)]

    # Delete columns we don't need
    submission.drop(['Producto_ID', 'Product_Demand'], axis=1, inplace=True)

    # write file
    submission.to_csv('submissions/avg_demand_by_product.csv', index=False)
