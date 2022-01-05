def tax(num):
    if(num>18):
        if (num<65):
            return True
        else:
            return False
    else:
        return False
name = 'oren'
result=tax(18.1)
if result == True:
    print (name + ' owes tax')
else:
    print (name + ' dont owes tax')