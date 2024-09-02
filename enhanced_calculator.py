#CIS 103: Introduction to Programming
#Lab 02: "Calculator Function"
#Instructor: Md Ali
#Date: 08/31/2024
#Student: Pierina Brito

#Python Operators
#In Python programming, Operators in general are used to perform operations on values and variables.
#These are standard symbols used for logical and arithmetic operations.
#OPERATORS: These are the special symbols. Eg- + , * , /, **, % .
#OPERAND: It is the value on which the operator is applied.

#Arithmetic Operators in Python
#Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction,
# multiplication, and division.

#Precedence of Arithmetic Operators in Python
#The precedence of Arithmetic Operators in Python is as follows:

#1.E – Exponentiation(**)
#2.M – Multiplication(‘*’) (Multiplication and division have the same precedence)
#3.D – Division
#4.A – Addition(‘+’) (Addition and subtraction have the same precedence)
#5.S – Subtraction(‘-‘)
#6.The modulus of Python operators (‘%’) helps us extract the last digit/s of a number. For example:


def main():
    while True:

        print("|*|+/**\-|% CALCULATOR %|-/**\+|*| ")
        choice = input("Choose an operator or exit (+ - * / ** % exit ): ")

        #exit/ break code
        if choice == "exit":
            print("Thank you, have a nice day! ")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        #code for add
        if choice == "+":
            result = num1 + num2
            print("The sum is {}".format(result))

        #code for subtract
        elif choice == "-":
            result = num1 - num2
            print("The difference is {}".format(result))

        #code for multiply
        elif choice == "*":
            result = num1 * num2
            print("The product is {}".format(result))

        #code for division
        elif choice == "/":
            result = num1 / num2
            print("The result is {}".format(result))

        # code for exponentiation
        elif choice == "**":
            result = num1 ** num2
            print("The exponent is {}".format(result))

        # code for modulus
        elif choice == "%":
            result = num1 % num2
            print("The modulus is {}".format(result))

        else:
            print(f"{choice} is not a valid operator, try again")

if __name__ == "__main__":
    main()

