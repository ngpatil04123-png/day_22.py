# print("Never Give up!!")
# mul=lambda x,y:x*y
# print(mul(4,50))
#---------------------------------------------------------------------------------------------------------------------------------------------------
# def sum_of_n():
#     sum=0
#     n=int(input("Enter the n value : "))
#     for i in range(1,n):
#         sum=sum+i
#     print(f"The sum of {n} numbers is: {sum}")
# sum_of_n()
#------------------------------------------------------------------------------------------------------------------------------------------------------
# a=int(input("Enter the a value : "))
# b=int(input("Enter the b value : "))
# add=lambda a,b:a+b 
# sub=lambda a,b:a-b 
# mul=lambda a,b:a*b 
# dev=lambda a,b:a/b 
# mod=lambda a,b:a//b 
# print(add(a,b))
# print(sub(a,b))
# print(mul(a,b))
# print(dev(a,b))
# print(mod(a,b))
#--------------------------------------------------------------------------------------------------------------------------------------------------
# def total(*number):
#     res=0
#     for num in number:
#         res+=num
#     return res
# print(total(1,2,3,4,5,6,7,8,9,10))
#------------------------------------------------------------------------------------------------------------------------------------------------
# def stu_info(**info):
#     for key,value in info.items():
#         print(f"The key is : {key} and value is : {value}")
# stu_info(name="naruto",age=20,work="Hokage")
#---------------------------------------------------------------------------------------------------------------------------------------------------
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(10))
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# def out_fun():
    
#     def in_fun():
#         name=str(input("Enter the name : "))
#         print(f"Hello,{name}")
#     in_fun()

# out_fun()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
def bodms():
    a=int(input("Enter the a value : "))
    b=int(input("Enter the b value : "))
    def add():
        sum=a+b
        print(f" The sum is : {sum}")
    add()
    def subt():
        sub=a-b
        print(f" The sub is : {sub}")
    subt()
    def mult():
        mul=a*b
        print(f" The mul is : {mul}")
    mult()
    def devs():
        dev=a/b
        print(f" The dev is : {dev}")
    devs()
bodms()
    
        






