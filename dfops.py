from util import query_to_df
from churndata import *
from sqlalchemy import *
import numpy as np
from sklearn.linear_model import LogisticRegression
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

db = create_engine('sqlite:///campaign-1.db')


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


