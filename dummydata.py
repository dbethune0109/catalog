from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import ItemType, Base, MenuItem

engine = create_engine('sqlite:///menuwithuser.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Menu for Just Desserts
type1 = ItemType(category="Appetizer")
type2 = ItemType(category="Entree")
type3 = ItemType(category="Dessert")
type4 = ItemType(category="Beverage")
session.add(type1)
session.add(type2)
session.add(type3)
session.add(type4)

item1 = MenuItem(
                name="Steak and Potatoes",
                description="Beef wiht Potato.",
                price="8.99", category="Entree")

item2 = MenuItem(
                name="Soda",
                description="Pepsi, serving size: 1 glass.",
                price="2.99", category="Beverage")

item3 = MenuItem(
                name="Deep fried Ice Cream",
                description=(
                    "Ice Cream deep fried in peanut oil," +
                    "serving size: 1 glass."),
                price="4.99", category="Appetizer")

item4 = MenuItem(
                name="Black Tea Ice Cream",
                description="Black tea flavor ice cream.",
                price="2.99", category="Dessert")

session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.commit()

print "added menu items!"
