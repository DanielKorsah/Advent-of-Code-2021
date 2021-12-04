depths = list(map(int, open("input.txt", "r").readlines()))
count_inc = 0
triplets = []
for i in range(2, len(depths)):
    triplets.append([depths[i], depths[i - 1], depths[i - 2]])
for i in range(1, len(triplets)):
    count_inc += sum(triplets[i]) > sum(triplets[i - 1])
print(count_inc)
