Prompt = "\n Please enter your age: "
Prompt += "\n (We have different ticket for different Ages. We need more info to better suite you.) "

active = True
while active:
    Age = int(input(Prompt))
    if Age == 1000:
        break

    if  Age < 3:
        print('Your ticket is Free!')
    elif Age <= 12:
        print('Your ticket is $10')  
        break 
    else:
        print('Your ticket is $15')
        

        
        
