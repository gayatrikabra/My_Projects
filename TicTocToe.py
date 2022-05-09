row_1 = [1, 2, 3]
row_2 = [4, 5, 6]
row_3 = [7, 8, 9]
def Display(row_1,row_2,row_3):
    print(row_1)
    print(row_2)
    print(row_3)
    
Display(row_1,row_2,row_3)

def User_input(position):
    user_1 = input("Enter X or O")
    if(position == 1 or position==2 or position ==3):
        #pos = "A"
        if position == 1:
            row_1[0] = user_1
            Display(row_1,row_2,row_3)
        if position == 2:
            row_1[1] = user_1
            Display(row_1,row_2,row_3)
        if position == 3:
            row_1[2] = user_1
            Display(row_1,row_2,row_3)
            
            
    if(position == 4 or position == 5 or position ==6):
        if position == 4:
            row_2[0] = user_1
            Display(row_1,row_2,row_3)
        if position == 5:
            row_2[1] = user_1
            Display(row_1,row_2,row_3)
        if position == 6:
            row_2[2] = user_1
            Display(row_1,row_2,row_3)
                
                
    if(position == 7 or position == 8 or position == 9):
        if position == 7:
            row_3[0] = user_1
            Display(row_1,row_2,row_3)
        if position == 8:
            row_3[1] = user_1
            Display(row_1,row_2,row_3)
        if position == 9:
            row_3[2] = user_1
            Display(row_1,row_2,row_3)
                    
                    
    else:
            pass
                    
        
            
            
            
            


def MainMethod():
    bool1 = True
    var1 = False
    var2 = False
    var3 = False
    var4 = False
    var5 = False
    var6= False
    var7 = False
    var8= False
    count = 0
    while(bool1):
        
        position = int(input("ENTER DESIRED POSITION"))
        User_input(position)
        count = count+1
        if(row_1[0] == row_1[1] and row_1[0]== row_1[2]):
            var1 = True
            bool1 = False
        if(row_1[0] == row_2[0] and row_1[0] == row_3[0]):
            var2 = True
            bool1 = False
        if(row_1[0]== row_2[1] and row_1[0]==row_3[2]):
             var3 = True
             bool1 = False
        if(row_1[1]==row_2[1] and row_1[1]==row_3[1]):
            var4 = True
            bool1 = False
        if(row_1[2]==row_2[2] and row_1[2]==row_3[2]):
            var5 = True
            bool1 = False
        if(row_1[2]==row_2[1] and row_1[2]==row_3[0]):
            var6 = True
            bool1 = False
        if(row_2[0] == row_2[1] and row_2[0] == row_2[2]):
            var7 = True
            bool1 = False
        if(row_3[0] == row_3[1]and row_3[0] == row_3[2]):
            var8 = True
            bool1 = False
          
        if(count == 9):
                print("Draw") 
                
        if(var1 or var2 or var3 or var5 or var6 or var7 or var8):
            print("User Won")
            
               
        
MainMethod()

    