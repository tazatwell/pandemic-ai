#pandemic.py: The board game pandemic

import random;

#edge class:
class Edge:
	start = "San Francisco";
	end = "Tokyo";


#city class:
class City:
	name = "San Francisco";
	color = "Blue";

	#list of edges from city to neighboring cities
	neighbors = [];

	numDiseaseCubes = 0;

	hasResearchCenter = False;

	#class constructor
	def __init__(self, new_name):
		self.name = new_name;
		self.color = "blue";
		self.neighbors = [];
		self.numDiseaseCubes = 0;	
		hasResearchCenter = False;

	#print fn
	def startCityPrint(self):
		print("City - " + self.name);
		print("\t" + "color: " + self.color);
		print("\t" + str(self.numDiseaseCubes) + " disease cubes");
		print("\t" + "research center - " + self.hasResearchCenter);
		#if (self.hasResearchCenter == True):
		#	print("\t" + "has research center");
		#elif (self.hasResearchCenter == False):
		#	print("\t" + "doesn't have research center");
		print("\t" + "neighbors:");
		for i in self.neighbors:
			print("\t\t" + i);


#Players
class Player:
	role = "Scientist";
	position = "Atlanta";
	cards = [];

	#constructor
	def __init__(self, new_role):
		self.role = new_role;
		self.position = "Atlanta";
		self.cards = [];

	def playerPrint(self):
		print("Player - " + self.role);
		print("\tin " + self.position);
		print("\tHand:");
		for i in self.cards:
			print("\t\t" + i);



#get list of cities
citiesList = [];

f = open('cities.txt', 'r');
for i in f:
	newCity = i[0:-1];
	citiesList.append(newCity);
f.close();

#works
#for i in citiesList:
#	print(i);
#print(len(citiesList));

#list of edges
edgesList = {};

#initialize all edges to 0
for i in citiesList:
	for j in citiesList:
		new_key = i + " - " + j;
		edgesList[new_key] = 0;

#print all edges - works!
#for i,j in edgesList.items():
#	print(i + '\t' + str(j));


#set the edges on the board to 1
#these edges are stored in edges.txt
f = open('edges.txt', 'r');
f_lines = f.readlines();
for i,j in edgesList.items():
	search_string = i + '\n';
	#print(search_string);
	if search_string in f_lines:
		j = 1;
		edgesList[i] = 1;
		#print("there's an edge between " + i);

#see num of edges that are on the board:
numEdges = 0;
for i,j in edgesList.items():
	if (j == 1):
		numEdges = numEdges + 1;
#		print("there's an edge between " + i);
#print("number of directed edges is " + str(numEdges));
#print("number of bidirectional edges is " + str(numEdges/2));


#deck of infection cards:
infectionCards = [];
for i in citiesList:
	infectionCards.append(i);
#print(infectionCards);
#print(citiesList);
#for i in citiesList:
#	print(i);


#deck of player cards:
playerCards = citiesList;

