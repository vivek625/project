def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("Please select the operation")
print("a:-> Addtion")
print("b:-> Subtract")
print("c:-> multiply")
print("d:-> divide")

choice = input("Please enter choice (a/ b/ c/ d):")

num_1 = int(input("Please enter the first number : "))
num_2 = int(input("Please enter the second number : "))

if choice == 'a':
    print(num_1 ,"+", num_2, "=", add(num_1,num_2))
elif choice == 'b':
    print(num_1 , "-" , num_2 , "=" , subtract(num_1,num_2))
elif choice == 'c':
    print(num_1 , "*" , num_2 , "=" , multiply(num_1,num_2))
elif choice == 'd':
    if num_2 > 0:
        print(num_1, "/" , num_2 , "=", divide(num_1,num_2))
    else:
        print("ZeroDivisionError: division by zero")
else:
    print("This is a Invalide input")
