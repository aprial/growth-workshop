import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np

db = create_engine('sqlite:///forjar.db')


metadata = MetaData(db)


users = Table('Users', metadata, autoload=True)

s = users.select()
rs = s.execute()

campaign_to_num = {
	'TW' : 1,
	'RE' : 2,
    'FB' : 3,
    'PI' : 4
}

campaigns = []


Session = sessionmaker(bind=some_engine)
session = Session()
q = session.query(users)


for row in rs:
    campaigns.append(campaign_to_num[row.Campaign_ID])



x = np.array(campaigns)

n, bins, patches = plt.hist(x,bins=4,label=['TW', 'RE', 'FB','PI'])


plt.xlabel('Campaigns ')
plt.ylabel('Number')
plt.title('Histogram of Users from Different Campaigns')
plt.grid(True)
plt.show()


print x