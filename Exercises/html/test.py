head = [0]
pos = [0,0]

def north(val):
    pos[1] += val

def right(val):
    head[0] += val
    head[0] %=360

north(10)
print(pos)
right(10)

print(head)