def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
choice=input("Enter your choice (add, subtract, multiply, divide):")
if choice=="add":
    print("The sum is:",add(num1,num2))
elif choice=="subtract":
    print("The difference is:",subtract(num1,num2))
elif choice=="multiply":
    print("The product is:",multiply(num1,num2))
elif choice=="divide":
    print("The quotient is:",divide(num1,num2))
else:
    print("Invalid choice")