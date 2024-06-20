#print ("Hello", "My", "name is Pratyush", sep="-",end=" ")
#print("Ninja")
#print("Hello" + " " "future" + " " "python!")
#print('My age is ' ,"+ 25")
#print (type ("True"))


# x = 10 / 4
# print(x)
# y = 6. / 4
# print(y)
# print (x + y)

# print(10 - 6 ** 2 / 9 * 10 + 1)

# y = 5
# y = "Jack"
# print(y)


#INPUT 

# name=input("Hello,What is your name?\n")

# print("Hello My name is "+ name )


# add_1=int(input("Enter the first number->"))
# add_2=int(input("Enter the second number->"))
# sum= add_1 + add_2
# print ("The sum is->"+str(sum))

# inputString = input('Enter a string: ')
# print(inputString, sep='#', end='&')

# print("hello "*10)

# Num = input("Enter a Number: ") 
# print (Num * 3 )

# check_1=int(input("Enter the first number->"))
# check_2=int(input("Enter the second number->"))

# def check_num(a,b):
#     if (a == b):
#         return True
#     else:
#         return False
    
# check_num(check_1,check_2)

# num=3
# guess= " "
# while guess != num or guess == "":
#     guess = int(input("Guess the number->"))
#     print("Not the correct number, Guess again")
# else:
#     print("congo")

# print (5 % 9)
# i = 2
# i += 2
# print (i)
# # i = 1
# while True:
#     if i % 0o7 == 0:
#         break
#     print(i)
#     i += 1


# i = 2
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 2

# x = 'abcd'
# for i in range(len(x)):
#     i.upper()
# print (x)


# x = 6
# print(x > 4 and x < 12)



#print(0b11001)


# print(22 << 1)

# print(bin(44))


# a = 20

# b = 5
# print(bin(b))
# print(0b10101)
# print("a & b =", a & b)

# print(5^11)



# list=[1,2,3,4]*4
# list2=list
# print(list)

# list[0]=0
# print(list)
# print(list2)



a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a)

print(a[2][3])
