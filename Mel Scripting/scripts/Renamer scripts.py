def Renamer (input):
   
    name = input 
    newName = name.split ("#")
    
        
    first = newName[0]
    second = newName[1]
    
    sel = cmds.ls(selection=True)
    
    num = 0
    

    hash = len(name) - (len(first) + len(second))
   

    for obj in sel:
        
        mid = ""
        num +=1
        
        i=1
        while i<=num:
            
            digits = 3
            digits+=1
          

            i*=2

        dif = hash - digits
        

        i=0
        while i < dif:
            

            mid += "0"
            i+=1


        mid += str(num)
        


        renamer = first + mid + second    
        cmds.rename (obj, renamer)
        
Renamer("R_Robot_##_jnt")