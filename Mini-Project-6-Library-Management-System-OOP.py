# print("-" * 50)
# print("Welcome To Library Management System")
# print("-" * 50)
#
# class
#
# def userRegistration():
#     userName = input("Enter your User-Name (length must be greterThan 6 and lessThan 15) : ")
#     userPassword = input("Enter your password (length must be greterThan 6 and lessThan 15) : ")
#     if (len(userName) > 6 and len(userPassword) > 6) and (len(userName) < 16 and len(userPassword) < 16):
#         with open("UserData.txt", "a") as file:
#             file.write(userName + ":" + userPassword + "\n")
#             print("Your registration was successful")
#     else:
#         print("Your registration was not successful")
#
# def userLogin():
#     userName = input("Enter your User-Name : ")
#     userPassword = input("Enter your password: ")
#     with open("UserData.txt", "r") as file:
#         userData = file.readlines()
#         for line in userData:
#             if userName in line and userPassword in line:
#                 print("Login Successful")
#                 return True
#         print("No User data found!")
#         return False
#
# def useLogOut():
#     print("Log Out Successfully")
#     return False
#
# is_Runnning = True
# while is_Runnning:
#     print("1. Register User")
#     print("2. Log In")
#     print("3. Search Book by Name OR Author")
#     print("4. Issue Book")
#     print("5. Return Book")
#     print("6. Logout")
#     print("7. Exit")
#     choice = input("Enter your choice: ")
#     isLoggedIn = False
#     if choice == "1":
#        userRegistration()
#     elif choice == "2":
#         isLoggedIn = userLogin()
#     elif choice == "3":
#         if isLoggedIn:
#             search = input("Enter Book Name or Author Name :")
#             searchBook(search)
#         else:
#             print("Login is Required !")
#             isLoggedIn = userLogin()
#     elif choice == "4":
#         if isLoggedIn:
#             issue = input("Enter Book Name : ")
#             issueBook(issue)
#         else:
#             print("Login is Required !")
#             isLoggedIn = userLogin()
#     elif choice == "5":
#         if isLoggedIn:
#             returnbook = input("Enter Book Name : ")
#             returnBook(returnbook)
#         else:
#             print("Login is Required !")
#             isLoggedIn = userLogin()
#     elif choice == "6":
#         if isLoggedIn:
#             isLoggedIn = userLogOut()
#         else :
#             print("Login is Required !")
#             isLoggedIn = userLogin()
#     elif choice == "7":
#         print("Thank You..")
#         is_Running = False
#     else:
#         print("Invalid Choice !")
#

print("-" * 50)
print("Welcome To Library Management System")
print("-" * 50)

# =========================
# BASE CLASS (INHERITANCE)
# =========================
class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display(self):
        print(f"User: {self.username}")

# =========================
# DERIVED CLASS (USER)
# =========================
class User(Person):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.issued_books = []

# =========================
# DERIVED CLASS (ADMIN)
# =========================
class Admin(Person):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_book(self, library):
        name = input("Enter book name: ")
        author = input("Enter author: ")
        library.books.append(Book(name, author))
        print("✅ Book added successfully")

# =========================
# BOOK CLASS
# =========================
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.is_issued = False

# =========================
# LIBRARY CLASS
# =========================
class Library:
    def __init__(self):
        self.books = []
        self.current_user = None
        self.load_books()

    def load_books(self):
        self.books.append(Book("Python Basics", "Guido"))
        self.books.append(Book("AI Fundamentals", "Andrew Ng"))
        self.books.append(Book("Data Structures", "Mark Allen"))

    # -------------------------
    # REGISTER USER
    # -------------------------
    def register_user(self):
        username = input("Enter username (6-15 chars): ")
        password = input("Enter password (6-15 chars): ")

        if 6 < len(username) < 16 and 6 < len(password) < 16:
            with open("UserData.txt", "a") as file:
                file.write("U," + username + ":" + password + "\n")
            print("✅ User Registered")
        else:
            print("❌ Invalid input")

    # -------------------------
    # REGISTER ADMIN
    # -------------------------
    def register_admin(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        with open("UserData.txt", "a") as file:
            file.write("A," + username + ":" + password + "\n")

        print("✅ Admin Registered")

    # -------------------------
    # LOGIN
    # -------------------------
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            with open("UserData.txt", "r") as file:
                for line in file:
                    role_data, cred = line.strip().split(",")
                    user, pwd = cred.split(":")

                    if user == username and pwd == password:
                        if role_data == "U":
                            self.current_user = User(username, password)
                            print("✅ User Login Successful")
                        else:
                            self.current_user = Admin(username, password)
                            print("✅ Admin Login Successful")
                        return
        except FileNotFoundError:
            print("No users found")

        print("❌ Invalid credentials")

    # -------------------------
    # LOGOUT
    # -------------------------
    def logout(self):
        self.current_user = None
        print("✅ Logged out")

    # -------------------------
    # SEARCH BOOK
    # -------------------------
    def search_book(self):
        if not self.current_user:
            print("⚠ Login required")
            return

        keyword = input("Enter book or author: ").lower()

        for book in self.books:
            if keyword in book.name.lower() or keyword in book.author.lower():
                status = "Available" if not book.is_issued else "Issued"
                print(f"{book.name} by {book.author} → {status}")

    # -------------------------
    # ISSUE BOOK
    # -------------------------
    def issue_book(self):
        if not isinstance(self.current_user, User):
            print("⚠ Only users can issue books")
            return

        name = input("Enter book name: ").lower()

        for book in self.books:
            if book.name.lower() == name:
                if not book.is_issued:
                    book.is_issued = True
                    self.current_user.issued_books.append(book.name)
                    print("✅ Book issued")
                else:
                    print("❌ Already issued")
                return

        print("❌ Book not found")

    # -------------------------
    # RETURN BOOK
    # -------------------------
    def return_book(self):
        if not isinstance(self.current_user, User):
            print("⚠ Only users can return books")
            return

        name = input("Enter book name: ").lower()

        for book in self.books:
            if book.name.lower() == name:
                if book.is_issued:
                    book.is_issued = False
                    self.current_user.issued_books.remove(book.name)
                    print("✅ Book returned")
                else:
                    print("❌ Book was not issued")
                return

        print("❌ Book not found")

    # -------------------------
    # ADMIN FUNCTION
    # -------------------------
    def admin_add_book(self):
        if isinstance(self.current_user, Admin):
            self.current_user.add_book(self)
        else:
            print("⚠ Only admin can add books")

# =========================
# MAIN PROGRAM
# =========================
library = Library()

while True:
    print("\n1. Register User")
    print("2. Register Admin")
    print("3. Login")
    print("4. Search Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Add Book (Admin)")
    print("8. Logout")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.register_user()
    elif choice == "2":
        library.register_admin()
    elif choice == "3":
        library.login()
    elif choice == "4":
        library.search_book()
    elif choice == "5":
        library.issue_book()
    elif choice == "6":
        library.return_book()
    elif choice == "7":
        library.admin_add_book()
    elif choice == "8":
        library.logout()
    elif choice == "9":
        print("Thank you!")
        break
    else:
        print("Invalid choice")