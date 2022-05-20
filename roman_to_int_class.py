
class Roman:
    my_dict= {'I' : 1 , 'V' : 5 , 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000}
    s_list = []
    list_val = []   
    def __init__(self,s):
        self.s = s
        
        
    def Separate_values(self):
        for char in self.s.upper():
            if Roman.my_dict.__contains__(char):
                self.s_list.append(char)
        for self.s in Roman.s_list:
            Roman.list_val = list(map(Roman.my_dict.get, Roman.s_list))
        
    def Convert(self):
        ans = 0
        if (len(Roman.list_val) == 1):
            ans = list(map(Roman.my_dict.get,Roman.s_list))
        else:
            for i in range(0,(len(Roman.list_val)-1),2):
                if(int(Roman.list_val[i]) >= int(Roman.list_val[i+1])):
                    ans += (Roman.list_val[i] + Roman.list_val[i+1])
                else:
                    ans += (Roman.list_val[i+1] - Roman.list_val[i])
        return ans
                    
    
    
    
s = input("Enter roman no\n")
R = Roman(s)
R.Separate_values()
print(R.Convert() )
    