output = ""

for i in range(1,15):
    for k in range(15,i, -1):
        output += ' '
    for u in range(0,2 * i -1):
        output += "*"
    output += '\n'

print(output)
