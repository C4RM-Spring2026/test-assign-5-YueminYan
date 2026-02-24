import numpy as np

def FizzBuzz(start, finish):
    numvec=np.arange(start, finish+1)
    condition=[(numvec % 15 == 0), (numvec % 3 == 0), (numvec % 5 == 0)]
    choice=['FizzBuzz', 'Fizz', 'Buzz']
    return np.select(condition, choice, default=numvec.astype(str))
