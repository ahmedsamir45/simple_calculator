def fact(n):
    if n == 0:
        return 1
    result = n*fact(n-1)
    return result

#def power(base_num, pow_num):
 #   result = 1
    
  #  for index in range(pow_num):
        
   #     result = result*base_num

        
    #return result

print('This program calculate (+,*,/,%,!,-,^)')

again = 'y'

while again == 'y':

    while True:

        
        try:
            num1 = float(input('please enter the first number : '))
            break
        except ValueError :
            print('invalid input , please enter a numeric value')


    while True:
        try:
            operator = input('please enter the operator : ')
            if operator in ['+' ,'*','/','%','!','-','^']:
                break
            else:
                raise ValueError


        except ValueError:
             print('invalid input , please enter (+,*,/,%,!,-,^)  ')
            



    
    if operator == '!':
        print('the factorial is: ',fact(num1))
    else:
        while True :
            try:
                num2 = float(input('please enter the second number : '))
                if operator == '/' and num2 ==0:
                    raise ZeroDivisionError
                break
            except ValueError:
                print('invalid input , please enter a numeric value')
            except ZeroDivisionError:
                print('invalid input , please enter any numeric value except zero ')



    if operator == '+':
       
        result = num1 + num2
        
    elif operator == '*':
       
        result = num1 * num2
        
    elif operator == '/':
        
        result = num1 / num2
        
    elif operator == '-':
        
        result = num1 - num2
        
    elif operator == '%':
        
        result = num1 % num2
        
  #  elif operator =='^':
   #     num2 = int(input('please enter the second number : '))
        
    #    print('the exponent is: ',power(num1,num2))
        
    elif operator =='^':
               
        result = num1**num2

        
    else:
        print('enter a true operator')


    if result != None :
        print(' the result is ',result)

    else:
        print('error')
        
    again=input('do you want to calculate another operation (enter y for yes): ')
