'''To handle eception we use three terms in python - try, except finally
'''
try: #this is used as first logical code

    user_intput1= input("Please enter number1  ")
    user_input2= input("Please enter number2 ")

    Output = int(user_intput1) + int(user_input2)

    print (Output)

except: # this is used while entring condition when exception is expected

    print ("this is not valid input")


finally: #this is optional and can be used when you want to perform either step after try or except

    print ("Your code executed")
