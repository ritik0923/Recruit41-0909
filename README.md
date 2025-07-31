# Recruit41-0909
import pandas as pd 
import sqlite3

df = pd.read_csv("C:\Users\Ritik\OneDrive\Desktop\Recruit41\products.csv")

df = df.fillna('')

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("""
               create table if not exists products(
                   cost REAL,
                   id intger primary key,
                   category text,
                   name text,
                   brand text,
                   retail_price real,
                   department text,
                   sku text,
                   distribution_center_id integer
                   
               )""")

for _, row in df.iterrows():
    cursor.execute("""
                   insert or ignore into products (
                       cost, id, category, name, barand, retail_price, department, sku, distribution_center_id) values(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (row['cost'], row['id'], row['category'], row['name'], row['brand'], 
                        row['retail_price'], row['sku'], row['distribution_center_id']))

conn.commit()
print("Data inserted into sqlite successfully!")

cursor.execute("select * from products limit 5")
rows = cursor.fetchall()

for row in rows:
    print(row)
    
conn.close
