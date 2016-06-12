from collections import Counter

def predict(df_train, df_test):
    # Get the most common occurence of Demanda_uni_equil
    demand_vals = df_train['Demanda_uni_equil'].tolist()
    most_common = Counter(demand_vals).most_common(1)[0][0]

    # Predict the most common value throughout
    submission = df_test['id'].to_frame()
    submission['Demanda_uni_equil'] = most_common

    # write file
    submission.to_csv('submissions/most_common.csv', index=False)
