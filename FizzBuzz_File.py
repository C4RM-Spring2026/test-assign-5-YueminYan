import numpy as np

def FizzBuzz(start, finish):
  numvec=np.arange(start, finish+1)
  objvec = np.array(numvec,dtype = 'object')
  condition=[(numvec % 15 == 0), (numvec % 3 == 0), (numvec % 5 == 0)]
  choice=["fizzbuzz", "fizz", "buzz"]
  np.select(condition, choice, default=objvec)
