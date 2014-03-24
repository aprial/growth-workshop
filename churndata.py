from forjar import *
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
    User_ID = Column(Integer, primary_key=True)
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
	Meal_Id = Column(Integer,primary_key = True)
	price = Column(Integer)
	def forge(self,session,basetime,date,**kwargs):
		self.Type = random.choice(['japanese','chinese','french','german','italian','mexican','vietnamese'])
        self.price = random.randint(5, 15)
	@classmethod
	def ntimes(self, i, time):
		return 1*pow(1.001, i)

	variance = ntimes


"""
Events on a site are for likes/favorites and buying.
"""
class Event(Base):
	__tablename__ = 'Events'
	date  = Column(DateTime, default=datetime.datetime.utcnow)
	User_ID = Column(Integer, ForeignKey("Users.User_ID"), nullable=False)
	Meal_Id = Column(Integer,ForeignKey("Meal.Meal_Id"),nullable = False)
	Type = Column(String(40))


	def forge(self,session,basetime,date,**kwargs):
		self.Type = random.choice(['like','bought'])
		self.User_ID = get_random(Users,session=session,basetime=basetime)
		self.Meal_Id = get_random(Meal,session=session,basetime=basetime)
