from __future__ import division
import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sklearn.linear_model import LogisticRegression
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from churndata import *
from sklearn.preprocessing import StandardScaler
from pandas import DataFrame
from pandas.core.groupby import GroupBy
from util import query_to_df
from util import campaign_to_num,event_to_num,transform_column,hist_and_show,vectorize,to_percentage,num_rows,vectorize_label,meal_to_num,to_milliseconds
db = create_engine('sqlite:///forjar.db')


metadata = MetaData(db)

Session = sessionmaker(bind=db)


session = Session()

q = session.query(Users,Referral)

df = query_to_df(session,q)

transform_column(df,'Users_Campaign_ID',campaign_to_num.get)
df['Users_date'] = df['Users_date'].apply(to_milliseconds)
x = df['Users_date']
y = df['Users_Campaign_ID']

print x

df.plot(x='Users_date',y='Users_Campaign_ID',kind='scatter')

plt.show()






