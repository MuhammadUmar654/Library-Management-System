    ##### Library Mangement System #####

    #     A simple program which keeps track of books in the library | show what's availble, what's borrowed, and letting the user add, borrow or return books. 
    #     In our version it will run in the console and store the collectin as a list of dictionaries in Python, where each book has tile author and availability status.
    #     The user will interact with it through a menu and choose options.

    ##### Features #####

    # View All Books (title, author, date published, category, status - (borrowed\published) )
    # Add a Book in the library 
    # Borrow a Book \ Return it 
    # Exit the sytem


    # classes and functions

class books:
    def __init__(self, title, author, date_published, book_type, status):
        self.title = title
        self.author = author
        self.date_published = date_published
        self.book_type = book_type
        self.status = status

    def display_details(self):
        print('Title:' + str(self.title))
        print('Author:' + str(self.author))
        print('Published Date:' + str(self.date_published))
        print('Type:' + str(self.book_type))
        print('Status:' + str(self.status))

    def available_books(self):
        return self.status == 'available'  
    
    def display_title(self):
        print('Title:' + str(self.title))

        


    # Library books data set of (70 items: 30 available, 40 borrowed)

library_books = [
    books("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", "available"),
    books("1984", "George Orwell", 1949, "Dystopian", "available"),
    books("Pride and Prejudice", "Jane Austen", 1813, "Romance", "available"),
    books("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", "available"),
    books("Moby Dick", "Herman Melville", 1851, "Adventure", "available"),
    books("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", "available"),
    books("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", "available"),
    books("Fahrenheit 451", "Ray Bradbury", 1953, "Dystopian", "available"),
    books("Jane Eyre", "Charlotte Brontë", 1847, "Classic", "available"),
    books("Brave New World", "Aldous Huxley", 1932, "Dystopian", "available"),
    books("Animal Farm", "George Orwell", 1945, "Satire", "available"),
    books("The Odyssey", "Homer", -800, "Epic", "available"),
    books("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy", "available"),
    books("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", "available"),
    books("Wuthering Heights", "Emily Brontë", 1847, "Gothic", "available"),
    books("The Alchemist", "Paulo Coelho", 1988, "Adventure", "available"),
    books("The Grapes of Wrath", "John Steinbeck", 1939, "Classic", "available"),
    books("Great Expectations", "Charles Dickens", 1861, "Classic", "available"),
    books("The Chronicles of Narnia", "C.S. Lewis", 1950, "Fantasy", "available"),
    books("Dracula", "Bram Stoker", 1897, "Horror", "available"),
    books("Frankenstein", "Mary Shelley", 1818, "Horror", "available"),
    books("A Tale of Two Cities", "Charles Dickens", 1859, "Historical", "available"),
    books("Don Quixote", "Miguel de Cervantes", 1605, "Classic", "available"),
    books("Les Misérables", "Victor Hugo", 1862, "Historical", "available"),
    books("War and Peace", "Leo Tolstoy", 1869, "Historical", "available"),
    books("The Picture of Dorian Gray", "Oscar Wilde", 1890, "Philosophical", "available"),
    books("Little Women", "Louisa May Alcott", 1868, "Classic", "available"),
    books("The Count of Monte Cristo", "Alexandre Dumas", 1844, "Adventure", "available"),
    books("The Brothers Karamazov", "Fyodor Dostoevsky", 1880, "Philosophical", "available"),
    books("The Old Man and the Sea", "Ernest Hemingway", 1952, "Fiction", "available"),
    books("The Da Vinci Code", "Dan Brown", 2003, "Thriller", "borrowed"),
    books("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Fantasy", "borrowed"),
    books("The Kite Runner", "Khaled Hosseini", 2003, "Drama", "borrowed"),
    books("Memoirs of a Geisha", "Arthur Golden", 1997, "Historical", "borrowed"),
    books("Life of Pi", "Yann Martel", 2001, "Adventure", "borrowed"),
    books("Gone Girl", "Gillian Flynn", 2012, "Thriller", "borrowed"),
    books("The Girl on the Train", "Paula Hawkins", 2015, "Thriller", "borrowed"),
    books("The Road", "Cormac McCarthy", 2006, "Post-apocalyptic", "borrowed"),
    books("The Shining", "Stephen King", 1977, "Horror", "borrowed"),
    books("Dune", "Frank Herbert", 1965, "Science Fiction", "borrowed"),
    books("Ender's Game", "Orson Scott Card", 1985, "Science Fiction", "borrowed"),
    books("A Game of Thrones", "George R.R. Martin", 1996, "Fantasy", "borrowed"),
    books("The Martian", "Andy Weir", 2011, "Science Fiction", "borrowed"),
    books("The Fault in Our Stars", "John Green", 2012, "Young Adult", "borrowed"),
    books("Twilight", "Stephenie Meyer", 2005, "Fantasy", "borrowed"),
    books("The Book Thief", "Markus Zusak", 2005, "Historical", "borrowed"),
    books("The Help", "Kathryn Stockett", 2009, "Drama", "borrowed"),
    books("The Hunger Games", "Suzanne Collins", 2008, "Dystopian", "borrowed"),
    books("Catching Fire", "Suzanne Collins", 2009, "Dystopian", "borrowed"),
    books("Mockingjay", "Suzanne Collins", 2010, "Dystopian", "borrowed"),
    books("The Maze Runner", "James Dashner", 2009, "Dystopian", "borrowed"),
    books("Divergent", "Veronica Roth", 2011, "Dystopian", "borrowed"),
    books("Insurgent", "Veronica Roth", 2012, "Dystopian", "borrowed"),
    books("Allegiant", "Veronica Roth", 2013, "Dystopian", "borrowed"),
    books("Ready Player One", "Ernest Cline", 2011, "Science Fiction", "borrowed"),
    books("The Giver", "Lois Lowry", 1993, "Dystopian", "borrowed"),
    books("The Outsiders", "S.E. Hinton", 1967, "Young Adult", "borrowed"),
    books("Percy Jackson & the Olympians", "Rick Riordan", 2005, "Fantasy", "borrowed"),
    books("The Lightning Thief", "Rick Riordan", 2005, "Fantasy", "borrowed"),
    books("The Sea of Monsters", "Rick Riordan", 2006, "Fantasy", "borrowed"),
    books("The Titan's Curse", "Rick Riordan", 2007, "Fantasy", "borrowed"),
    books("The Battle of the Labyrinth", "Rick Riordan", 2008, "Fantasy", "borrowed"),
    books("The Last Olympian", "Rick Riordan", 2009, "Fantasy", "borrowed"),
    books("City of Bones", "Cassandra Clare", 2007, "Fantasy", "borrowed"),
    books("City of Ashes", "Cassandra Clare", 2008, "Fantasy", "borrowed"),
    books("City of Glass", "Cassandra Clare", 2009, "Fantasy", "borrowed"),
    books("City of Fallen Angels", "Cassandra Clare", 2011, "Fantasy", "borrowed"),
    books("City of Lost Souls", "Cassandra Clare", 2012, "Fantasy", "borrowed"),
    books("City of Heavenly Fire", "Cassandra Clare", 2014, "Fantasy", "borrowed"),
    books("A Wrinkle in Time", "Madeleine L'Engle", 1962, "Science Fiction", "borrowed"),
    books("Charlotte's Web", "E.B. White", 1952, "Children's", "borrowed"),
    books("Matilda", "Roald Dahl", 1988, "Children's", "borrowed"),
    books("The Secret Garden", "Frances Hodgson Burnett", 1911, "Children's", "borrowed"),
    books("Anne of Green Gables", "L.M. Montgomery", 1908, "Classic", "borrowed"),
                ]

    # Main User Menu 

