def Exceptions():
    
    try:  
       x = 10 / 0
       print (x)
  
    except ZeroDivisionError:  
        print ("1.ArithmeticError Exception Raised.\n" )


    


    try:  
       import math
       print(math.exp(1000))

    except OverflowError:  
        print ("2.OverFlow Exception Raised.\n")

    try:
      my_list = [7,10,13]
      print(my_list[3])        

    except IndexError:
        print("3.IndexError Exception Raised.\n")


    


    try:
        print (float('shankar'))
    except ValueError:
        print ("4.ValueError Exception raised.\n")


    try:  
        a = 100
        b = "shankar"
        assert a == b
    except AssertionError:  
        print ("5.Assertion Exception Raised.\n")

Exceptions()

