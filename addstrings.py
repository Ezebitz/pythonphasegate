def add_strings(num1, num2):
  

    num1 = ()
    num2 = ()
    if not isinstance(num1, str) or not isinstance(num2, str):
       raise TypeError("Both inputs must be strings")


    result = str (int(num1) + int(num2))
    return result 
print (add_strings(22,24))
