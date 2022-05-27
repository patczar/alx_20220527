from random import randint

x = randint(1, 100)
print(x)

if (y := x*x) > 100:
    print(f'x kwadrat jest duże, bo wynosi {y}')
else:
    print(f'x kwadrat jest małe, bo wynosi {y}')

while (x := 2*x) < 10_000:
    print(x)

