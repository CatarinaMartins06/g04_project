# Class Movies
# Import the generic class
from classes.gclass import Gclass
from classes.studios import Studios

class Movies(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_title','_genre','_release_year', '_studios_id']
    # Class header title
    header = 'Movies'
    # field description for use in, for example, input form
    des = ['Id','Title','Genre','Release year', 'Studios id']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,title,genre,release_year,studios_id):
        super().__init__()
        
        studios_id =int(studios_id)
        if studios_id in Studios.lst:
            id = Movies.get_id(id)
            self._id = id
            self._title = title
            self._genre = genre
            self._release_year = release_year
            self._studios_id = studios_id
            Movies.obj[id] = self
            Movies.lst.append(id)
        else:
            print('Studio ', studios_id, ' not found')

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
    def name(self, name):
        self._name = name

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, novo_title):
        self._title = novo_title

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self, novo_genre):
        self._genre = novo_genre

    @property
    def release_year(self):
        return self._release_year
    
    @release_year.setter
    def release_year(self, novo_release_year):
        self._release_year = novo_release_year
    
    @property
    def studios_id(self):
        return self._studios_id
    
    @studios_id.setter
    def studios(self, novo_id):
        self._studios_id = novo_id
