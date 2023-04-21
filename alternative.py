# intializing string
test_str= "helloworld"
#printing original string
print("the original string is:"+str(test_str))
# Alterntive case in stirng using loop
res = ""
for idx in range(len(test_str)):
    if not idx %2 :
      res = res + test_str[idx].upper()
    else:  
       res = res + test_str[idx].lower()
 # printing the alternative string 
print("the alternative case string is:" +str(res))      


new_string = input("Please enter a string: ").split()
char_storage = " ".join([x.upper() if i % 2 else x.lower() for i, x in enumerate(new_string)])
#printing alternative word in string
print(char_storage) 