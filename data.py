import pandas as pd

df=pd.read_csv('/Users/tjeff/Desktop/CODING/Web-Design-Challenge/Resources/cities.csv')
df.to_html('data.html', index=False)
table = df.to_html()
print(table)