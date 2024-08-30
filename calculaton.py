# python programing for simple calculator

from audioop import add


print         ("                                      Basic  Calculator                                          ")


select = int(input("select operation form1,2,3,4:"))

number_1 = int(input("enter first number:"))
number_2= int(input("enter the second no:"))

if select == 1:
    print(number_1, "+",number_2, "=",
          add(number_1, number_2))
    
elif select == 2:
    print(number_1, "-",number_2, "=",
          subtract(number_1, number_2))
    
elif select == 3:
    print(number_1, "*",number_2, "=",
          multiply(number_1, number_2))
    
elif select == 4:
    print(number_1, "/",number_2, "=",
          divide(number_1, number_2))
          
else:
    print("invalid input" )