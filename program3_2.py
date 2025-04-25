#Endrit Ngjelina
#SPC ID#2436798
#COP1000
#Worked alone
#This program prompts user to enter odd multiple of 19 greater than 60 and less than 200
#If input is incorrect, it displays 'Bad Input'
#If input is correct, it displays 'Good Input' and the factor

#Input section
#User inputs number
number = int(input('Enter an odd multiple of 19 between 60 and 200: '))

#Processing section
#If statement calculates if input is correct 
if number > 60 and number < 200 and number % 2 != 0 and number % 19 == 0:
    
#Output section
#Display 'Good Input' if number is correct
#Display factor, if number is correct
    print('Good Input.')
    print(f'The factor is {number/19}.')
    
#Display 'Bad Input' if number is incorrect
else:
    print('Bad Input.')


