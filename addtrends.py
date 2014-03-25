from sqlalchemy import *
import numpy as np
from scipy.stats import bernoulli


db = create_engine('sqlite:///forjar.db')



"""
Biases - 

Randomly add bias such that users from twitter do not convert as much.
Make pinterest users the ones who tend to buy things
Ensure lots of traffic from facebook and twitter, slightly more conversions from facebook than twitter.
Lots of liking and sharing on reddit and facebook.
Possibly add slightly more shares for Instagram.



"""

metadata = BoundMetaData(db)

users = Table('Users', metadata, autoload=True)
meals = Table('Meal',metadata ,autoload = True)
events = Table('Event',metadata,autoload = True)



class PriorsUpdater(object):
	def __init__(self,user,table,conn,target_column,priors):
		self.user = user
		self.priors = priors
        self.select = select([table]).where(table.c.User_Id == self.user.id)
        self.results = conn.execute(self.select)
    def update(self):
    	for result in self.results:
             should_gen = bernoulli.rvs(self.priors[result[target_column],size=1)
             if should_gen >= 1:
             	print 'Updating ' + str(result) + ' for user ' + str(self.user)










"""
Priors for bernoulli for sampling wrt to mentioned biases above
"""

TWITTER_CONVERSION_P = 0.2
PINTEREST_BUY = 0.7
SHARE_FACEBOOK_REDDIT = 0.6


user_select = select([users])
meal_select = select([meals])
event_select = select[events])

PRIORS = {
	'TW' : TWITTER_CONVERSION_P,
	'PI' : PINTEREST_BUY,
	'FB' : SHARE_FACEBOOK_REDDIT,
	'RE' : SHARE_FACEBOOK_REDDIT 
}

conn = engine.connect()

all_users = conn.execute(user_select)

for user in all_users:
    updater = PriorsUpdater(user,events,connection,'Type',PRIORS)
    updater.update()
