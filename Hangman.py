import random
import re

def funcguesstheword():
    words = ["წიგნი", "რვეული", "კალამი", "მერხი", "სახაზავი"]
    usedletters = []

    guessword = list(random.choice(words))

    resword = "_ " * len(guessword)
    reslist = resword.split()

    print("გამოიცანი სასკოლო ინვენტარი: ", resword)

    while True:

       inpvalue = input("შეიყვანე ქართული სიმბოლო: ")

       if inpvalue == "exit":
            break

       if len(inpvalue) != 1:
            print("შეყვანილი სიმბოლოების რაოდენობა უნდა იყოს ერთი")
            next
       elif ord(inpvalue) < ord("ა") or ord(inpvalue) > ord("ჰ"):
            print("სიმბოლო უნდა იყოს ქართული ალფავიტიდან!")
            next
       elif inpvalue in usedletters:
           print("სიმბოლო უკვე გამოყენებულია!")
       else:
            
           usedletters.append(inpvalue) 
           symbolfound = False
           for i in range(len(guessword)):
                if guessword[i] == inpvalue:
                    reslist[i] = inpvalue
                    symbolfound = True
           if not symbolfound:
               print(f"სიმბოლო არ მოიძებნა. მცდელობა # {len(usedletters)}")
           elif not "_" in reslist:
               print("სიტყვა გამოცნობილია: ", reslist)
               return

           print(*reslist, sep=" ")
                

             

funcguesstheword()