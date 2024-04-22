"""""num1 = int(input('Digite o primeiro numero'))
num2 = int(input('Digite o segundo numero'))
num3 = int(input('Digite o terceiro numero'))

if num1 >num2 :
    print(num1)
elif num2 >num3:
    print(num2)
else:
    print(num3)"""

ref = 0
for x in range(3):
    n = int(input('Digite o segundo numero'))
    if n > ref:
        ref = n
print(ref)



