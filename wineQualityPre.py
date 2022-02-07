import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def quality_chec(df):
    # df=pd.DataFrame(a,b,c,d,e,f,g,h)
    # df=df(1,-1)
    data=pd.read_csv("winequality-red.csv")


    # droping some colums for our data
    data.drop("residual sugar",axis=1,inplace=True)
    data.drop("free sulfur dioxide",axis=1,inplace=True)
    data.drop("pH",axis=1,inplace=True)

    # importing sklearn
    from sklearn.preprocessing import StandardScaler
    scaler=StandardScaler()
    scaler.fit(data.drop('quality', axis=1))
    train_data=data.drop('quality', axis=1)
    # test_data=data["quality"]
    # from sklearn.model_selection import train_test_split
    # x_train, x_test, y_train, y_test = train_test_split(train_data,data.quality,test_size=0.30)
    from sklearn.neighbors import KNeighborsRegressor
    knn=KNeighborsRegressor(n_neighbors = 4)
    # knn.fit(x_train ,y_train)
    knn.fit(train_data ,data["quality"])
    return (knn.predict(df).astype(int))

