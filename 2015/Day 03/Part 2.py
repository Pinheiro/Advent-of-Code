class Deliver:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.updatePosition()

    def move(self, d):
        if (d == "^"):
            self.y += 1
        if (d == "v"):
            self.y -= 1
        if (d == ">"):
            self.x += 1
        if (d == "<"):
            self.x -= 1
        self.updatePosition()

    def updatePosition(self):
        self.p = str(self.x) + ',' + str(self.y)

s = Deliver() # Santa coordinates
r = Deliver() # Robot coordinates

directions = [x for x in open("2015/Day 03/Input.txt").read()]
houses = [] # x,y coordinates for each house receiving a present
turn = True # (True) Santa turn; (False) Robot turn

houses.append(s.p) # first house serviced by Santa
houses.append(r.p) # first house serviced by the robot

for d in directions: # update coordinates depending on direction received
    if (turn): # Santa turn to process the direction
        s.move(d)
        houses.append(s.p)
    else: # Robot turn to process the direction
        r.move(d)
        houses.append(r.p)
    turn = not turn
houses = list(dict.fromkeys(houses)) # remove duplicate houses from the list
print(len(houses))