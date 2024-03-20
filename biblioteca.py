from math import cos, sin, tan, radians

ang = int(input('Introduza o valor do seu angulo:'))

ang_rad = radians(ang)

sin = sin(ang_rad)
tan = tan(ang_rad)
cos = cos(ang_rad)

print('O seno do angulo é:',sin)
print('A tangente do angulo é:',tan)
print('O cosseno do angulo é',cos)