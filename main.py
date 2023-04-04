import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
from scipy import stats

data_shopping=pd.read_csv('train.csv')
data_shopping.head()
data =data_shopping.copy()
data.columns = data.columns.str.lower()
(data.isnull().sum()/len(data))*100

group_mean_weight = data.pivot_table(index = ["item_type"], values = "item_weight", aggfunc = [np.mean])
group_mean_weight
mean_weight = group_mean_weight.iloc[:,[0][0]]
mean_weight
def missing_value(cols):
    item_type = cols[0]
    item_weight =cols[1]
    if pd.isnull(item_weight):
        if item_type == "Baking Goods":
            return 12.277
        elif item_type == "Breads":
            return 11.347
        elif item_type == "Breakfast":
            return 12.768
        elif item_type == "Canned":
            return 12.30
        elif item_type == "Dairy":
            return 13.42
        elif item_type == "Frozen Foods":
            return  12.867061
        elif item_type == "Fruits and Vegetables":
            return 13.224769
        elif item_type == "Hard Drinks":
            return 11.400328
        elif item_type == "Health and Hygiene":
            return 13.142314
        elif item_type == "Household":
            return 13.384736
        elif item_type == "Meat":
            return 12.817344
        elif item_type == "Others":
            return 13.853285
        elif item_type == "Seafood":
            return 12.552843
        elif item_type == "Snack Foods":
            return 12.987880
        elif item_type == "Soft Drinks":
            return 11.847460
        elif item_type == "Starchy Foods":
            return 13.690731
    return item_weight   

data["item_weight"] = data[["item_type","item_weight"]].apply(missing_value, axis = 1)







cols = ['item_identifier', 'item_fat_content',
       'item_type', 'outlet_identifier',
       'outlet_establishment_year', 'outlet_size', 'outlet_location_type',
       'outlet_type']

for i in cols:
    x  = data[i].value_counts().to_dict()
    data[i] = data[i].map(x)

new_data= data.copy()
new_data =new_data.drop(["item_weight","item_identifier", "item_type", "item_fat_content","outlet_location_type"], axis = 1)
new_data.skew()
for i in new_data.columns:
    new_data[i] =np.log(new_data[i])
x = new_data.drop("item_outlet_sales", axis = 1) 

#Depenedent Variables 
y = new_data["item_outlet_sales"].values.reshape(-1,1)
from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test = train_test_split(x,y, test_size =0.20, random_state = 3)
from sklearn.linear_model import LinearRegression
regressor =LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)


test_data = pd.read_csv("test.csv")
test = test_data.copy()
test.columns = test.columns.str.lower()
(test.isnull().sum()/len(test))*100
group_mean = test.pivot_table(index = ["item_type"], values = "item_weight", aggfunc = [np.mean])
mean_weigh = group_mean.iloc[:,[0][0]]
def missing_value1(cols):
    item_type = cols[0]
    item_weight =cols[1]
    if pd.isnull(item_weight):
        if item_type == "Baking Goods":
            return 12.277
        elif item_type == "Breads":
            return 10.86
        elif item_type == "Breakfast":
            return  13.759603
        elif item_type == "Canned":
            return 12.393565
        elif item_type == "Dairy":
            return 12.955040
        elif item_type == "Frozen Foods":
            return  12.101543
        elif item_type == "Fruits and Vegetables":
            return 13.146659
        elif item_type == "Hard Drinks":
            return 11.844417
        elif item_type == "Health and Hygiene":
            return 13.216929
        elif item_type == "Household":
            return 13.270504
        elif item_type == "Meat":
            return 12.702148
        elif item_type == "Others":
            return 14.009725
        elif item_type == "Seafood":
            return 13.241136
        elif item_type == "Snack Foods":
            return 12.684256
        elif item_type == "Soft Drinks":
            return 11.691965
        elif item_type == "Starchy Foods":
            return 13.618247
    return item_weight 

test["item_weight"] = test[["item_type","item_weight"]].apply(missing_value1, axis = 1)
sns.countplot(data = test, x = "outlet_type",hue = "outlet_size")
plt.xticks(rotation =90)
def impute_size1(cols):
    size = cols[0]
    ot_type = cols[1]
    if pd.isnull(size):
        if ot_type == "Supermarket Type1":
            return "Small"
        elif ot_type == "Supermarket Type2":
            return "Medium"
        elif ot_type == "Grocery Store":
            return "Small"
        elif ot_type == "Supermarket Type3":
            return "Medium"
    return size 

test["outlet_size"] = test[["outlet_size","outlet_type"]].apply(impute_size1, axis = 1)
test["item_fat_content"].unique()
test["item_fat_content"] = test["item_fat_content"].str.replace("LF", "low fat").str.replace("reg", "regular").str.lower()
test["item_fat_content"].unique()
mean_item_visibility = test.pivot_table(index = "item_identifier",  values = "item_visibility")
mean_item_visibility.head()
test_d = test.copy()

columns = ['item_identifier', 'item_fat_content',
       'item_type', 'outlet_identifier',
       'outlet_establishment_year', 'outlet_size', 'outlet_location_type',
       'outlet_type']
for i in columns:
    x  = test_d[i].value_counts().to_dict()
    test_d[i] = test_d[i].map(x)
    
new_test_data = test_d.copy()
new_test_data =new_test_data.drop(["item_weight","item_identifier", "item_type", "item_fat_content","outlet_location_type"], axis = 1)
new_test_data.skew()

for i in new_test_data.columns:
    new_test_data[i] =np.log(new_test_data[i]+1)

new_test_data.skew()

# #Independent Variables:
# x = new_.drop("item_outlet_sales", axis = 1) 

# #Depenedent Variables 
# y = new_test_data["item_outlet_sales"].values.reshape(-1,1)

# #Splitting The data  into Train and Test Dataset:
# from sklearn.model_selection import train_test_split
# x_train,x_test, y_train, y_test = train_test_split(x,y, test_size =0.20, random_state = 3)

# #Applying Linear Regression Model
# from sklearn.linear_model import LinearRegression
# regressor =LinearRegression()
# regressor.fit(x_train, y_train)

item_outsale_pred = regressor.predict(new_test_data)
item_outsale_pred
actual_item_outsale = np.exp(item_outsale_pred+1)
actual_item_outsale


