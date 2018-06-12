from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Florist, Base, Bouquet, User

engine = create_engine('sqlite:///flowers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

User1 = User(name="Pradeepthi", email="pradeepthiyadavalli222@gmail.com")
session.add(User1)
session.commit()


# Designs of Dutch Florist
florist1 = Florist(user_id=1, name="Dutch Florist")

session.add(florist1)
session.commit()

bouquet1 = Bouquet(user_id=1, name="Cascade Bouquet",
                   description="It features a waterfall of flowers ",
                   price="$120.00", course="wedding", florist=florist1)

session.add(bouquet1)
session.commit()


bouquet2 = Bouquet(user_id=1, name="posy Bouquet",
                   description="it is small enough to be held in hands",
                   price="$175.00", course="Engagement", florist=florist1)

session.add(bouquet2)
session.commit()

bouquet3 = Bouquet(user_id=1, name="Hand-Tied",
                   description="Freer than other bouquet styles",
                   price="$200.50", course="anniversary", florist=florist1)

session.add(bouquet3)
session.commit()

bouquet4 = Bouquet(user_id=1, name="Round Bouquet",
                   description="These are formed into perfect domes",
                   price="$100.00", course="wedding", florist=florist1)

session.add(bouquet4)
session.commit()


# Designs of Aster Florist
florist2 = Florist(user_id=1, name="Aster Florist")

session.add(florist2)
session.commit()

bouquet1 = Bouquet(user_id=1, name="Nosegay Bouquet",
                   description="Nosegays place more emphasis on greenery",
                   price="$s0.00", course="wedding", florist=florist2)

session.add(bouquet1)
session.commit()


bouquet2 = Bouquet(user_id=1, name="pomander Bouquet",
                   description="Perfectly round spheres of blooms",
                   price="$70.00", course="Engagement", florist=florist2)

session.add(bouquet2)
session.commit()

bouquet3 = Bouquet(user_id=1, name="Composite Bouquet",
                   description="It composed of individual petals",
                   price="$80.50", course="anniversary", florist=florist2)

session.add(bouquet3)
session.commit()

bouquet4 = Bouquet(user_id=1, name="Shower Bouquet",
                   description="It gracefully flow out the brides hands",
                   price="$70.00", course="wedding", florist=florist2)

session.add(bouquet4)
session.commit()


# Designs of Ferns N Petals
florist3 = Florist(user_id=1, name="Ferns N Petals")

session.add(florist3)
session.commit()

bouquet1 = Bouquet(user_id=1, name="Presentation Bouquet",
                   description="It is a sheaf of flowers ",
                   price="$40.00", course="wedding", florist=florist3)

session.add(bouquet1)
session.commit()


bouquet2 = Bouquet(user_id=1, name="Biedermeier Bouquet",
                   description="It is arranged in circular patteren",
                   price="$100.00", course="Engagement", florist=florist3)

session.add(bouquet2)
session.commit()

bouquet3 = Bouquet(user_id=1, name="The wrist corsage Bouquet",
                   description="A besutiful corsage worn on the wrist",
                   price="$35.50", course="anniversary", florist=florist3)

session.add(bouquet3)
session.commit()

bouquet4 = Bouquet(user_id=1, name="Carmen rose Bouquet",
                   description="It is designed by using roses",
                   price="$70.00", course="wedding", florist=florist3)

session.add(bouquet4)
session.commit()

# Designes of Flowers forver
florist4 = Florist(user_id=1, name="Flowers Forver")

session.add(florist4)
session.commit()

bouquet1 = Bouquet(user_id=1, name="Posy Bouquet",
                   description="These are small enough to be held in hands",
                   price="$220.00", course="wedding", florist=florist4)

session.add(bouquet1)
session.commit()


bouquet2 = Bouquet(user_id=1, name="composite Bouquet",
                   description="It composed of individual petals",
                   price="$200.00", course="Engagement", florist=florist4)

session.add(bouquet2)
session.commit()

bouquet3 = Bouquet(user_id=1, name="Presentation Bouquet",
                   description="It is a sheaf of flowers",
                   price="$45.50", course="anniversary", florist=florist4)

session.add(bouquet3)
session.commit()

bouquet4 = Bouquet(user_id=1, name="Bridal Bouquet",
                   description="It is designed specially for brides",
                   price="$250.00", course="wedding", florist=florist4)

session.add(bouquet4)
session.commit()


print ("added Bouquets!")
