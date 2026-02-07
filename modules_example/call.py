# import calculator
# import datetime

# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
# ans = calculator.aditionOfTwoDigit(12, 5)
# x = dir(calculator)
# print(ans)
# print(x)
# print(calculator.person1["name"])
