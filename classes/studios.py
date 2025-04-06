# Class Studios
# Import the generic class
from gclass import Gclass

class Studios(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_name','_location']
    header = 'Studios'
    des = ['Id','Name','Location']

    def __init__(self, id, name, location):
        super().__init__()
        self._name = name
        self._location = location

        Studios.obj[id] = self
        Studios.lst.append(id)

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
    def location(self):
        return self.location
    
    @location.setter
    def location(self, novo_location):
        self._id = novo_location
