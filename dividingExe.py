num = int(input())
# num = 12
result = None
if num % 2 == 0:
    result = 2
else:
    if num % 3 == 0:
        result = 3
    else:
        if num % 4 == 0:
            result = 4
        else:
            if num % 5 == 0:
                result = 5
            else:
                result = "prime"
if result == "prime":
    print("the number might be " + str(result))
if result != "prime":
    print(str(num) + " first divider is " + str(result))


# def tax(num):
#     if(num>18):
#         if (num<65):
#             return True
#         else:
#             return False
#     else:
#         return False
# name = 'oren'
# result=tax(18.1)
# if result == True:
#     print (name + ' owes tax')
# else:
#     print (name + ' dont owes tax')
