depths = open("Day1\day1input.txt").readlines()
largerThanPrevious = 0
current = int(depths[0])
depths.pop(0)
print("Starting point: " + str(current))
for i in depths:
    modifier = "(decreased)"
    if int(i) > int(current):
        largerThanPrevious += 1
        modifier = "(increased)"
    print(i + modifier)
    current = i

print(largerThanPrevious)