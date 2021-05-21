def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string

word = input("Please enter a word to check:")
if is_palindrome(word.casefold()):
    print("'{}' is a palindrome.".format(word))
else:
    print("'{}' is not a palindrome.".format(word))