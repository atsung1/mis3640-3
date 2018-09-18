def diff21(n):
  if n < 21:
    return(abs(n - 21))
  elif n > 21:
    return(2 * abs(n - 21))
  else:
    return(0)
  
print(diff21(21))
print(diff21(-100))
print(diff21(100))