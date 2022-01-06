"""share_names = ["Frog", "google", "apple", "paypal", "nvidia", "serviceNow"]
share_prices = [3000, 2700, 30, 500, 700, 1000]
i = 0
x = len(share_prices) - 1
while i < len(share_names):
    print("the price of share " + share_names[i] + " is " + str(share_prices[i + x]))
    i = i + 1
    x = x - 2

print("==================")


for x in range(len(share_names)):
    print(share_names[x])
    
    
print("==================")"""

# car_number = "123452112313225567655665656755645645645645646456454564564675567687154321"
# is_palindrom = True
# i = 0
# # x = len(car_number) - 1
# while i < len(car_number) / 2 and is_palindrom == True:
#     if car_number[i] == car_number[len(car_number) - 1 - i]:
#         is_palindrom = True
#     else:
#         is_palindrom = False
#     i = i + 1
#     # x = x - 1
# if is_palindrom == True:
#     print("the input is palindrom")
# else:
#     print("the input is not palindrom")


n = int(input("Enter number:"))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
