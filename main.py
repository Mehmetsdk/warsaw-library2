
from book import Book
from patron import Patron
from librarian import Librarian
from library import Library


book1 = Book("Dead Poets Society", "Nancy H. Kleinbaum", "3134567987")
book2 = Book("La Dame Aux Camelias", "Alexandre Dumas", "8554613479")
book3 = Book("White nights", " Fyodor Dostoevsky", "7897875641")


patron1 = Patron("Jack", "P001")
patron2 = Patron("Anna", "P002")

librarian = Librarian("Giorgina", "L001")


library = Library("Bibliothèque François-Mitterrand")


librarian.add_book(library, book1)
librarian.add_book(library, book2)
librarian.add_book(library, book3)


librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)


patron1.borrow_book(book1)
patron1.borrow_book(book2)


patron1.return_book(book1)


print("Books in the library:")
for book in library.list_books():
    print(book)

print("Patrons in the library:")
for patron in library.list_patrons():
    print(patron)
