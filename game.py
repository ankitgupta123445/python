print("------------welcome to the game--------------")
print("choose a no. which are present between 1 and 31")
print("check if it is present in given line press '1' otherwise '0'")
k=0

num=int(input("16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31"))
if num==1 or num==0 :
    k=k+num*16
else :
    print("wrong input")
    print("warning : restart the game otherwise it give wrong input")
num=int(input("8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31"))
if num==1 or num==0 :
    k=k+num*8
else :
    print("wrong input")
    print("warning : restart the game otherwise it give wrong input")
num=int(input("4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31"))
if num==1 or num==0 :
    k=k+num*4
else :
    print("wrong input")
    print("warning : restart the game otherwise it give wrong input")
num=int(input("2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31"))
if num==1 or num==0 :
    k=k+num*2
else :
    print("wrong input")
    print("warning : restart the game otherwise it give wrong input")
num=int(input("1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31"))
if num==1 or num==0 :
    k=k+num*1
else :
    print("wrong input")
    print("warning : restart the game otherwise it give wrong input")
print(k)


