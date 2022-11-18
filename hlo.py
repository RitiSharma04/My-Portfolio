from tkinter.messagebox import YES


sign_up=input("enter the sign")
if(sign_up=="yes"):
    print("next")
    number=int(input("enter the mob.no"))
    if len(str(number))==10:
        print(number)
        name=input("enter the name")
        if((name>="a")and(name<="z")and(name>="A")and(name<="z")):
            print(name)
            sarname=input("enter the sarname")
            if((sarname>="a")and(sarname<="z")or(sarname>="A")and(sarname<="Z")):
                print(sarname)
                gender=input("enter the gender")
                if((gender=="male")or(gender=="female")):
                    print(gender)
                    year=int(input("enter the year"))
                    if(year>=2000):
                        print(year)
                        month=int(input("enter the month"))
                        if(month<=12):
                            print(month)
                            date=int(input("enter the date"))
                            if(date<=31):
                                print(date)
                                PASS=(input("enter the password"))
                                if((PASS=="#@&")and(PASS>="a")and (PASS<="z")or(PASS>="A")and(PASS<="Z")and(PASS>=0)and(PASS<=9)in(PASS)):
                                    print(PASS)
                                    confirm=input("enter the pass")
                                    if(confirm=="yes"):
                                        print("welcome")
                                    else:
                                        print ("not confirm")
                                else:
                                    print("invalid PASS")
                            else:
                                print("incorrect phone")
                        else:
                            print("invalid date")             
                    else:
                        print("invalid month")
                else:
                    print("invalid year")
            else:
                print("incorrect gender")
        else:
            print("incorrect sarname")
    else:
        print("incorrect name")
else:
    print("wrong")
