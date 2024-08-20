import pandas as pd
from datetime import datetime

data = {
    'customer_id': [1, 1, 1, 2, 2, 3],
    'order_date': ['2023-01-01', '2023-02-15', '2023-03-10', '2023-01-15', '2023-04-05', '2023-03-20'],
    'order_value': [100, 150, 80, 200, 120, 90]
}

df = pd.DataFrame(data)

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Calculate metrics
rfm = df.groupby('customer_id').agg(
    recency=('order_date', lambda x: (df['order_date'].max() - x.max()).days),
    monetary_value=('order_value', 'sum'),
    frequency=('order_date', 'nunique')
)

# RFM scores
rfm['recency_score'] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['frequency_score'] = pd.qcut(rfm['frequency'], 5, labels=[1, 2, 3, 4, 5])
rfm['monetary_score'] = pd.qcut(rfm['monetary_value'], 5, labels=[1, 2, 3, 4, 5])
rfm['RFM_Score'] = rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str) + rfm['monetary_score'].astype(str)  


print(rfm)