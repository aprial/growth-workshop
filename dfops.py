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
     events = session.query(Users).join(Event).add_entity(Event).group_by(Users.id).order_by(Event.date.desc()).subquery()

     return query_to_df(session, events)


def user_visited_in_last_k_days(threshold):
    now = datetime.utcnow()
    days = now - timedelta(days=threshold)
    """
    Only grab the logins that occurred in the last 90 days
    """
    most_recent_user_visits = session.query(Users.id,Visit.date).join(Visit,Users.id == Visit.user_id).order_by(Visit.date.desc()).group_by(Users.id)

    df = query_to_df(session,most_recent_user_visits)
    df = df.sort('Users_id')
    df['churned'] = df['visit_date'].apply(lambda x : x < days)
    return df


print user_visited_in_last_k_days(90)

