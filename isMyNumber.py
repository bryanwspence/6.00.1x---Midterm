def isMyNumber(x):
    if x == secret_number:
        return 0
    if x > secret_number:
        return 1
    else:
        return -1


def jumpAndBackpedal(y):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 1
    foundNumber = False
    while not foundNumber:
        if isMyNumber(guess) == 0:
            break
        else:
            if isMyNumber(guess) == 1:
                guess -= 1
            if isMyNumber(guess) == -1:
                guess += 1
    return guess


secret_number = int(input("Enter your secret number: "))
print(jumpAndBackpedal(secret_number))
