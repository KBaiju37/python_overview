pas = input("enter password : ")
if len(pas)>=8 and any(c.isdigit() for c in pas):
    print("strong password")
else :
    print("weak password")

