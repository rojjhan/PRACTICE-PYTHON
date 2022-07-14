#odd OR even

number = int(input("enter number:"))
if number % 2 == 0:
    print(f" {number} is even")
else:
    print(f" {number} is odd")

#-------------------------------------
#absolute velue


number2 = int(input("enter number:"))

if number2 < 0 :
    number2 = -number2
print(number2)


#--------------------------------------
#Take the coefficients of a quadratic equation and calculate its roots

a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

# delta = (b ^ 2) - 4 * a * c

delta = (b ** 2) - 4 * a * c

if delta < 0 :
    print("no roots")
elif delta == 0:
    root = -b / (2.0 * a)
    print("x1 = x2 = ")
    print(root)
else:
    root1 = (-b - delta ** 0.2) / (2.0 *a)
    root2 = (-b + delta ** 0.2) / (2.0 *a)
    print("x1 = ")
    print(root1)
    print("x2 = ")
    print(root2)
