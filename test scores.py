#Endrit Ngjelina
#SPC ID#2436798
#COP1000
#prompt the user to enter the first test score
#prompt the user to enter the second test score
#prompt the user to enter the third test score
#print the average of the three scores

def main():
#Input section
#User inputs three test scores
    num1= int(input("Enter the score for test 1 "))
    num2 = int(input("Enter the score for test 2 "))
    num3 = int(input("Enter the score for test 3 "))
#Processing Section
#Add the three scores
#Divide the total by three to find average
    total = num1 + num2 + num3
    result = total / 3
#Outout Section
#Display the average score
    print(f'The average of these scores is {result:.2f}%.')
main()
