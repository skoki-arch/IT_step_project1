import random

def guessthenumber():
    
    rnumber = random.randint(0, 100)
    count = 0

    while True:
        inpvalue = input("შეიყვანეთ რიცხვი 1-დან 100-მდე: ")
        if inpvalue == "exit":
            break
        
        try:
            inpvalue = int(inpvalue)
        except:
            print("აუცილებელია შეიყვანოთ რიცხვი!")
            next

        if inpvalue < 1 or inpvalue > 100:
            print("რიცხვი უნდა იყოს 1დან 100მდე!")
            next
        
        count += 1
        if inpvalue == rnumber:
            print(f"რიცხვი გამოცნობილია! მცდელობების რაოდენობა {count}")
            break
        elif inpvalue < rnumber:
            print("უფრო მაღალი!")
        else:
            print("უფრო დაბალი!")
        

guessthenumber()