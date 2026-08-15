import pandas as pd 

filtered_df = df[df['amount'] > 50]

avg_price_by_category = df.groupby('category')['price'].mean()

df['total'] = df['quantity'] * df['price']

cleaned_df = df.dropna(subset=['email'])

sorted_df = df.sort_values('date', ascending=False)