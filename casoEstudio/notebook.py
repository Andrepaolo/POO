import datetime

last_id = 0

class Note:
    """ Representa una nota en el cuaderno. busca coincidencias con una cadena
    en las búsquedas y almacena etiquetas para cada nota"""

    def __init__(self, memo, tags=""):
        """Inicializa una nota con un memo y etiquetas (opcional) separadas por
        espacio. se debe establecer automáticamente la fecha de creación de la 
        nota asimismo debe tener una identificación unica (id)."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determina si una nota coincide con el texto del filtro.
        devuelve True si coincide, False en caso contrario."""
        return filter in self.memo or filter in self.tags


class Notebook:
    """Representa una colección de notas que se pueden etiquetar,
    modificar, buscar - eliminar. """

    def __init__(self):
        """ Inicializa un cuaderno (Notebook) con una lista vacia."""
        self.notes = []

    def new_note(self, memo, tags=""):
        """ Crea una nueva nota y lo agrega a la lista (array) """
        #n1 = Note("el gato feliz", "gato feliz")
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Buscar la nota con el id y cambiar el contenido"""
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        """ Busca la nota para hacer el cambio en las etiquetas """
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break


    def search(self, filter):
        """busca todas las notas que coincide (match) con el filtro """
        return [ note for note in self.notes if note.match(filter) ]


    def del_note(self, note_id):
        self.notes.pop(note_id)
        print ("nota eliminada")