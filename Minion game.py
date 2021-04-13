def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    str_length=len(string)
    kevin,stuart=0,0
    for i in range(str_length):
        if s[i] in vowels:
            kevin+=(str_length-i)
        else:
            stuart+=(str_length-i)
    if kevin>stuart:
        print("Kevin",kevin)
    elif kevin<stuart:
        print("Stuart",stuart)
    else:
        print("Draw")

