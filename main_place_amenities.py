#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models.__init__ import storage
from models.user import User
from models.place import Place, place_amenity
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


# creation of a State

state = State(name="California")
state.save()
# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

print(state.cities)





storage.save()
print("OK")

