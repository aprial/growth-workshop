import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sqlalchemy.orm import sessionmaker
from churndata import *
from pandas import DataFrame

db = create_engine('sqlite:///forjar.db')


metadata = MetaData(db)

Session = sessionmaker(bind=db)


session = Session()


q = session.query(Users.Campaign_ID,Event.Type)
result = session.execute(q)

d = DataFrame(result.fetchall())
d.columns = result.keys()

print d





