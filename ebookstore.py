#====Database Creation====
import sqlite3

#create a file called ebookstore with a SQLite3 DB
db = sqlite3.connect('ebookstore.db')

#get a cursor object
cursor = db.cursor()

#create the table
cursor.execute('''
    CREATE TABLE ebookstore(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
    ''')
db.commit()

#insert data into table
id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30
id2 = 3002
Title2 = "Harry Potter and the Philosopher's Stone"
Author2 = 'J.K. Rowling'
Qty2 = 40
id3 = 3003
Title3 = 'The Lion, the Witch and the Wardrobe'
Author3 = 'C.S. Lewis'
Qty3 = 25
id4 = 3004
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R. Tolkien'
Qty4 = 37
id5 = 3005
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

books = [(id1,Title1,Author1,Qty1),(id2,Title2,Author2,Qty2),(id3,Title3,Author3,Qty3),(id4,Title4,Author4,Qty4),(id5,Title5,Author5,Qty5)]

cursor.executemany(''' INSERT INTO ebookstore(id, Title, Author, Qty) VALUES(?,?,?,?)''',books)
print('data inserted')

db.commit()

#====Function Section====

#function to add a new book
def add_book(idx, Titlex, Authorx, Qtyx):
    id = idx
    Title = Titlex
    Author = Authorx
    Qty = Qtyx
    cursor.execute(''' INSERT INTO ebookstore(id, Title, Author, Qty) VALUES(?,?,?,?)''', (id,Title,Author,Qty))
    print('data inserted')
    db.commit()

#function to update an existing book
def update_title(idx, Titlex):
    id = idx
    Title = Titlex
    cursor.execute('''UPDATE ebookstore SET Title = ? WHERE id = ?''', (Title,id))
    db.commit()

def update_author(idx, Authorx):
    id = idx
    Author = Authorx
    cursor.execute('''UPDATE ebookstore SET Author = ? WHERE id = ?''', (Author,id))
    db.commit()

def update_qty(idx, Qtyx):
    id = idx
    Qty = Qtyx
    cursor.execute('''UPDATE ebookstore SET Qty = ? WHERE id = ?''', (Qty,id))
    db.commit()

#function to delete book
def delete_id(idx):
    id = idx
    cursor.execute('''DELETE FROM ebookstore WHERE id = ?''', (id,))
    db.commit()

def delete_title(Titlex, Authorx):
    Title = Titlex
    Author = Authorx
    cursor.execute('''DELETE FROM ebookstore WHERE Title = ? AND Author = ?''', (Title,Author,))
    db.commit()

#function to search for a book
def search_id(idx):
    id = idx
    cursor.execute('''SELECT id,Title,Author,Qty FROM ebookstore WHERE id = ?''', (id,))
    book = cursor.fetchone()
    print(book)
    db.commit()

def search_title(Titlex):
    Title = Titlex
    cursor.execute('''SELECT id,Title,Author,Qty FROM ebookstore WHERE Title =?''', (Title,))
    for row in cursor:
        print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))
    db.commit()

def search_author(Authorx):
    Author = Authorx
    cursor.execute('''SELECT id,Title,Author,Qty FROM ebookstore WHERE Author =?''', (Author,))
    for row in cursor:
        print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3]))
    db.commit()

#====Menu Section====

while True:
    # presenting the menu to the user
    print()
    menu = int(input('''Select one of the following Options below:
1 - Enter book
2 - Update book
3 - Delete book
4 - Search books
0 - Exit
: '''))

    if menu == 1:
        '''Add a new book to the database'''
        idx = int(input("Please enter the id for the book: "))
        Titlex = str(input("Please enter the title of the book: "))
        Authorx = str(input("Please enter the book's Author: "))
        Qtyx = int(input("Please enter the quantity of books: "))
        new_book = add_book(idx, Titlex, Authorx, Qtyx)
        
    elif menu == 2:
        '''Allow a user to update an existing book'''
        menu2 = input('''Select one of the following Options below:
        a - Update Title
        b - Update Author
        c - Update Qty
        e - Exit
:       ''')
        if menu2 == 'a':
            idx = int(input("Please enter the id of the book you want to update: "))
            Titlex = str(input("Please enter the new title of the book: "))
            update_book = update_title(idx, Titlex)
        elif menu2 == 'b':
            idx = int(input("Please enter the id of the book you want to update: "))
            Authorx = str(input("Please enter the new Author of the book: "))
            update_book = update_author(idx,Authorx)
        elif menu2 == 'c':
            idx = int(input("Please enter the id of the book you want to update: "))
            Qtyx = str(input("Please enter the new quantity for the book: "))
            update_book = update_qty(idx,Qtyx)
        elif menu2 == 'e':
            continue
        else:
            print("Oops,You have made a wrong choice, Please Try again")
        
    elif menu == 3:
        '''Delete a book from the database'''
        menu3 = input('''Select one of the following Options below:
        a - Delete book if you know id
        b - Delete book if you know Title and Author
        e - Exit
:       ''')
        if menu3 == 'a':
            idx = int(input("Please enter the id of the book you which to update: "))
            delete_book = delete_id(idx)
        elif menu3 == 'b':
            Titlex = str(input("Please enter the Title of the book you want to delete: "))
            Authorx = str(input("Please enter the Author of the book you want to delete: "))
            delete_book = delete_title(Titlex, Authorx)
        elif menu3 == 'e':
            continue
        else:
            print("You have made a wrong choice, Please Try again")
        
    elif menu == 4:
        '''Search for an existing book'''
        menu4 = input('''Select one of the following Options below:
        a - Search by id
        b - Search by title
        c - Search by Author
        e - Exit
:       ''')
        if menu4 == 'a':
            idx = int(input("Please enter the id of the book you want to find: "))
            search_book = search_id(idx)
        elif menu4 == 'b':
            Titlex = str(input("Please enter the Title of the book you want to find: "))
            search_book = search_title(Titlex)
        elif menu4 == 'c':
            Authorx = str(input("Please enter the Author of the book you want to find: "))
            search_book = search_author(Authorx)
        elif menu4 == 'e':
            continue
        else:
            print("You have made a wrong choice, Please Try again")
        
    elif menu == 0:
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

db.commit()
db.close()

#==========================