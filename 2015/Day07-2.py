class Wire:

    def __init__(self, name, cmd, in1, in2):
        self.name = name
        self.cmd = cmd
        self.in1 = in1
        self.in2 = in2
        self.val = None

book = [x.split() for x in open("2015/Day07.Input").read().splitlines()]
wire = {}

for instr in book:
    l = len(instr) 
    if l == 3:
        wire[instr[2]] = Wire(instr[2], 'SET', instr[0], None)
    if l == 4:
        wire[instr[3]] = Wire(instr[3], instr[0], instr[1], None)
    if l == 5:
        wire[instr[4]] = Wire(instr[4], instr[1], instr[0], instr[2])

def isInt(s):
    try:
        int(s)
        return True
    except:
        return False

wire['b'] = Wire('b', 'SET', '16076', None)

while True:
    for w in wire:
        if wire[w].val is None:
            if isInt(wire[w].in1):
                if (wire[w].cmd == 'SET'):
                    wire[w].val = int(wire[w].in1)
                elif (wire[w].cmd == 'NOT'):
                    wire[w].val = ~int(wire[w].in1)
                elif isInt(wire[w].in2):
                    if (wire[w].cmd == 'AND'):
                        wire[w].val = int(wire[w].in1) & int(wire[w].in2)
                    if (wire[w].cmd == 'OR'):
                        wire[w].val = int(wire[w].in1) | int(wire[w].in2)
                    if (wire[w].cmd == 'LSHIFT'):
                        wire[w].val = int(wire[w].in1) << int(wire[w].in2)
                    if (wire[w].cmd == 'RSHIFT'):
                        wire[w].val = int(wire[w].in1) >> int(wire[w].in2)
                else:
                    if not wire[wire[w].in2].val is None:
                        if isInt(wire[wire[w].in2].val):
                            wire[w].in2 = int(wire[wire[w].in2].val)
            else:
                if not wire[wire[w].in1].val is None:
                    if isInt(wire[wire[w].in1].val):
                        wire[w].in1 = int(wire[wire[w].in1].val)
    if not wire['a'].val is None:
        print(wire['a'].val)
        break