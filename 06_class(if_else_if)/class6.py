# union type (assign multiple types)
from typing import Union

percentage : Union[int,float] = 48
grade : Union[str,None] = 7 

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
elif percentage >= 33:
    grade = "E"
else:
    grade = "Fail"
print(f"Dear Student your peercentage is {percentage} now your calculated grade is: \t{grade}")

