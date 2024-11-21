def display(names):
  for i in names:
    print(i)

def reverse(names):
  for i in range (len(names)-1, -1, -1):
    print(names[i])

names=['Kuko', 'Rusty', 'Ryu', 'Donna', 'Bobby','Momma']

display(names)
print()
reverse(names)