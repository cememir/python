from random import randint
from time import time
from cemir_print.ccprint import ccprint
from cemir_error.ccerror import error_tracking

while True:
    num1 = randint(2, 9)
    num2 = randint(2, 9)
    product = num1 * num2
    start_time = time()
    response = input(f'What is {num1} * {num2}? ')
    if not response:
        break
    elapsed_time = time() - start_time
    try:
        int_response = int(response)
        if int_response == product:
            ccprint(f'Correct in {elapsed_time:.2f} sn. {num1} {num2}')
        else:
            ccprint('Incorrect')
    except Exception as e:
        import sys
        error_tracking(e, sys, "en")
