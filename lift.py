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
from pandas import DataFrame,Series
from pandas.core.groupby import GroupBy
from util import query_to_df
from util import campaign_to_num,event_to_num,transform_column,hist_and_show,vectorize,to_percentage,num_rows,vectorize_label,meal_to_num,num_days_apart
db = create_engine('sqlite:///campaign-1.db')


metadata = MetaData(db)

Session = sessionmaker(bind=db)


session = Session()
"""
We only want events and users such that the user bought an item.
We count bought as $1 of revenue for simplicity.
"""

q = session.query(Users.Campaign_ID,Event.Type).filter(Event.Type == 'bought')

"""
Print out the counts by name.
This is a way of showing how to aggregate by campaign ids.
"""
df = query_to_df(session,q)
"""
Basic statistics collecting; calculate the sum for each row.
"""
sum = 0
for campaign_id in campaign_to_num.keys():
    rows = num_rows(df.groupby('Users_Campaign_ID').get_group(campaign_id))
    sum = sum + rows
    print 'id was ' + campaign_id + ' ' + str(rows)

"""
Print the percentage of buy actions for each campaign id
"""
for campaign_id in campaign_to_num.keys():
    rows = num_rows(df.groupby('Users_Campaign_ID').get_group(campaign_id))
    rows = rows / sum
    print 'id was ' + campaign_id + ' and percent of customers bought was ' + str(rows)



"""
Calculate the lift curves

We will take our first data set and use it as a baseline.

We will assume that each user gained was the result of a marketing campaign on each social network.

Our goal here is to calculate the lift curve such that when we run a second campaign, we can see

either improvements or not with respect to the delta. The positive response rate will be marked

by the number of buy actions within the dataset, from there we can calculate a conversion rate.

After wards, we will run similar calculations to visualize a lift curve.

"""



"""
We only want events and users such that the user bought an item.
We count bought as $1 of revenue for simplicity.
"""

q = session.query(Users.Campaign_ID,Meal.Type,Event.Type).limit(300)

"""
Print out the counts by name.
This is a way of showing how to aggregate by campaign ids.
"""
df = query_to_df(session,q)

print df

transform_column(df,'Event_Type',event_to_num.get)
transform_column(df,'Users_Campaign_ID',campaign_to_num.get)
transform_column(df,'Meal_Type',meal_to_num.get)
print df
"""
Prediction scores.

"""
data_set = vectorize(df,'Event_Type')
labels =  vectorize_label(df,'Event_Type',2,4)


# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(data_set, labels, random_state=0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

logistic = LogisticRegression()
fit = logistic.fit(X_train,y_train)
prediction = fit.predict(X_test)
"""
Append the probabilities of true (0,1) to the data trame
"""
probabilities = fit.predict_proba(X_test)[:0]
df['probabilities'] = Series(len(X_test), index=df.index)




cm = confusion_matrix(y_test, prediction)




print probabilities


"""
Multiply the results by a cost benefit matrix.

Grab out probabilities, save out features

Add column churn/not churn (pre recorded) based on order drop off,

Whether they ordered in the last 3 months would be considered churn


Need to add columns for features;

logged in last 90 days
bought in last 30 days
was_active (shared,liked,..) last 30,60,90

Possibly add: mean delivery time for each user (add variance)


For the final list, it's a moving threshold for each instance.




"""










