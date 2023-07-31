#!/usr/bin/python3
<<<<<<< HEAD
""" Index view for the API."""
=======
""" Index page"""
from api.v1.views import app_views
>>>>>>> 832d4c6724033a03560a8aadf62561d0295f84ab
from flask import jsonify
from models import storage

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

<<<<<<< HEAD

@app_views.route('/status')
def get_status():
    """Gets status of the API.
    """
    return jsonify(status='OK')


@app_views.route('/stats')
def get_stats():
    """Gets number of objects for each type.
    """
    objects = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
=======
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns JSON """
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Returns the number of each instance type """
    return jsonify(amenities=storage.count("Amenity"),
                   cities=storage.count("City"),
                   places=storage.count("Place"),
                   reviews=storage.count("Review"),
                   states=storage.count("State"),
                   users=storage.count("User"))
>>>>>>> 832d4c6724033a03560a8aadf62561d0295f84ab
