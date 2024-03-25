import xgboost as xgb
from data_preprocessing import make_all_process
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")

# take data from preprocessing file 
df = make_all_process()
# split data into train and test 
train = df.iloc[:-90]
test = df.iloc[-90:]


def make_count_model(X_train, y_train):
    model_count = xgb.XGBRegressor(
        objective='reg:squarederror',
        min_child_weight=5,
        # minimum sum of instance weight (hessian) needed in a child. This can be used to control the complexity of the decision tree by preventing the creation of too small leaves. good values for try are 1, 5, 15, 200
        subsample=0.7,
        # percentage of rows used for each tree construction. Lowering this value can prevent overfitting by training on a smaller subset of the data. It is common to set this value between 0.5 and 1
        # colsample_bytree=0.7,          #percentage of columns used for each tree construction. Lowering this value can prevent overfitting by training on a subset of the features.
        gamma=15,
        # minimum loss reduction required to make a further partition on a leaf node of the tree. Higher values increase the regularization.
        alpha=15,
        colsample_bytree=0.7,
        num_boost_round=20,
        max_depth=7,
        learning_rate=0.001,
        n_estimators=20000,
        reg_lambda=0.001,
        random_state=101
    )
    model_count.fit(X_train_count, y_train_count)
    return model_count


def make_sell_model(x, y):
    model_xgb = xgb.XGBRegressor(
        objective='reg:squarederror',
        min_child_weight=1,
        # minimum sum of instance weight (hessian) needed in a child. This can be used to control the complexity of the decision tree by preventing the creation of too small leaves. good values for try are 1, 5, 15, 200
        subsample=0.8,
        # percentage of rows used for each tree construction. Lowering this value can prevent overfitting by training on a smaller subset of the data. It is common to set this value between 0.5 and 1
        colsample_bytree=0.7,
        # percentage of columns used for each tree construction. Lowering this value can prevent overfitting by training on a subset of the features.
        # gamma=15,                     #minimum loss reduction required to make a further partition on a leaf node of the tree. Higher values increase the regularization.
        # alpha=15,
        num_boost_round=20,
        max_depth=12,
        learning_rate=0.001,
        n_estimators=20000,
        reg_lambda=0.001,
        random_state=101
    )

    model_xgb.fit(x, y)
    return model_xgb


if __name__=="__main__":
    # create train and test values for tranined model amount
    # Split data into X_train, X_test and ...
    # X_train_count, y_train_count = train[['year', 'month', 'day', 'id_prd_to_plc', 'season', 'series', 'event']] , train[['amount']]
    # X_test_count, y_test_count = test[['year', 'month', 'day', 'id_prd_to_plc', 'season', 'series', 'event']] , test[['amount']]
    X_train_count, y_train_count = train[['year', 'month', 'day', 'id_prd_to_plc', 'season', 'series', 'event']], train[
        ['amount']]
    X_test_count, y_test_count = test[['year', 'month', 'day', 'id_prd_to_plc', 'season', 'series', 'event']], test[
        ['amount']]
    # train model count
    model_count = make_count_model(X_train=X_train_count, y_train=y_train_count)
    preds_count = model_count.predict(X_test_count)
    preds_count = np.round(preds_count)

    # create train adn test values for model sales
    # X_train, y_train = train[['year', 'month', 'day','id_prd_to_plc', 'season',
    #                           'series', 'event', 'event_percent', 'amount']] , train[['total_price']]
    # X_test, y_test = test[['year', 'month', 'day','id_prd_to_plc', 'season',
    #                        'series', 'event', 'event_percent']] , test[['total_price']]
    X_train, y_train = train[['year', 'month', 'day', 'id_prd_to_plc', 'season',
                              'series', 'event', 'amount']], train[['total_price']]
    X_test, y_test = test[['year', 'month', 'day', 'id_prd_to_plc', 'season',
                           'series', 'event']], test[['total_price']]

    # predict new amounts for test values
    preds_count = model_count.predict(X_test_count)
    preds_count = np.round(preds_count)

    X_test['amount'] = preds_count
    # train model sales
    model_xgb = make_sell_model(x=X_train, y=y_train)
    # save models
    filename_count = 'apps/home/buisness/models/count_model.pkl'
    pickle.dump(model_count, open(filename_count, 'wb'))

    filename_sale = 'apps/home/buisness/models/sale_model.pkl'
    pickle.dump(model_xgb, open(filename_sale, 'wb'))
