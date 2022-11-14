def solution():
    size=[]
    figure = ""
    for x in range(10):
        figure += "X"        
        size.append(figure + "S")
    
    size.append("S")
    size.append("M")
    size.append("L")
    figure = "" 
    for x in range(10):        
        figure += "X"
        size.append(figure + "L")

    node = input() 
    index = size.index(node)
    
    total_no_shirts = input()
    

    for i in size[index+1::]:
        print(i + " " ,end="")
solution()

