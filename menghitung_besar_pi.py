import random as rd
def pi(banyak_data):
    num_circle = 0
    num_point = 0
    for i in range(banyak_data):
        x = rd.random()
        y = rd.random()
        distance = x**2+y**2
        if distance<=1:
            num_point+=1
        num_circle+=1
    print(4*num_point/num_circle)
    print(num_circle)
    print(num_point)
pi(10000)