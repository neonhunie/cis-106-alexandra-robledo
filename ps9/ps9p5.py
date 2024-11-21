def display_arrays(players, averages):
  for i in range(len(players)):
      print(players[i], averages[i])

def search_player(players, averages, search_name):
  whichplayer = -1
  for i in range(len(players)):
      if players[i].lower() == search_name.lower():
          whichplayer = i
          break
  if whichplayer != -1:
      print(f"The batting average for {players[whichplayer]} is {averages[whichplayer]}")
  else:
      print(f"Player {search_name} not found.")

f = open("ps9p4.txt", "r")
player_name = f.readline().rstrip('\n')
players = []
averages = []

while player_name != "":
  players.append(player_name)
  average = float(f.readline())
  averages.append(average)
  player_name = f.readline().rstrip('\n')

print(players)
print(averages)

display_arrays(players, averages)

search_name = input("Enter a player's last name to search (or 'quit' to exit): ").rstrip('\n')
while search_name.lower() != 'quit':
  search_player(players, averages, search_name)
  search_name = input("Enter a player's last name to search (or 'quit' to exit): ").rstrip('\n')