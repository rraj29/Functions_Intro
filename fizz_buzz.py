import random as rand

def fizz():
    """
    it gives a random `int` n
    we have to give `n+1` or 100. else we lose
    this game will continue till either we lose, we type `100` when we win.
    :return:
    """
    b = rand.randint(1,100)
    print(b)
    a = int(input())
    if a == b+1 and a!=100:
        fizz()
    elif a!=b+1 and a!=100:
        print("fuck off")
    else:
        print("good luck")
fizz()