while True:
    print("\nWelcome to Umer's Library Mangement System:")
    print("\nWhat are you looking for today?")
    print("\n1)View All Books with Details \n2)Available Now \n3)Borrow a Book \n4)Return a Book")
    given_choice = int(input("\nPlease select form the above:"))

    # To View All the Books 
    if given_choice == 1:
        for book in library_books:    
            book.display_details()
            print("---")

    # To View books availble to borrow
    elif given_choice == 2:
        for book in library_books:
            if book.available_books():
                book.display_details()
                print("---")

    # To Borrow a Book
    elif given_choice == 3:
        book_found = False
        requested_book = str(input("Which Book you would like to borrow?:")).strip().lower()
        for book in library_books:
            if book.title.strip().lower() == requested_book and book.status == 'available':
                book_found = True
                print(f"You can collect {requested_book} at the reception!")
                print("Thanks for your visit! Enjoy!")
                book.status = 'borrowed'
                break
            elif book.title.strip().lower() == requested_book and book.status == "borrowed":
                print(f"{requested_book} is already borrowed.")
                book_found = True
                break

        if not book_found:
            print("Sorry! We don't have this book in our current collection.")

    # To Return a Book
    elif given_choice == 4:
        book_returned = False
        requested_book = str(input("Which Book you would like to return?:")).strip().lower()

        for book in library_books:
            if book.title.strip().lower() == requested_book and book.status == 'borrowed':
                print(f"Thank you! Hope you enjoyed reading {requested_book}")
                book.status = 'available'
                book_returned = True
                break

            elif book.title.strip().lower() == requested_book and book.status == 'available':
                print(f"{requested_book} is already availalbe in the library!")
                book_returned = True
                break

        if not book_returned:
            print("Thank you!")
            print("But this book doesn't belongs to our Library!")

            
    else:
        print("Please select from the above functions.")

    playback = str(input("\nDo you want to continue:(y/n)\n"))

    if playback.lower() != 'y':
        print("Thanks for your visit")
        break
        exit()






