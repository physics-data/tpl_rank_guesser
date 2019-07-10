# TODO: read one int from standard input
# HINT: use input()
rank = int(input())

# infinite loop
while True:
    # TODO: print guessing message
    # HINT: use print()
    print('Guess?')

    # TODO: read one int from standard input
    # HINT: use input()
    guess = int(input())

    # TODO: how to compare guess and rank?
    if guess > rank:
        # TODO: print correct message
        # HINT: use print()
        print('Too big')
    elif guess < rank:
        # TODO: print too big message
        # HINT: use print()
        print('Too small')
    elif guess == rank:
        # TODO: print too small message
        # HINT: use print()
        print('Correct')
        break
