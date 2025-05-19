# Class Actors
# Import the generic class
from classes.gclass import Gclass

class Actors(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_name','_birthdate','_nationality']
    # Class header name
    header = 'Actors'
    # field description for use in, for example, input form
    des = ['Id','Name','Birthdate','Nationality']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,name,birthdate,nationality):
        super().__init__()
        # Object attributes
        id = Actors.get_id(id)
        self._id = id
        self._name = name
        self._birthdate = birthdate
        self._nationality = nationality
        # Add the new object to the Customer's list
        Actors.obj[id] = self
        Actors.lst.append(id)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, novo_name):
        self._name = novo_name

    @property
    def birthdate(self):
        return self._birthdate
    
    @birthdate.setter
    def birthdate(self, novo_birthdate):
        self._birthdate = novo_birthdate

    @property
    def nationality(self):
        return self._nationality
    
    @nationality.setter
    def nationality(self, novo_nationality):
        self._nationality = novo_nationality

    