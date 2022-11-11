class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        rented_days = 0
        for username, book_details in self.rented_books.items():
            for b_name, days_to_rtrn in book_details.items():
                if b_name == book_name:
                    rented_days = days_to_rtrn
        return f"The book {book_name} is already rented and will be available in {rented_days} days!"

    def return_book(self, author, book_name, user):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]



