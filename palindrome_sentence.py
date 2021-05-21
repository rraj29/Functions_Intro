def is_palindrome(string):
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


def is_palindrome_sentence(sentence: str) -> bool:
    made_sentence = ""
    for letter in given_sentence:
        if letter.isalnum():
            made_sentence += letter
    print(made_sentence)
    #return made_sentence[::-1].casefold() == made_sentence.casefold()
    return(is_palindrome(made_sentence))    #we can call other functions from a function.
    # both the return lines are doing the same output finally.



given_sentence = input("Please enter a sentence: ")
if is_palindrome_sentence(given_sentence):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
