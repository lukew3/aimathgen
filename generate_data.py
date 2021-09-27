from mathgenerator import mathgen

lines = []
for _ in range(1000):
    problem, solution = mathgen.addition()
    line = problem + solution + '\n'
    lines.append(line)

with open('data.txt', 'w') as f:
    f.writelines(lines)


