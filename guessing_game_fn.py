#This is just a better version of the guessinggame code.
import random


def get_integer(prompt):
    """
    Get an integer as a standard input (stdin).

    it keeps looping, and prompting the user
     until a valid `int` is given as input.
    :param prompt: The string that user will see, when
        they are prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)    # ****press "CTRL+Q" after selecting INPUT
                                # to see the documentation of Input function
        #OR     * Hold "CTRL" and then click on "Input" to see the documentation
        #      same can be done for any "BUILT-IN FUNCTION"
        if temp.isnumeric():
            return int(temp)
        else:
            print("'{}' is not a valid input.".format(temp))


lowest = 1
highest = 1000
answer = random.randint(lowest,highest)
print(answer)  # TODO: Delete after testing

print("Please input a number between {0} to {1}: ".format(lowest,highest))
guess=0     #we can put it to be any number that is not the answer.
cnt=0
while guess != answer:
    guess= get_integer(": ")
    cnt +=1
    if cnt >= 10:
        print("Sorry bro, bad luck")
        break
    if guess==0:
        break
    elif guess == answer:
        print("Yayy you got it right in {} times!".format(cnt))
        break
    elif guess > answer:
        print("Please guess lower: ")
    else:
        print("Please guess higher: ")

