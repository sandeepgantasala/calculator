#importing tkinter 
#import tkinter
#top = tkinter.Tk()
#top.mainloop()
print("Welcome to the Simple calculator\n")
FirstNumber = int(input("Enter the First Number:\n"))
SecondNumber = int(input("Enter the Second Number:\n"))
print(" Press 1 for Addition\n Press 2 for Multiplication\n Press 3 for Division\n Press 4 for Substraction\n Press 5 for Modulus\n Press 6 for Exponentiation\n Press 7 for Floor Division ")
print("Please Press the Option for calculating the Two Numbers\n")

option = int(input("Please Enter the Option:\n"))

if option == 1 :
    print("The Output is: ",FirstNumber + SecondNumber)
elif option == 2:
    print("The Output is: ",FirstNumber * SecondNumber)
elif option ==3:
    print("The Output is: ",FirstNumber / SecondNumber)
elif option == 4 :
    print("The Output is: ",FirstNumber - SecondNumber)
elif option == 5:
    print("The Output is: ",FirstNumber | SecondNumber)
elif option == 6:
    print("The Output is: ",FirstNumber ** SecondNumber)
elif option == 7:
    print("The Output is: ",FirstNumber // SecondNumber)
else:
    print("Invalid Option")

