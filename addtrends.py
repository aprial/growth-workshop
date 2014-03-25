from sqlalchemy import *

db = create_engine('sqlite:///forjar.db')



"""
Biases - 

Randomly add bias such that users from twitter do not convert as much.
Make pinterest users the ones who tend to buy things
Ensure lots of traffic from facebook and twitter, slightly more conversions from facebook than twitter.__add__(
Lots of liking and sharing on reddit and facebook.
Possibly add slightly more shares for Instagram.
"""
