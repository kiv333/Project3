a, b, perks, car = 2, 1, [], {}
for i in range(1, a+1):
    for j in range(1, b+1):
        if car == None:
            continue
        else:
            for k in range(4):
                perks1 = int(input(f"Введите {i} в {j} = "))
                perks.append(perks1)
            car [i,j] = perks
            print(perks)
            perks = []
print(car)



