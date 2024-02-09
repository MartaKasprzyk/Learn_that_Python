def check_palindrome():
    text = input("Enter your text: ")
    text = text.lower().replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False


print(check_palindrome())
