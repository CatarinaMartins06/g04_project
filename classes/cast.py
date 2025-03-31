"""
@author: António Brito / Carlos Bragança (2025)
#objective: class OrderProduct
"""""
# Class Cast
from movies import Movies
from actors import Actors
# Import the generic class
from gclass import Gclass

class Cast(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_movies_id','_actors_id']
    header = 'Cast'
    des = ['Id','Movies_id','Actors_id']
    def __init__(self, id, movies_id, actors_id, role):
        super().__init__()
        movies_id = int(movies_id)
        actors_id = int(actors_id)
        if movies_id in Movies.lst:
            if actors_id in Actors.lst:
                id = Cast.get_id(id)
                self._id = id
                self._movies_id = movies_id
                self._actors_id = actors_id
                self._role = role
                Cast.obj[id] = self
                Cast.lst.append(id)
            else:
                print('Actor ', actors_id, ' not found')
        else:
            print('Movie ', movies_id, ' not found')

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def movies_id(self):
        return self._movies_id
    
    @movies_id.setter
    def movies_id(self, novo_id):
        self._movies_id = novo_id
    
    @property
    def actors_id(self):
        return self._actors_id
    
    @actors_id.setter
    def actors_id(self, novo_id):
        self._actors_id = novo_id

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, novo_role):
        self._role = novo_role



        