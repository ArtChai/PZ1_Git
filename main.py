
import help
from messages import begin
from operations import calculate

begin()
help.help()

a = float(input("введите первое число: "))
b = float(input("введите второе число: "))
operation = input("введите операцию (+ или -): ")

print("результат:", calculate(a, b, operation))
