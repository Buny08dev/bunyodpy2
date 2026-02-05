# a=2.3245123
# print("%.0f" % a,"hello", "world", sep="\n" )


# from math import *

# x1,x2,c,d=map(float, input().split())
# c=int(c)
# d=int(d)

# f1=abs( (sin(fabs(c*x2**3+d*x1**3-c*d))**2) / (sqrt((c*x1**2+d*x2**2+2)+5)) )+tan(x1*x2**2+d**3)

# print("%.2f"%f1)
# a=int(input())
# if (a%4==0 or a%400==0) and a%100!=0:
#     print("kabisa yili")
# print((a%4==0 or a%400==0) and  a%100!=0)
# print(a%4==0 or a%400==0 and a%100!=0)




# l=0
# for i in s:
#     if i==s[0] and i=="-" and s[1]!="0":
#         l+=1
#     if "0"<=i<="9" and s[0]!="0":
#             l+=1

# s=input()
# if "-"==s[0]:
#     if s[1:].isdecimal():
#         print("Yes")
#     else:
#         print("No")
# elif s.isdecimal():
#     print("Yes")
# else:
#     print("No")



####################################### o`yin
# from random import *
# round=int(input("raund soni: "))
# for i in range(round):
#     print("Oyinchi tepish vaqti!!")
#     oyinchi_top=int(input("Qayerga tepasan(1,2,3): "))
#     # komp_varatar=choice("ong","orta","chap")
#     komp_varatar=randrange(1, 4)
#     oyinchi=0
#     Kompyuter=0
#     if oyinchi_top!=oyinchi:
#         print("---Oyinchi--- gol urdi 1 ochko\n")
#         oyinchi+=1
#     else:
#         print("---Kampyuter--- qaytardi 1 ochko\n")
#     print("Oyinchi qaytarish vaqti")
#     oyinchi_varatar=int(input("Qayerni qaytarasan(1,2,3): "))
#     komp_top=randrange(1, 4)
#     if oyinchi_varatar==komp_top:
#         print("---Oyinchi--- qaytardi 1 ochko\n")
#     else:
#         print("---Kampyuter--- gol urdi 1 ochko\n")
#         Kompyuter+=1
# else:
#     if Kompyuter==oyinchi:
#         while Kompyuter==oyinchi:
#             print("Turrang bolgani uchun yana bir oyin qoshiladi\n")
#             print("Oyinchi tepish vaqti!!")
#             oyinchi_top=int(input("Qayerga tepasan(1,2,3): "))
#             # komp_varatar=choice("ong","orta","chap")
#             komp_varatar=randrange(1, 4)
#             if oyinchi_top!=oyinchi:
#                 print("---Oyinchi--- gol urdi 1 ochko\n")
#                 oyinchi+=1
#             else:
#                 print("---Kampyuter--- qaytardi 1 ochko\n")
#             print("Oyinchi qaytarish vaqti")
#             oyinchi_varatar=int(input("Qayerni qaytarasan(1,2,3): "))
#             komp_top=randrange(1, 4)
#             if oyinchi_varatar==komp_top:
#                 print("---Oyinchi--- qaytardi 1 ochko\n")
#             else:
#                 print("---Kampyuter--- gol urdi 1 ochko\n")
#                 Kompyuter+=1
# if Kompyuter>oyinchi:
#     print(f"---Komputer--- yutdi {Kompyuter}:{oyinchi}ga")
# else:
#     print(f"---Oyinchi--- yutdi {oyinchi}:{Kompyuter}ga")







# print("*".join(list("python programming")))


# 7. Markazlashtirish
# txt = "python programming" 
# print(txt.center(20)) 

# 8. Bosh harf bilan boshlanishini tekshirish
# txt = "python programming" 
# print(txt.startswith(txt[0].upper())) 

# 9. Kichik va bosh harflarni o‘zgartirish
# txt = "Python ProgramminNg" 
# print(txt.capitalize()) 

# 10. Bosh harf bilan boshlanishini tekshirish
# txt = "Python programming" 
# print(txt.startswith("hello")) 

# 11. Harflarni aylantirish
# txt="Python is FUN"
# print(txt.swapcase()) 

# 12. Maxsus formatlash
# txt="hello world python"
# txt=txt.title()
# for i in range(1,len(txt.split())+1):
#     print(txt.split()[i-1])


####################################### Murakkab topshiriqlar