#create list of colored cities:
blueCities = ["San Francisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "Madrid", "London", "Essen", "St. Petersburg", "Paris", "Milan"];

yellowCities = ["Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Sao Paolo", "Buenos Aires", "Lagos", "Khartoum", "Kinshasa", "Johannesburg"];

blackCities = ["Moscow", "Tehran", "Istanbul", "Algiers", "Cairo", "Baghdad", "Karachi", "Delhi", "Kolkata", "Riyadh", "Mumbai", "Chennai"];

redCities = ["Beijing", "Seoul", "Shanghai", "Tokyo", "Hong Kong", "Taipei", "Osaka", "Bangkok", "Ho Chi Minh City", "Manila", "Jakarta", "Sydney"];

#initialize the cities:
boardCities = {};
for i in citiesList:
	new_city = City(i);
	if i in blueCities:
		new_city.color = "blue";
	elif i in yellowCities:
		new_city.color = "yellow";
	elif i in blackCities:
		new_city.color = "black";
	elif i in redCities:
		new_city.color = "red";
	else:
		print("city not in colors list - " + i);
		exit();
	new_city.numDiseaseCubes = 0;
	if (i == "Atlanta"):
		new_city.hasResearchCenter = "true";
	else:
		new_city.hasResearchCenter = "false";
	for j in citiesList:
		search_string = i + " - " + j;
		if (edgesList[search_string] == 1):
			new_city.neighbors.append(j);
	boardCities[i] = new_city;


#print status of board after start of game:
#print("cities' status before game:");
#for i,j in boardCities.items():
	#print("an element");
	#print(j.name + '\t' + j.color + '\t' + str(j.numDiseaseCubes) + '\t' + j.hasResearchCenter + '\t');
	#j.startCityPrint();
	#for neighbor in j.neighbors:
		#print(neighbor);

#list of character roles:
character_roles = ["Scientist", "Medic", "Researcher", "Dispatcher", "Operations Expert", "Contingency Planner", "Quarantine Specialist"];
players = [];

numPlayers = int(input("how many players are playing?"));

counter = 0;
while (counter < numPlayers):
	role = random.choice(character_roles);
	character_roles.remove(role);
	new_player = Player(role);
	players.append(new_player);
	counter = counter + 1;

count = 1;
for i in players:
	#player_no = i+1;
	#player_no_string = str(player_no);
	i.playerPrint();
	count = count + 1;

#set up cities w diseases:
random.shuffle(infectionCards);

#print(infectionCards);

#works - now randomized.
#for i in infectionCards:
#	print(i);

#infection counter
infectionCounter = 2;

#num of free moves before incrementing infectionCounter w u play an epidemic card.
numEpidemicFreeMoves = 1;

#infection discard pile
infectionDiscardPile = [];

#set up diseased cities:
for i in range(3):
	next_city = random.choice(infectionCards);
	infectionDiscardPile.append(next_city);
	infectionCards.remove(next_city);
	boardCities[next_city].numDiseaseCubes = 3;

for i in range(3):
	next_city = random.choice(infectionCards);
	infectionDiscardPile.append(next_city);
	infectionCards.remove(next_city);
	boardCities[next_city].numDiseaseCubes = 2;

for i in range(3):
	next_city = random.choice(infectionCards);
	infectionDiscardPile.append(next_city);
	infectionCards.remove(next_city);
	boardCities[next_city].numDiseaseCubes = 1;

'''
#print diseased Cities
for i in boardCities:
	if (boardCities[i].numDiseaseCubes != 0):
		boardCities[i].startCityPrint();	
'''



#check if game is over
gameIsOver = False;

currentPlayer = 0;

#play the game, next player's turn
while (gameIsOver != True):

	#print board status
	for i in boardCities:
		if (boardCities[i].numDiseaseCubes != 0):
			boardCities[i].startCityPrint();	

	#no. of actions remaining.
	numActions = 3;
	
	#print current Player's stats:
	print(players[currentPlayer].role + 's Turn: ');
	players[currentPlayer].playerPrint();	


	#do this for every action:
	while (numActions > 0):	

		#print no. actions remaining, current City status.
		print("you have " + str(numActions) + " actions remaining");
	
		print("current city stats:");
		for i in boardCities:
			if (players[currentPlayer].position == boardCities[i].name):
				boardCities[i].startCityPrint;
	


		#store available options.
		cityOptions = [];

		#print options to move to cities
		optionIndex = 0;
		for i in boardCities:
			if players[currentPlayer].position in boardCities[i].neighbors:
				print(str(optionIndex) + " - walk to " + boardCities[i].name);
				optionIndex = optionIndex + 1;
				cityOptions.append(boardCities[i]);

		#store option to cure city.
		for i in boardCities:
			if (players[currentPlayer].position == boardCities[i].name and boardCities[i].numDiseaseCubes != 0):
				print(str(optionIndex) + " - cure " + players[currentPlayer].position);
		cityOptions.append("cure");


		#select an option
		playerOption = input("select an option:");	
		nextCity = cityOptions[int(playerOption)];
		
		#if player wants to remove a disease cube
		if nextCity == "cure":
			for i in boardCities:
				if players[currentPlayer].position == boardCities[i].name:
					boardCities[i].numDiseaseCubes = boardCities[i].numDiseaseCubes - 1;
					print(boardCities[i].name + " now has " + str(boardCities[i].numDiseaseCubes) + " disease cubes");	
	
		#if player wants to move to a different city
		else:
			print("you chose " + nextCity.name);

			#move to city.
			players[currentPlayer].position = nextCity.name;
			print("moving to " + players[currentPlayer].position);

		#dec num actions remainng
		numActions = numActions - 1;
	
	#inc current Player, wrap around if necessary
	currentPlayer = currentPlayer + 1;
	if (currentPlayer >= len(players)):
		currentPlayer = currentPlayer - len(players);
	
	#check if there's no disease cubes - if so, players win
	numRemainingCubes = 0;
	for i in boardCities:
		numRemainingCubes = numRemainingCubes + boardCities[i].numDiseaseCubes;
	if (numRemainingCubes == 0):
		print("you eliminated all disease cubes - you win!");
		gameIsOver = True;


'''
#list of edges
#edgesList = [[0 for x in range(len(citiesList))] for y in range(len(citiesList))];

#initalize all edges to 0:
for i in range(len(citiesList)):
	for j in range(len(citiesList)):
		edgesList[i][j] = 0;

#open file w edges
f = open('edges.txt', 'r');
g = open('edges.txt', 'r');

#for detecting when to move to next city
marker = "End" + '\n';

#counters
i_count = 0;
j_count = 0;

#store edges now
#for every city
for i in f:
	i_count = i_count + 1;
	#for every other city
	for j in g:
		j_count = j_count + 1;
		if (i == j):
			continue;
		if (j == marker):
			i = j;
			i = next(f);
			i_count = j_count + 1;
			continue;
		#then these cities have a shared edge
		if (i_count >= len(citiesList) | j_count >= len(citiesList)):
			print("error: i_count is " + i_count + " and j_count is " + j_count);
			continue;
		else:
			edgesList[i_count][j_count] = 1;

for i in citiesList:
	for j in citiesList:
		if (edgesList[i][j] == 1):
			print(citiesList[i] + ' is connected to ' + citiesList[j]);
'''






