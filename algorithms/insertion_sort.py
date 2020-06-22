a = [1, 2, 3, 4, 5]
u = int(input('Число:'))
j = 0
i = 'nil'

for j in range(len(a)):
    if (a[j] == u): 
        i = j
        break

print(i)