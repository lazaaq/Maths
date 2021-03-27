import math #to import module math (we are gonna using math.sqrt())

user_input = int(input()) #user input (non-negative integer)
int_input = int(math.sqrt(user_input)) #root

inside_root = root #this is the value outside the root symbol, which has default 1
for i in range(int_input, 0, -1):
    square = i*i
    if int(user_input/square) == user_input/square: 
        #we are gonna scan from int_input until reach 1, and then stop. when we find this if statement true, 
        #which is that "i" integer is a square integer, we gonna change the "inside_root" value, and then break the loop
        inside_root = int(user_input/square)
        break

outside_root = int(math.sqrt(user_input/root)) #this is the value inside root symbol

print(outside_root, "root", inside_root)

sample input  : 90
sample output : 3 root 10
    

sample input  : 54
sample output : 3 root 6
