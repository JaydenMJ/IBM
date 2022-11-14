def solution():
    with open(file) as f:
        lines = f.readlines()
    line = input()
    allValid = True
    errorCodes=[]
    
    for record in lines[:line]:
            allValid = record.isValid()  

            if record.isvalid() == False:
                errorCodes.append(record.split(" ")[2])
                allValid = False

            
    if allValid :
        print("Yes")
    if allValid==False:
        for x in errorCodes:            
            print ( "No",x + " ",end="")
