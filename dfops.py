from util import query_to_df
from churndata import *
from sqlalchemy import *
import numpy as np
from datetime import datetime,timedelta
from sklearn.linear_model import LogisticRegression
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

db = create_engine('sqlite:///forjar.db')


metadata = MetaData(db)

Session = sessionmaker(bind=db)


session = Session()


def most_recent_visits():
     """
     Returns the most recent visits for a user, primarily used in featurizing
     """
     visits = session.query(Users).join(Visit).add_entity(Visit).group_by(Users.id).order_by(Visit.date.desc())
     return query_to_df(session, visits)



def most_recent_actions():
     """
     Returns the most recent events for a user, primarily used in featurizing
     """
     events = session.query(Users).join(Event).add_entity(Event).group_by(Users.id).order_by(Event.date.desc())
     return query_to_df(session, events)


def user_visited_in_last_90_days():
    now = datetime.utcnow()
    ninety_days = now - timedelta(days=90)
    """
    Only grab the logins that occurred in the last 90 days
    """
    most_recent_user_visits = session.query(Users).join(Visit,Users.id == Visit.user_id).group_by(Users.id).order_by(Visit.date.desc()).add_entity(Visit).filter(Visit.date < ninety_days)
    print query_to_df(session,most_recent_user_visits)



print user_visited_in_last_90_days()