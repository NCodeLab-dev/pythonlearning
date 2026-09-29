

names=[
    "narayan sahu",
    "pallavi sahu",
    "jagannath sahu",
    "rukmani sahu"
]

names_without_spaces=[]

for name in names:
    names_without_spaces.append(name.replace(" ","-"))

print(names_without_spaces)


withoutSpaces= [name.replace(" ","-") for name in names]




print(dir(withoutSpaces))
fruits = ["pears", "apples", "bananas"]
for fruit in reversed(fruits):
  print(fruit)
y = "Yay!"
print(len(y))



p = 3, 4, 5
q = (6, 7, 8)
print(type(p))
print(type(q))


fruits = {"apples": 2, "pears": 3, "grapes": 20}
y = fruits.pop("apples")
print(y)
p = (2, 1, 3)
x, y, z = p
print(x)

months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
print(months[1:3])
