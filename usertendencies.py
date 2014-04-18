import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sqlalchemy.orm import sessionmaker
from churndata import *
from pandas import DataFrame
from util import query_to_df
from util import campaign_to_num,event_to_num,transform_column,hist_and_show
db = create_engine('sqlite:///forjar.db')


metadata = MetaData(db)

Session = sessionmaker(bind=db)


session = Session()


q = session.query(Users.Campaign_ID,Event.Type)
d = query_to_df(session,session.query(Users.Campaign_ID,Event.Type))

transform_column(d,'Users_Campaign_ID',campaign_to_num.get)
transform_column(d,'Event_Type',event_to_num.get)

hist_and_show(d,'Users_Campaign_ID')
hist_and_show(d,'Event_Type')







