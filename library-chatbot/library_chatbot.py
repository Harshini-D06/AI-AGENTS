# College Library Chatbot

books = [
    {
        "id": "B001",
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "subject": "Computer Science",
        "status": "Available"
    },
    {
        "id": "B002",
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "subject": "Python",
        "status": "Available"
    },
    {
        "id": "B003",
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "subject": "Programming",
        "status": "Issued"
    },
    {
        "id": "B004",
        "title": "Database System Concepts",
        "author": "Abraham Silberschatz",
        "subject": "Database",
        "status": "Available"
    },
    {
        "id": "B005",
        "title": "Computer Networks",
        "author": "Andrew S. Tanenbaum",
        "subject": "Networking",
        "status": "Available"
    },
    {
        "id": "B006",
        "title": "Operating System Concepts",
        "author": "Abraham Silberschatz",
        "subject": "Operating Systems",
        "status": "Issued"
    },
    {
        "id": "B007",
        "title": "Artificial Intelligence",
        "author": "Stuart Russell",
        "subject": "AI",
        "status": "Available"
    },
    {
        "id": "B008",
        "title": "Data Structures and Algorithms",
        "author": "Mark Allen Weiss",
        "subject": "Data Structures",
        "status": "Available"
    },
    {
        "id": "B009",
        "title": "Software Engineering",
        "author": "Ian Sommerville",
        "subject": "Software Engineering",
        "status": "Issued"
    },
    {
        "id": "B010",
        "title": "Machine Learning",
        "author": "Tom M. Mitchell",
        "subject": "Machine Learning",
        "status": "Available"
    }
]


# --------------------------------------------------
# SHOW ALL BOOKS
# --------------------------------------------------

def show_all_books():

    print("\n========== ALL LIBRARY BOOKS ==========")

    for book in books:
        print("----------------------------------------------")
        print("Book ID   :", book["id"])
        print("Title     :", book["title"])
        print("Author    :", book["author"])
        print("Subject   :", book["subject"])
        print("Status    :", book["status"])


# --------------------------------------------------
# SEARCH FOR A PARTICULAR BOOK
# --------------------------------------------------

def search_book():

    print("\n========== SEARCH FOR A BOOK ==========")

    book_name = input(
        "Enter the book name you want to search: "
    ).strip()

    found = False

    for book in books:

        if book_name.lower() in book["title"].lower():

            found = True

            print("\n📚 BOOK FOUND")
            print("----------------------------------------------")
            print("Book ID   :", book["id"])
            print("Title     :", book["title"])
            print("Author    :", book["author"])
            print("Subject   :", book["subject"])
            print("Status    :", book["status"])

            if book["status"] == "Available":
                print("Result    : ✅ Book is available.")
            else:
                print("Result    : ❌ Book is currently issued.")

    if not found:
        print("\n❌ Sorry, this book was not found.")


# --------------------------------------------------
# SEARCH BY AUTHOR
# --------------------------------------------------

def search_by_author():

    print("\n========== AUTHORS IN THE LIBRARY ==========")

    authors = []

    for book in books:
        if book["author"] not in authors:
            authors.append(book["author"])

    print("\nAuthors available in the library:")

    for i, author in enumerate(authors, 1):

        print(f"\n{i}. {author}")

        print("   Books:")

        for book in books:
            if book["author"] == author:
                status = "Available" if book["status"] == "Available" else "Issued"

                print(
                    f"   - {book['title']} ({status})"
                )

    print("\n----------------------------------------------")

    author_name = input(
        "\nEnter the author name you want to search: "
    ).strip()

    found = False

    print("\n========== SEARCH RESULT ==========")

    for book in books:

        if author_name.lower() in book["author"].lower():

            found = True

            print("----------------------------------------------")
            print("Book ID :", book["id"])
            print("Book    :", book["title"])
            print("Author  :", book["author"])
            print("Subject :", book["subject"])
            print("Status  :", book["status"])

    if not found:

        print("\n❌ No books found for this author.")


# --------------------------------------------------
# SEARCH BY SUBJECT
# --------------------------------------------------

def search_by_subject():

    print("\n========== SUBJECTS IN THE LIBRARY ==========")

    subjects = []

    for book in books:
        if book["subject"] not in subjects:
            subjects.append(book["subject"])

    print("\nSubjects available in the library:")

    for i, subject in enumerate(subjects, 1):

        print(f"\n{i}. {subject}")

        print("   Books:")

        for book in books:

            if book["subject"] == subject:

                status = (
                    "Available"
                    if book["status"] == "Available"
                    else "Issued"
                )

                print(
                    f"   - {book['title']} "
                    f"by {book['author']} ({status})"
                )

    print("\n----------------------------------------------")

    subject_name = input(
        "\nEnter the subject you want to search: "
    ).strip()

    found = False

    print("\n========== SEARCH RESULT ==========")

    for book in books:

        if subject_name.lower() in book["subject"].lower():

            found = True

            print("----------------------------------------------")
            print("Book ID :", book["id"])
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            print("Subject :", book["subject"])
            print("Status  :", book["status"])

    if not found:

        print("\n❌ No books found for this subject.")


# --------------------------------------------------
# CHECK AVAILABILITY
# --------------------------------------------------

def check_availability():

    print("\n========== CHECK BOOK AVAILABILITY ==========")

    book_name = input(
        "Enter the book name: "
    ).strip()

    found = False

    for book in books:

        if book_name.lower() in book["title"].lower():

            found = True

            print("\n📖", book["title"])
            print("----------------------------------------------")
            print("Author :", book["author"])
            print("Status :", book["status"])

            if book["status"] == "Available":

                print("✅ This book is available.")

            else:

                print("❌ This book is currently issued.")

    if not found:

        print("\n❌ Book not found.")


# --------------------------------------------------
# HELP
# --------------------------------------------------

def show_help():

    print("\n========== HELP ==========")

    print("""
1. Show all books
   → Displays all 10 books in the library.

2. Search for a book
   → Enter the name of a particular book.

3. Search by author
   → Shows all authors and the books written by them.
   → Then asks which author you want to search.

4. Search by subject
   → Shows all subjects and the books under each subject.
   → Then asks which subject you want to search.

5. Check book availability
   → Checks whether a particular book is available.

6. Help
   → Shows chatbot instructions.

7. Exit
   → Closes the chatbot.
""")


# --------------------------------------------------
# MAIN CHATBOT
# --------------------------------------------------

def chatbot():

    print("\n==============================================")
    print("        🎓 COLLEGE LIBRARY CHATBOT")
    print("==============================================")

    print("\nHello! Welcome to the College Library.")
    print("How can I help you today?")

    while True:

        print("\n============== MENU ==============")

        print("1. Show all books")
        print("2. Search for a book")
        print("3. Search by author")
        print("4. Search by subject")
        print("5. Check book availability")
        print("6. Help")
        print("7. Exit")

        print("==================================")

        choice = input(
            "Enter your choice (1-7): "
        ).strip()

        if choice == "1":

            show_all_books()

        elif choice == "2":

            search_book()

        elif choice == "3":

            search_by_author()

        elif choice == "4":

            search_by_subject()

        elif choice == "5":

            check_availability()

        elif choice == "6":

            show_help()

        elif choice == "7":

            print("\nThank you for using the College Library Chatbot! 📚")
            break

        else:

            print("\n❌ Invalid choice.")
            print("Please enter a number from 1 to 7.")


# --------------------------------------------------
# START PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    chatbot()