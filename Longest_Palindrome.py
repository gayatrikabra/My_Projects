# LARGEST PALINDROME SUBSTRING IN GIVEN STRING...

s = input("Enter String \n")
#palindrome = False
maxlen = 2
s_list = []
len_palindrome = dict()
for i in range((len(s)+1)):
    for j in range(1,(len(s)+1)):
        str1 = s[i:j]
        if(str1 == str1[::-1] and (len(str1) > 1)):
            s_list.append(str1)
            s_list.append(len(str1))

for item in s_list:
    len_palindrome = {s_list[i]: s_list[i + 1] for i in range(0, len(s_list), 2)}
print(len_palindrome)

ans = 0
for key,value  in len_palindrome.items():
    if value > maxlen:
        maxlen = value
        ans = key
    
print(f"largest palindrome substring in given string is {ans} with length {maxlen}")
            
        