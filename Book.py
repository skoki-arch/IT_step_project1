
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.year})"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        
        self.books.append(book)
        print(f"დაემატა წიგნი: {book}")

    def show_all_books(self):
        if not self.books:
            print("სია ცარიელია.")
            return

        print("ყველა წიგნი:")
        for book in self.books:
            print(book)

    def search_by_title(self, title):
 
        found = [book for book in self.books if book.title.count(title)]

        if found:
            print("ნაპოვნი წიგნები:")
            for b in found:
                print(b)
        else:
            print("ასეთი სათაურის წიგნი არ არსებობს.")


manager = BookManager()

# წიგნების დამატება
manager.add_book(Book("დათა თუთაშხია", "ჭაბუა ამირეჯიბი", 1971))
manager.add_book(Book("ვეფხის ტყაოსანი", "შოთა რუსთაველი", 1901))

# ყველა წიგნის ჩვენება
#manager.show_all_books()

# ძებნა
manager.search_by_title("ოსანი")