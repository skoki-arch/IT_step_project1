def calculate_expression():
    
    inputedval = input("შეიყვანეთ გამოსხულება გამოსათვლელად: ")
   
    try:
        calcuatedval = eval(inputedval)
        print(calcuatedval)
    except:
        print("გამოსახულების გამოთვლა შეუძლებელია")
    
    

calculate_expression()