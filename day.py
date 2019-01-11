date=int(input("enter the date"))
month=int(input("enter the month"))
t=365
if month==1:
    rem=(31-date)+(t-31)
    print("no. of remaining days=",rem)
elif month==2:
    rem=(28-date)+(t-31-28)
    print("no. of remaining days=",rem)
elif month==3:
    rem=(31-date)+(t-31-28-31)
    print("no. of remaining days=",rem)
elif month==4:
    rem=(30-date)+(t-31-28-31-30)
    print("no. of remaining days=",rem)
elif month==5:
    rem=(31-date)+(t-31-28-31-30-31)
    print("no. of remaining days=",rem)
elif month==6:
    rem=(30-date)+(t-31-28-31-30-30-31)
    print("no. of remaining days=",rem)
elif month==7:
    rem=(31-date)+(t-31-28-31-30-30-31-31)
    print("no. of remaining days=",rem)
elif month==8:
    rem=(31-date)+(t-31-28-31-30-30-31-31-31)
    print("no. of remaining days=",rem)
elif month==9:
    rem=(30-date)+(t-31-28-31-30-30-31-31-31-30)
    print("no. of remaining days=",rem)
elif month==10:
    rem=(31-date)+(t-31-28-31-30-30-31-31-31-30-31)
    print("no. of remaining days=",rem)
elif month==11:
    rem=(30-date)+(t-31-28-31-30-30-31-31-31-30-31-30)
    print("no. of remaining days=",rem)
elif month==12 :
    rem=31-date
    print("no. of remaining days=",rem)
else :
    print("invalid input")
 
