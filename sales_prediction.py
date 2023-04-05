import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
data_shopping=pd.read_csv('train.csv')

data =data_shopping.copy()

data.columns = data.columns.str.lower()

group_mean_weight = data.pivot_table(index = ["item_type"], values = "item_weight", aggfunc = [np.mean])

mean_weight = group_mean_weight.iloc[:,[0][0]]

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

def impute_size(cols):
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

data["outlet_size"] = data[["outlet_size","outlet_type"]].apply(impute_size, axis = 1)


data["item_fat_content"] = data["item_fat_content"].str.replace("LF", "low fat").str.replace("reg", "regular").str.lower()


mean_visibility = data.pivot_table(index = "item_identifier",  values = "item_visibility")

data.loc[(data["item_visibility"] == 0.0), "item_visibility"] = data.loc[(data["item_visibility"] == 0.0), "item_identifier"].apply(lambda x : mean_visibility.at[x, "item_visibility"])


cols = ['item_identifier', 'item_fat_content',
       'item_type', 'outlet_identifier',
       'outlet_establishment_year', 'outlet_size', 'outlet_location_type',
       'outlet_type']


for i in cols:
    x  = data[i].value_counts().to_dict()
    data[i] = data[i].map(x)

new_data= data.copy()

new_data =new_data.drop(["item_weight","item_identifier", "item_type", "item_fat_content","outlet_location_type"], axis = 1)

for i in new_data.columns:
    new_data[i] =np.log(new_data[i])

x = new_data.drop("item_outlet_sales", axis = 1) 
#Depenedent Variables 
y = new_data["item_outlet_sales"].values.reshape(-1,1)


# x_train,x_test, y_train, y_test = train_test_split(x,y, test_size =0.20, random_state = 3)

li =LinearRegression()
li.fit(x,y)



def predict_sales(**Input_values):
    print(Input_values)
    new_df = pd.DataFrame({
        'item_identifier': Input_values['Item_Identifier'],
        'item_weight' : [float(Input_values['Item_Weight'])],
        'item_visibility' : [float(Input_values['Item_Visibility'])],
        'item_fat_content' : Input_values['Item_Fat_Content'],
        'item_type': Input_values['Item_Type'], 
        'item_mrp':[float(Input_values['Item_MRP'])],
        'outlet_identifier':Input_values['Outlet_ID'],
        'outlet_establishment_year':[int(Input_values['Outlet_Establishment_Year'])],
        'outlet_size':Input_values['Outlet_Size'],
        'outlet_location_type' : Input_values['Outlet_Location'],
        'outlet_type':Input_values['Outlet_Type'],
    })
    
    new_df.columns = new_df.columns.str.lower()

    group_mean_weight = data.pivot_table(index = ["item_type"], values = "item_weight", aggfunc = [np.mean])

    mean_weight = group_mean_weight.iloc[:,[0][0]]
    
    new_df["item_weight"] = new_df[["item_type","item_weight"]].apply(missing_value, axis = 1)

    new_df["item_fat_content"] = new_df["item_fat_content"].str.replace("LF", "low fat").str.replace("reg", 
       "regular").str.lower()
    
    mean_visibility = data.pivot_table(index = "item_identifier",  values = "item_visibility")
    new_df.loc[(new_df["item_visibility"] == 0.0), "item_visibility"] = new_df.loc[(data["item_visibility"] == 
       0.0), "item_identifier"].apply(lambda x : mean_visibility.at[x, "item_visibility"])
    
    for i in cols:
      x  = new_df[i].value_counts().to_dict()
      new_df[i] = new_df[i].map(x)

    new_data_df =new_df.drop(["item_weight","item_identifier", "item_type", 
         "item_fat_content","outlet_location_type"], axis = 1)
    
    result = li.predict(new_data_df)
    
    return int(result)






