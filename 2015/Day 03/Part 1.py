directions = [x for x in open("2015/Day 03/Input.txt").read()]
houses = [] # x,y coordinates for each house receiving a present
x = 0
y = 0
houses.append(str(x) + str(y)) # first house at position (0,0)
for d in directions: # update coordinates depending on direction received 
    if (d == "^"):
        y += 1
    if (d == "v"):
        y -= 1
    if (d == ">"):
        x += 1
    if (d == "<"):
        x -= 1
    houses.append(str(x) + str(y)) # append each house to the list
houses = list(dict.fromkeys(houses)) # remove duplicate houses from the list
print(len(houses))