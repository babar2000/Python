print("This is my 1st Q3 class!")
name: str = "Zia Khan"
print(name)
print("name")

print("My name is", name)
print("This is our class")
print('This is our class')
print('"Be patient, because good things come to those who wait"')
print(''' Be Patient, because good things
      come to those who wait
      ''')
print('PIAIC', 'GenAI', 'Cloud Applied',sep='---')
print('PIAIC', end=' ')
print('GenAI', end=' ')
print('Cloud Applied', end=' ')

fruits: list[str] = ['apple','banana','Lemon','Chiki','Mango','melon']
print(fruits)
print(fruits[2])
print(fruits[-2])
print(fruits[3:5])
print(fruits[-3:-1])
print(fruits[-3:-5])
print(fruits[0:])
print(fruits[0::2])
fruits.sort()
print(fruits)
print(fruits.count('apple'))


fruits.append('Watermelon')
fruits_list = list(fruits)
fruits_list.append('Watermelon')
fruits=tuple(fruits_list)
print(fruits)

x:int= 0
while x <=10:
    print("Zain")
    x = x+1

x : int = 0
for x in range(10):
    print('Zain')
    