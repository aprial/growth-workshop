from forjar import *
from scipy.stats import bernoulli




"""
Generates a user table for cohort analysis and churn prediction.
A few things of note below:

Campaigns are from social networks. This is primarily meant to measure click data.
    FB: facebook
    TW: twitter
    RE: reddit
    PI: pinterst

Each of these campaigns are represenative of a cohort.
"""
class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    date  = Column(DateTime, default=datetime.datetime.utcnow)
    Campaign_ID = Column(String(40))
    Created_Date  = Column(DateTime, default=datetime.datetime.utcnow)

    def forge(self, session, basetime, date, **kwargs):
        self.Campaign_ID = random.choice(['FB','TW','RE','PI'])
        self.Created_Date = date
        
    period = DAY
    @classmethod
    def ntimes(self, i, time):
        return 1*pow(1.005, i)

    variance = ntimes

"""
Meals are of different types. The idea here would be that 
different kinds of users may like or buy different kinds of meals on the site.
For brevity, the types will be restricted to categories.
"""
class Meal(Base):

    __tablename__ = 'Meal'
    Type = Column(String(40))
    date  = Column(DateTime, default=datetime.datetime.utcnow)
    id = Column(Integer,primary_key = True)
    price = Column(Integer)
    def forge(self,session,basetime,date,**kwargs):
        self.Type = random.choice([
            'japanese',
            'chinese',
            'french',
            'german',
            'italian',
            'mexican',
            'vietnamese'
        ])
        self.price = random.randint(5, 15)
        
	period = DAY
    @classmethod
    def ntimes(self, i, time):
    	return 1*pow(1.005, i)
    
    variance = ntimes

"""
Events on a site are for likes/favorites and buying.
"""
class Event(Base):

    __tablename__ = 'Event'
    id = Column(Integer,primary_key = True)
    date  = Column(DateTime, default=datetime.datetime.utcnow)
    User_Id= Column(Integer, ForeignKey("Users.id"), nullable=False)
    Meal_Id = Column(Integer,ForeignKey("Meal.id"),nullable = False)
    Type = Column(String(40))


    def forge(self,session,basetime,date,**kwargs):
         self.Type = random.choice(['like','bought','share','nothing'])
         self.User_Id = get_random(Users,session=session,basetime=basetime)
         user = session.query(Users).filter_by(id = self.User_Id).all()[0]
         if user.Campaign_ID == 'TW':
             should_gen = bernoulli.rvs(0.7,size=1)
             if should_gen >= 1:
                self.Type = 'nothing'

         elif user.Campaign_ID == 'RE':
             should_gen = bernoulli.rvs(0.6,size=1)
             if should_gen >= 1:
                self.Type = 'share'

         elif user.Campaign_ID == 'FB':
             should_gen = bernoulli.rvs(0.6,size=1)
             if should_gen >= 1:
                 self.Type = 'like'
         elif user.Campaign_ID == 'PI':
             should_gen = bernoulli.rvs(0.7,size=1)
             if should_gen >= 1:
                self.Type = 'bought'
         
         print 'Campaign ' + user.Campaign_ID + ' with ' + self.Type
         self.Meal_Id = get_random(Meal,session=session,basetime=basetime)
         
    period = DAY
    @classmethod
    def ntimes(self, i, time):
    	return 1*pow(1.001, i)
    
    variance = ntimes


def main(forjar):
    forjar.forge_base(Users)
    forjar.forge_base(Meal)
    forjar.forge_base(Event)

    forjar.session.commit()
    forjar.print_results()

if __name__ == "__main__":
    forjar_main(main=main)
