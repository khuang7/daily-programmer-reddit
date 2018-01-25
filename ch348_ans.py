#A way simpler sample solution

#Creates an empty array of 96 elements (representing months)
bun_m, bun_f = [[0 for x in range(96)] for i in range(2)]

# so they put like 2 in the 2 month stage coz theres 2 rabbits at that age
bun_m[2], bun_f[2] = 2, 4


count = 0

while sum(bun_f) + sum(bun_m) < 1000:
    new_b = sum(bun_f[4:]) 
    bun_f = [9*new_b] + bun_f[:-1] #adds 9 new females
    bun_m = [5*new_b] + bun_m[:-1] #adds 5 new males

    print(bun_f)


    count += 1 #iterate month
print(count)