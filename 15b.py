datafile = "../../AoC/2023/15.txt"

REMOVE = 0
ADD = 1

boxes = []

def hash(label):
    val = 0
    for char in label:
        val = ((val + ord(char)) * 17) % 256
    return val

with open(datafile) as input:
    data = input.read()
    steps = data[:-1].split(",")

for n in range(256):
    boxes.append({})

for step in steps:
    if step[-1] == "-":
        action = REMOVE
        label = step[:-1]
    else:
        action = ADD
        label = step[:-2]
        fl = int(step[-1])
    box_no = hash(label)
    if action == REMOVE:
        boxes[box_no].pop(label, None)
    else:
        boxes[box_no][label] = fl

power = 0
for box_no in range(256):
    slot_no = 0
    for fl in boxes[box_no].values():
        slot_no += 1
        power += (box_no + 1) * slot_no * fl

print('Result = ', power)