class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        if self.check_isbn(isbn):
            self.isbn = isbn
        else:
            raise ValueError("Invalid ISBN")

    @staticmethod
    def check_isbn(isbn):
        """checks if isbn is correct"""
        if "-" in isbn:
            isbn = isbn.replace("-", "")

        weight_for_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        isbn = [int(i) for i in isbn]

        if len(isbn) == 10:
            result = []
            for i in range(len(weight_for_10)):
                result.append(weight_for_10[i] * isbn[i])
            result2 = sum(result) % 10
            if result2 == isbn[-1]:
                return True
            else:
                return False

        elif len(isbn) == 13:
            even_numbers = []
            odd_numbers = []
            for i in range(0, len(isbn)):
                if i % 2 == 0:
                    even_numbers.append(isbn[i])
                else:
                    odd_numbers.append(isbn[i])
            result = (sum(even_numbers) + 3 * sum(odd_numbers[0:-1])) % 10
            if result == 0 == isbn[-1]:
                return True
            elif result != 0:
                if 10 - result == isbn[-1]:
                    return True
            else:
                return False

    def __str__(self):
        """defines how the output should be displayed"""
        return f'Title: {self.title} \nAuthor: {self.author} \nISBN: {self.isbn}'


book1 = Book("Some Title", "Some Author", "978-3-16-148410-0")
print(book1)