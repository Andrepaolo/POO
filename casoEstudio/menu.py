import sys
from notebook import Notebook

class Menu:
    """Mostrará un menu y podrá escoger una opción"""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.del_note,
            "6": self.quit,
        }

    def display_menu(self):
        print(
            """
            Menu Notebook
            1. Mostrar todas las notas
            2. Buscar una nota
            3. Agregar una nota
            4. Modificar una nota
            5. Borrar una nota
            6. Salir
            """
        )

    def run(self):
        """Muestra el menu para escoger una opcion"""
        while True:
            self.display_menu()
            choice = input("Entre una opción: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(" {0} no es una opcion valida".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1} \n {2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter=input("buscar")
        notes =self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Ingrese la nota: ")
        self.notebook.new_note(memo)
        print("La nota ha sido agregada.")

    def modify_note(self):
        id = input ("Enter a note id")
        memo = input("Enter a memo: ")
        tags =input("Enter tags")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_memo(id, tags)
    def del_note(self):
        id_note =input("Ingrese el id de la nota a borrar: ")
        self.notebook.del_note(int(id_note)-1)

    def quit(self):
        print("Gracias por usar tu notebook el dia hoy")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()


