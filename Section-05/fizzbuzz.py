for i in range(1,101):
  if i %3 == 0 and not i %5 ==0:
    print("Fizz number: ", i)
  elif i %5 ==0 and not i %3 ==0:
    print("Buzz number: ", i)
  elif (i %3 == 0 and i %5 ==0 ):
    print("FuzzBuzz number: ", i)
  else:    
    print(i)
