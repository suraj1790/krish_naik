from idlelib.configdialog import font_sample_text

import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np


iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df["Species"] = iris.target.data
dic = {0:"setosa",1:"versicolor",3:"virginica"}
df.replace({"Species":dic})

sepal_len = st.slider("Sepal_length",2.0,10.0,step=0.1)
sepal_wid = st.slider("Sepal_width",1.0,5.0,step=0.1)
petal_len = st.slider("petal_length",0.0,8.0,step=0.1)
petal_wid = st.slider("petal_width",0.0,3.0,step=0.1)

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

rf = RandomForestClassifier(n_estimators=50)
rf.fit(x,y)

data = np.array([sepal_len,sepal_wid,petal_len,petal_wid]).reshape(1,4)
st.write(data)
my_prid = rf.predict(data)

st.write(my_prid)

st.line_chart(df)



st.write(df)
# st.write(iris)