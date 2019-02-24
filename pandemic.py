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



#Option - available actions
class Option:
	cure = False;
	city = "Atlanta";
	walk = False;
	direct_flight = False;
	buildResearchStation = False;
	teleportBetweenStations = False;

	#constructor
	def __init__(self, isCure, isCity, isWalk, isCard_Flight, willBuildResearchStation, willTeleport):
		self.cure = isCure;
		self.city = isCity;
		self.walk = isWalk;
		self.direct_flight = isCard_Flight;
		self.buildResearchStation = willBuildResearchStation;
		self.teleportBetweenStations = willTeleport;

#main 
def main():
	return play_pandemic();


#create list of cities
def create_cities(filename):
	citiesList = [];
	f = open(filename, 'r');
	for i in f:
		newCity = i[0:-1];
		citiesList.append(newCity);
	f.close();
	return citiesList;	


#create and initialize edges that exist
def create_edges(citiesList):
	#list of edges
	edgesList = {};

	#initialize all edges to 0
	for i in citiesList:
		for j in citiesList:
			new_key = i + " - " + j;
			edgesList[new_key] = 0;


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
	
	return edgesList;


#play game
#until difficulties are implemented, 
def play_pandemic():

	citiesList = create_cities('cities.txt');

	edgesList = create_edges(citiesList);


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
	random.shuffle(playerCards);


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

	'''
	count = 1;
	for i in players:
		#player_no = i+1;
		#player_no_string = str(player_no);
		i.playerPrint();
		count = count + 1;
	'''


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


	#give each player their starting hand
	if numPlayers == 4:
			numStartingHand = 2;
	elif numPlayers == 3:
			numStartingHand = 3;
	else:
			numStartingHand = 4;

	print("Drawing starting player hands");
	for i in players:
			#print(i.role + " is drawing cards:");
			for j in range(numStartingHand):
					nextPlayerCard = playerCards.pop(0);
					#print("you drew a " + nextPlayerCard + " card");
					i.cards.append(nextPlayerCard);


	#print players' starting info
	for i in players:
		i.playerPrint();


	'''
	#print diseased Cities
	for i in boardCities:
		if (boardCities[i].numDiseaseCubes != 0):
			boardCities[i].startCityPrint();	
	'''



	#check if game is over
	gameIsOver = False;

	#check if players won or lost
	gameWon = False;

	currentPlayer = 0;

	#play the game, next player's turn
	while (gameIsOver != True):

		''' delete this after debugging starting city info
		#print board status
		for i in boardCities:
			if boardCities[i].numDiseaseCubes != 0:
				boardCities[i].startCityPrint();	
			elif boardCities[i].hasResearchCenter == True:
				boardCities[i].startCityPrint();
		'''
		
		#debug
		for i in boardCities:
			boardCities[i].startCityPrint();


		#no. of actions remaining.
		numActions = 4;
		
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
					newOption = Option(False, boardCities[i].name, True, False, False, False);
					cityOptions.append(newOption);

			#store option to cure city.
			for i in boardCities:
				if (players[currentPlayer].position == boardCities[i].name and boardCities[i].numDiseaseCubes != 0):
					print(str(optionIndex) + " - cure " + players[currentPlayer].position);
					optionIndex = optionIndex + 1;
					newOption = Option(True, "Atlanta", False, False, False, False);
					cityOptions.append(newOption);

			#store options for direct flights
			for i in players[currentPlayer].cards:
				print(str(optionIndex) + " - direct flight to " + i);
				newOption = Option(False, i, False, True, False, False);
				cityOptions.append(newOption);
				optionIndex = optionIndex + 1;

			#store option for building a research center
			for i in players[currentPlayer].cards:
				if i == players[currentPlayer].position:
					print(str(optionIndex) + " - build research station in " + i);
					newOption = Option(False, i, False, False, True, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;

			#store options for teleporting a research center
			if boardCities[players[currentPlayer].position].hasResearchCenter == "true":
				for i in boardCities:
					if boardCities[i].hasResearchCenter == "true" and i != players[currentPlayer].position:
						print(str(optionIndex) + " teleport to " + i + " via Research Station");
						newOption = Option(False, i, False, False, False, True);
						cityOptions.append(newOption);
						optionIndex = optionIndex + 1;

			#select an option
			playerOption = input("select an option:");	
			nextOption = cityOptions[int(playerOption)];
			
			#if player wants to remove a disease cube
			if nextOption.cure == True:
				for i in boardCities:
					if players[currentPlayer].position == boardCities[i].name:
						boardCities[i].numDiseaseCubes = boardCities[i].numDiseaseCubes - 1;
						print(boardCities[i].name + " now has " + str(boardCities[i].numDiseaseCubes) + " disease cubes");	
		
			#if player wants to move to a different city
			elif nextOption.walk == True:
				print("you chose " + nextOption.city);

				#move to city.
				players[currentPlayer].position = nextOption.city;
				print("moving to " + players[currentPlayer].position);

			#if player wants to take a direct flight
			elif nextOption.direct_flight == True:
				#fly to city
				players[currentPlayer].position = nextOption.city;
				print("flying to " + players[currentPlayer].position);
				#delete the city card
				for i in players[currentPlayer].cards:
					if nextOption.city == i:
						players[currentPlayer].cards.remove(i);
						print("removed " + players[currentPlayer].position);

			#if player wants to build a research station
			elif nextOption.buildResearchStation == True:
				for i in boardCities:
					if players[currentPlayer].position == boardCities[i].name:
						boardCities[i].hasResearchCenter = "true";
						print("built a research station at " + boardCities[i].name);
				#remove player's card
				for i in players[currentPlayer].cards:
					if i == nextOption.city:
						players[currentPlayer].cards.remove(i);
						print("removed " + players[currentPlayer].position);

			#if player wants to teleport between stations
			elif nextOption.teleportBetweenStations == True:
				players[currentPlayer].position = nextOption.city;

			#dec num actions remainng
			numActions = numActions - 1;
		
		#draw cards from infection deck.
		#structure of cards: draw from beginning of infectionCards deck
		#insert at beginning of infection discard pile
		#did NOT code epidemics yet.
		for i in range(infectionCounter):
			nextInfectedCity = infectionCards.pop(0);
			infectionDiscardPile.insert(0, nextInfectedCity);
			for i in boardCities:
				if boardCities[i].name == nextInfectedCity:
					if boardCities[i].numDiseaseCubes < 3:
						boardCities[i].numDiseaseCubes = boardCities[i].numDiseaseCubes + 1;
						print(boardCities[i].name + " now has " + str(boardCities[i].numDiseaseCubes) + " disease cubes");

		#draw cards from player cards deck. add to hand.
		#draw from beginning of list
		for i in range(2):
			#if the player cards deck is empty
			if not playerCards:
				gameOver = True;
				print("There are no more player cards to draw! Players lose :( ");
				exit;
			nextPlayerCard = playerCards.pop(0);
			print("you drew a " + nextPlayerCard + " card");
			players[currentPlayer].cards.append(nextPlayerCard);

		#if the player has more than 7 cards, discard cards until he/she has 7. 
		while (len(players[currentPlayer].cards) > 7):
			print("you have more than 7 cards - discard until you get to 7.");
			for i in range(len(players[currentPlayer].cards)):
				print("\t" + str(i) + " - " + players[currentPlayer].cards[i]);
			discardOption = int(input("Select a number to discard:")); 
			discardCard = players[currentPlayer].cards[discardOption];
			players[currentPlayer].cards.remove(discardCard);	
			print("you discarded your " + discardCard + " card");

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
			gameWon = True;

	return;		


main();


