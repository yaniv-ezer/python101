def tax(num):
    if num > 18 and num < 65:
        return True
    else:
        return False


result = tax(18.1)
name = "oren"
if result == True:
    print(name + " owes tax")
else:
    print(name + " dont owes tax")
