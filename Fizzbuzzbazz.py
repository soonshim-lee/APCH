# for x in range(1,101):
#     remainder_3 = x % 3
#     remainder_5 = x % 5
#     if remainder_3 == 0 and remainder_5 == 0:
#         print("Fizzbuzz")
#     elif remainder_3 == 0:
#         print("Fizz")
#     elif remainder_5 == 0:
#         print("Buzz")
#     else:
#         print(x)

# def fizz(y):
#     remainder = y % 3
#     if remainder == 0:
#         factor = True
#     else:
#         factor = False
#     return factor

# def buzz(y):
#     remainder = y % 5
#     if remainder == 0:
#         factor = True
#     else:
#         factor = False
#     return factor

# def bazz(y):
#     remainder = y % 7
#     if remainder == 0:
#         factor = True
#     else:
#         factor = False
#     return factor

# for x in range(1,101):
#     fizz1 = fizz(x)
#     buzz1 = buzz(x)
#     bazz1 = bazz(x)
#     if fizz1 == True and buzz1 == True and bazz1 == True:
#         print("FizzBuzzBazz")
#     elif fizz1 == True and buzz1 == True:
#         print("FizzBuzz")
#     elif fizz1 == True and bazz1 == True:
#         print("FizzBazz")
#     elif buzz1 == True and bazz1 == True:
#         print("BuzzBazz")
#     elif fizz1 == True:
#         print("Fizz")
#     elif buzz1 == True:
#         print("Buzz")
#     elif bazz1 == True:
#         print("Bazz")
#     else: 
#         print(x)

def fizz(y):
    remainder = y % 3
    if remainder == 0:
        factor = True
    else:
        factor = False
    return factor

def buzz(y):
    remainder = y % 5
    if remainder == 0:
        factor = True
    else:
        factor = False
    return factor

def bazz(y):
    return  y % 7 == 0

for x in range(1,101):
    line = ""
    fizz1 = fizz(x)
    buzz1 = buzz(x)
    bazz1 = bazz(x)
    if fizz1 == True:
        line+= "fizz"
    if buzz1 == True:
        line+= "buzz"
    if bazz1 == True:
        line+= "bazz"
    if line == "":
        print(x)
    else:
        print(line)
