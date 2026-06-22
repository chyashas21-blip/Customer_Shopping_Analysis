
import pandas as pd
df = pd.read_csv("customer_shopping_behavior.csv", encoding="latin1")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())

df.columns = df.columns.str.lower()                                     
df.columns = df.columns.str.replace(" ", "_")
df= df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

#creating a new column 'age_group' using qcut
labels = ['young adult', 'adult','middle aged','senior']
df["age_group"]= pd.qcut(df['age'], q=4, labels= labels)
print(df[['age','age_group']].head(10))

#creating a column purchase frequency days using .map
frequency_mapping = {
    "Fortnightly":14,
    "Weekly":7,
    "Monthly":30,
    "Quarterly":90,
    "Bi-weekly":14,
    "Annually":365,
    "Every 3 months":90
}
df["purchase_frequency_days"]= df["frequency_of_purchases"].map(frequency_mapping)
print(df.head(10))

#checking for column "promo_code_used" & "discount_applied" are same or not
print(df[["promo_code_used","discount_applied"]].head(10))
print((df["promo_code_used"]==df["discount_applied"]).all())
#so both carry same details and we can remove one column i.e promo code
df= df.drop("promo_code_used",axis=1)
print(df.columns)

df= df.rename(columns={'ï»¿customer_id':'customer_id'})

print(df.columns)

df.to_csv("customer_shopping_behaviour.csv",index= False)

import pymysql 
from sqlalchemy import create_engine
try:
    engine_mysql=create_engine("mysql+pymysql://root:veenank@localhost:3306/customer_shopping_behaviour")
    print("Connection Successful")
except:
    print("Failed")
print(df.to_sql(name="customer",con= engine_mysql,if_exists="replace",index=False))