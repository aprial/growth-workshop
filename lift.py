from __future__ import division
import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from churndata import *
from pandas import DataFrame
from pandas.core.groupby import GroupBy
from util import query_to_df
from util import campaign_to_num,event_to_num,transform_column,hist_and_show,vectorize,to_percentage,num_rows
db = create_engine('sqlite:///forjar.db')


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


