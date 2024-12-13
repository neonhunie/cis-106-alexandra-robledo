num_items = int(input("Enter the number of items in the list: "))
my_list = []
for i in range(num_items):
    value = int(input("Enter a number: "))
    my_list.append(value)
print("List:", my_list)

my_list.insert(1, 99)
print("List after inserting 99:", my_list)

my_list[my_list.index(99)] = 100
print("List after replacing 99 with 100:", my_list)

second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)
my_list.extend(second_list)
print("First list after extending:", my_list)

my_list.remove(800)
print("List after removing 800:", my_list)

my_list.pop(2)
print("List after removing the third item:", my_list)

grades = ["A", "B", "C", "A", "A", "C"]
print("Number of A grades:", grades.count("A"))
print("Index of the first B grade:", grades.index("B"))

if "F" not in grades:
    print("F is not in the list")

second_list.clear()
print("Second list after clearing:", second_list)

del second_list
try:
    print(second_list)
except:
    print("Second list no longer exists")

players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
players.sort()
print("Sorted players:", players)

players2 = players.copy()
print("Copied list of players:", players2)

players2.reverse()
print("Original players list:", players)
print("Reversed copy of players list:", players2)
