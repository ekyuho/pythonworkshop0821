lastname= input('Lastname? ')
point = input('Point? ')
if lastname in { 'kim', 'lee' }:
    point = int(point) + 15  # from master
    print(point)
else:
    point = int(point) + 10
    print(point)

input('anything else? ')
print('done')
print('try again? ')