# a1=list(map(int,input().split()))[:10]
# for i in a1:
#     if i>0:
#         a=a1
#         print(f" {i}-musbat")
#     elif i==0:
#         print(f" {i} -nol")
#     else:
#         print(f"{i}-manfiy")

# n = int(input())
# s = list(map(int , input().split()))[:n]
# for i in range(n):
#     print(i)
#     print(s[i])
#     if s[i] < 0:
#         s.remove(s[i])
# print(s)


# a={
#     "name":"bunyod",
#     "age":16,
#     "Is_married":False  
# }
# for i in a:
#     print(i)


# def argv_int(*a):
#     a=list(a)
#     int_=[]
#     for i in a:
#         if type(i)==int:
#             print(i)
#             int_.append(i)
#     return len(int_)

# def params(*arg,**a):
#     return(len(arg)+len(a))

# def f(x,y):
#     if (x**5+y)*(y+2)>x**6:
#         return (x**2+x)/y
#     else:
#         return x+y
# print(f(8,6))

# n=int(input())
# for i in range(2,n):
#     for j in range(2,int(i**(1/2)+1)):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")


# a=[0,1]
# def qoshish(x):
#     if x>a[-1]:
#         a.append(a[-1]+a[-2])
#         return qoshish(x)
#     else:
#         del a[-1]
#         return a
# print(qoshish(50))


# a=lambda name: len(name)
# print(sorted(["san", "bular","ular","bunyod"],key=a))



# 1
# def Salom_dunyo():
#     return "Salom Dunyo"

# 2
# def Salom_name(name):
#     return f"Salom {name}"

# 3
# def plus(a,b):
#     return a+b

# 4
# def son_kvadrat(a):
#     return a**2

# 5
# def orta_qiymat(a,b,c):
#     return (a+b+c)/3

# 6
# def toq_or_juft(n):
#     if n%2==0 and n!=0:
#         return "juft son"
#     elif n%2==1:
#         return "toq son"
#     else:
#         return "son 0"

# 7
# def eng_katta_son(a,b,c):
#     return max(a,b,c)

# 8
# def polindrom_soz(a):
#     if a==a[::-1]:
#         return f"{a} -- Polimdrom soz"
#     else:
#         return f"{a} -- Polimdrom soz emas"
# print(polindrom_soz("tot"))

# 9
# def manfiy_or_musbat(n):
#     if n>0:
#         return "Musbat son"
#     elif n<0:
#         return "Manfiy son"
#     else:
#         return "0 son"

# 10
# def kabisa_yil(year):
#     if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#         print(f'{year} Kabisa yili')
#     else:
#         print(f'{year} Kabisa yili emas')

# nums= list(map(int,input().split()))
# target = int(input())


# def two_sum(nums:list, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
# print(two_sum(nums,target))



# # 2. Add Two Numbers
# def addTwoNumbers(l1:list, l2:list):
#     answer=int("".join(list(map(lambda x:str(x),l1))[::-1]))+int("".join(list(map(lambda x:str(x),l2))[::-1]))
#     return [int(i) for i in str(answer)][::-1]
# print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))


# for i in range(1,103):
#     if 102%i==0:
#         print(i)

# class bunyod:
#     def __init__(self,name:str,years:int):
#         self.__name=name 
#         self.__years=years
#     def intrdoduction(self):
#         return self.__name, self.__years
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self,new_name):
#         self.__name=new_name 
# a=bunyod("bunyod",15)
# a.name="azamat"
# print(a._bunyod__name)


# class bunyod:
#     name="bunyod"
# print(bunyod.name)


# print(bunyod("bunyod",16).intrdoduction())


# from time import time

# a = time()
# # .20f - nuqtadan keyin 20 ta raqam chiqar degani
# print(f"{a:.20f}")


# name="Bunyo-d 123"
# print("-".join(name.lower().split()))
# print("-".join(map(lambda x:x.lower(), name.split())))
# b=time()
# print(f"{a:.30f},\n{a:.30f}")

# from timeit import timeit


# def switch():
#     b = 200
#     match b:
#         case 200:
#             return "ok"
# def condition():
#     a = 200
#     if a == 200:
#         return 'ok'
#     else:
#         return 'error'
    
# work=timeit(switch,number=1000)
# print(f'switch {work}')

# work2=timeit(condition,number=1000)

# print(f'condition {work2}')

