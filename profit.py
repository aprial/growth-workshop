import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sqlalchemy.orm import sessionmaker
from churndata import *
from pandas import DataFrame
from util import query_to_df
from util import campaign_to_num,event_to_num,transform_column,hist_and_show,vectorize
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
Convert to pandas
"""
df = query_to_df(session,q)
print df

"""
Map it to numbers such that it can be histogrammed.
Then plot the user campaign ids, remember, we already
filtered by the bought action, so visualizing the counts of the
campaign ids, gives us an idea of what campaigns bought more.
"""
transform_column(df,'Users_Campaign_ID',campaign_to_num.get)
transform_column(df,'Event_Type',event_to_num.get)

hist_and_show(df,'Users_Campaign_ID')


