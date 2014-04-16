import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sqlalchemy.orm import sessionmaker
from churndata import *

db = create_engine('sqlite:///forjar.db')


metadata = MetaData(db)

Session = sessionmaker(bind=db)


session = Session()


q = session.query(Users.Campaign_ID,Event.Type)
result = session.execute(q)

instances = q.instances(result)


#Visualize histograms of users to events, need to discretize (map string values to numbers)
l = []
for r in result:
	l.append(r)
arr = np.asarray(l)

n, bins, patches = plt.hist(arr,label=['TW', 'RE', 'FB','PI'])


plt.xlabel('Campaigns ')
plt.ylabel('Number')
plt.title('Histogram of Users from Different Campaigns')
plt.grid(True)
plt.show()





