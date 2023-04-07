# How the pkl file is made: Do your ml model making magic...
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Read in the DF
df = pd.read_csv('https://www.ishelp.info/data/insurance.csv')

# Generate dummy variables
for col in df:
  if not pd.api.types.is_numeric_dtype(df[col]):
    df = pd.get_dummies(df, columns=[col], drop_first=True)

# Set your y and X
y = df['charges']
X = df.drop(columns=['charges']) # No need to assign const=1 using the sklearn package

# Normalize data
X = pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(X), columns=X.columns)

# Split it up
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Fit the model (in this case we name our model reg)
reg = LinearRegression().fit(X_train, y_train)


# Now we get to wrap the model up into a nice package. This package will be a pickle (pkl)

# Export trained model to .pkl file. Make the path whatever you need it to be in your case
# This will create the model.pkl file for you that the app.py refers to. 
with open('./model.pkl','wb') as file:
  pickle.dump(reg,file)