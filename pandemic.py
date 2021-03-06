#pandemic.py: The board game pandemic

#for shuffling decks
import random;

#city's colors
blueCities = ["San Francisco", "Chicago", "Montreal", "New York", "Atlanta", "Washington", "Madrid", "London", "Essen", "St. Petersburg", "Paris", "Milan"];

yellowCities = ["Los Angeles", "Mexico City", "Miami", "Bogota", "Lima", "Santiago", "Sao Paolo", "Buenos Aires", "Lagos", "Khartoum", "Kinshasa", "Johannesburg"];

blackCities = ["Moscow", "Tehran", "Istanbul", "Algiers", "Cairo", "Baghdad", "Karachi", "Delhi", "Kolkata", "Riyadh", "Mumbai", "Chennai"];

redCities = ["Beijing", "Seoul", "Shanghai", "Tokyo", "Hong Kong", "Taipei", "Osaka", "Bangkok", "Ho Chi Minh City", "Manila", "Jakarta", "Sydney"];



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
		print("\t" + "research center - " + str(self.hasResearchCenter));
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
			if i in blueCities:
				print("\t\t" + i + " - BLUE");
			elif i in yellowCities:
				print("\t\t" + i + " - YELLOW");
			elif i in blackCities:
				print("\t\t" + i + " - BLACK");
			elif i in redCities:
				print("\t\t" + i + " - RED");
			else:
				print("\t\t" + i);
				


#Option - available actions
class Option:
	cure = False;
	city = "Atlanta";
	walk = False;
	direct_flight = False;
	buildResearchStation = False;
	teleportBetweenStations = False;
	useEvent = False;
	cureBlue = False;
	cureYellow = False;
	cureBlack = False;
	cureRed = False;
	trade = False;
	tradeCard = "Atlanta";
	tradePartner = -1;
	tradeGive = False;
	opExpJump = False

	#constructor
	def __init__(self, isCure, isCity, isWalk, isCard_Flight, willBuildResearchStation, willTeleport, willUseEvent, willCureBlue, willCureYellow, willCureBlack, willCureRed, willTrade, willTradeCard, willTradePartner, willTradeGive, willOpExpJump):
		self.cure = isCure;
		self.city = isCity;
		self.walk = isWalk;
		self.direct_flight = isCard_Flight;
		self.buildResearchStation = willBuildResearchStation;
		self.teleportBetweenStations = willTeleport;
		self.useEvent = willUseEvent;
		self.cureBlue = willCureBlue;
		self.cureYellow = willCureYellow;
		self.cureBlack = willCureBlack;
		self.cureRed = willCureRed;
		self.trade = willTrade;
		self.tradeCard = willTradeCard;
		self.tradePartner = willTradePartner;
		self.tradeGive = willTradeGive;
		self.willOpExpJump = willOpExpJump

'''
#Card - whether Card is an Event or a City Card
#class Card:
	isCity = True;
	CityName = 
'''



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


#performs outbreak
def outbreak(city, numOutbreaks, boardCities, alreadyOutbreaked, currentPlayer, players, blueCured, blueCities, yellowCured, yellowCities, blackCured,blackCities,  redCured, redCities):
	
	#print
	print(str(numOutbreaks+1) + "th outbreak in " + city.name + "!");
	
	#global list of cities w/ outbreak this turn to prevent inf loop.
	alreadyOutbreaked.append(city);

	#inc. numOutbreaks, set city's numDiseaseCubes to 3
	#if this is eighth outbreak, players lose.
	numOutbreaks += 1;
	if (numOutbreaks == 8):
		print("Eighth outbreak has occured. Players lose :( ");
		exit();

	'''
	for i in boardCities:
		if boardCities[i].name == nextInfectedCity:
			boardCities[i].numDiseaseCubes = 3;
	'''

	#iter through outbreak'd cities' neighbors, if numCubes = 3, recursively call outbreak. else, inc. numCubes.
	#keep global list of cities so that it doesn't inf. loop
	for i in city.neighbors:
		if boardCities[i] in alreadyOutbreaked:
			continue;
		#dont outbreak/increase disease cube if current player is Medic and disease is cured
		elif medicSaveInfection(players, i, blueCured, blueCities, yellowCured, yellowCities, redCured, redCities, blackCured, blackCities) == False:
			if boardCities[i].numDiseaseCubes == 3:
				numOutbreaks = outbreak(boardCities[i], numOutbreaks, boardCities, alreadyOutbreaked, currentPlayer, players, blueCured, blueCities, yellowCured, yellowCities, blackCured, blackCities, redCured, redCities);
			else:
				boardCities[i].numDiseaseCubes += 1;
				print(boardCities[i].name + " now has " + str(boardCities[i].numDiseaseCubes) + " disease cubes due to outbreak");
	return numOutbreaks;

#choose_city - asks players for any city to travel to/place research center in using GOV GRANT/travel to if player is OP EXPERT.
#this is repeated many times, so I made it a fn.
def choose_city(citiesList):
	#debug
	city_count = 0;
	print("choose a city: ");
	for i in citiesList:
		print(str(city_count) + " - " + str(i));
		city_count = city_count + 1;
	cityOption = input("select an option:");
	return int(cityOption);


#medic_save: returns true if medic prevents disease cube from landing on city, false if otherwise
def medicSaveInfection(players, nextInfectedCity, curedBlue, blueCities, curedYellow, yellowCities, curedBlack, blackCities, curedRed, redCities):
	for iter_player in players:
		if iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedBlue == True and nextInfectedCity in blueCities:
			return True
		elif iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedYellow == True and nextInfectedCity in yellowCities:
			return True
		elif iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedBlack == True and nextInfectedCity in blackCities:
			return True
		elif iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedRed == True and nextInfectedCity in redCities:
			return True
	return False


def discardCard(players, currentPlayer, blueCities, yellowCities, blackCities, redCities):
		for i in range(len(players[currentPlayer].cards)):
			if players[currentPlayer].cards[i] in blueCities:
				print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - BLUE");
			elif players[currentPlayer].cards[i] in yellowCities:
				print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - YELLOW");
			elif players[currentPlayer].cards[i] in blackCities:
				print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - BLACK");
			elif players[currentPlayer].cards[i] in redCities:
				print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - RED");
			else:
				print("\t" + str(i) + " - " + players[currentPlayer].cards[i]);
		discardOption = int(input("Select a number to discard:")); 
		discardCard = players[currentPlayer].cards[discardOption];
		players[currentPlayer].cards.remove(discardCard);	
		print("you discarded your " + discardCard + " card");


#play game
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
	#random.shuffle(playerCards);


	#epidemic cards - rt now it's just randomly shuffled
	#fix this later so it becomes more evenly distributed
	#short-term fix - add epidemic cards after dealing player cards out.
	'''
	epidemicCard = "EPIDEMIC";
	difficulty = 4;	
	while (difficulty > 0):
		playerCards.append(epidemicCard);
		difficulty = difficulty - 1;
	random.shuffle(playerCards);
	'''


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
			new_city.hasResearchCenter = True;
		else:
			new_city.hasResearchCenter = False;
		for j in citiesList:
			#if not short term fix
			if j == "EPIDEMIC" or j == "GOVERNMENT GRANT":
				continue;
			search_string = i + " - " + j;
			if (edgesList[search_string] == 1):
				new_city.neighbors.append(j);
		boardCities[i] = new_city;

	#debug
	citiesList = playerCards;
	random.shuffle(playerCards);


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

	#let players choose their roles.
	counter = 0;
	takenIndices = [];
	while counter < numPlayers:
		for i in range(len(character_roles)):
			if i not in takenIndices:
				print(str(i) + " - " + character_roles[i]);
		nextRole = int(input("PLAYER " + str(counter) + ": PICK YOUR ROLE"));
		takenIndices.append(nextRole);
		counter = counter + 1;
		new_player = Player(character_roles[nextRole]);
		players.append(new_player);



	'''
	#this randomly assigns player roles
	counter = 0;
	while (counter < numPlayers):
		role = random.choice(character_roles);
		character_roles.remove(role);
		new_player = Player(role);
		players.append(new_player);
		counter = counter + 1;
	'''


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

	#debug - test if trading works
	#uncomment this if trading works
	playerCards.insert(0, "Atlanta");

	print("Drawing starting player hands");
	for i in players:
			#print(i.role + " is drawing cards:");
			for j in range(numStartingHand):
					nextPlayerCard = playerCards.pop(0);
					#print("you drew a " + nextPlayerCard + " card");
					i.cards.append(nextPlayerCard);

	eventCardList = ["ONE QUIET NIGHT", "FORECAST", "AIRLIFT", "GOVERNMENT GRANT", "RESILIENT POPULATION"];

	#between dealing starting hands and putting in epidemics, we'll insert the
	#event cards.
	for i in eventCardList:
		playerCards.append(i);
	random.shuffle(playerCards);


	#ok, so NOW we put in the epidemic cards
	#rt now it's just randomly shuffled
	#fix this later so it becomes more evenly distributed
	#later ask players for difficulty
	epidemicCard = "EPIDEMIC";

	#ask for no. of epidemic cards
	difficulty = int(input("how many epidemic cards in play? (4, 5, or 6 please)"));
	
	#length of each sub pile - for setting up epidemic cards
	subPileLength = int(len(playerCards) / (difficulty + 1));
	print("each sub pile will have length " + str(subPileLength));
	
	#will have the size of each sub pile - for placing epidemic cards
	subPileLengthArray = [];
	for i in range(difficulty + 1):
		subPileLengthArray.append(subPileLength);

	#in case no. of playerCards doesn't divide no. of sub piles nicely
	subPileIter = 0;
	count = 0;
	while True:
		count = 0;
		for i in subPileLengthArray:
			count += i;
		if count < len(playerCards):
			subPileLengthArray[subPileIter] += 1;
			subPileIter += 1;
		else:
			break;

	'''
	#debug
	print("length of each sub pile:");
	for i in subPileLengthArray:
		print(i);
	'''

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

	#number of outbreaks
	numOutbreaks = 0;

	#cured diseases
	numCuredDiseases = 0;
	blueCured = False;
	yellowCured = False;
	blackCured = False;
	redCured = False;

	#player cards discard pile
	playerDiscardPile = []

	#check if trade works - comment this later
	#playerCards.insert(0, "Atlanta");


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
		#testing for epidemic cards
		for i in boardCities:
			if (boardCities[i].numDiseaseCubes != 0 or boardCities[i].hasResearchCenter == True):
				boardCities[i].startCityPrint();


		#no. of actions remaining.
		numActions = 4;
		
		#print current Player's stats:
		print(players[currentPlayer].role + 's Turn: ');
		players[currentPlayer].playerPrint();	

		#re-set counter for ONE QUIET NIGHT card
		skipInfections = False;

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

			#print options to walk to nearby cities
			optionIndex = 0;
			for i in boardCities:
				if players[currentPlayer].position in boardCities[i].neighbors:
					print(str(optionIndex) + " - walk to " + boardCities[i].name);
					optionIndex = optionIndex + 1;
					newOption = Option(False, boardCities[i].name, True, False, False, False, False, False, False, False, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);

			#store option to cure city.
			for i in boardCities:
				if (players[currentPlayer].position == boardCities[i].name and boardCities[i].numDiseaseCubes != 0):
					print(str(optionIndex) + " - cure " + players[currentPlayer].position);
					optionIndex = optionIndex + 1;
					newOption = Option(True, "Atlanta", False, False, False, False, False, False, False, False, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);

			#store options for direct flights, Op Expert can fly anywhere if at a research center
			if players[currentPlayer].role == 'Operations Expert' and boardCities[players[currentPlayer].position].hasResearchCenter == True:
				print(str(optionIndex) + " - jump using Research Center")
				optionIndex += 1
				newOption = Option(False, "Atlanta", False, False, False, False, False, False, False, False, False, False, "Atlanta", -1, False, True)
				cityOptions.append(newOption)
			for i in players[currentPlayer].cards:
				if i not in eventCardList:
					print(str(optionIndex) + " - direct flight to " + i);
					newOption = Option(False, i, False, True, False, False, False, False, False, False, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;

			#store option for building a research center
			#if player is Operations Expert, doesn't need to discard card
			if players[currentPlayer].role == 'Operations Expert':
				print(str(optionIndex) + " - build research station in " + players[currentPlayer].position + " w/o card - Operations Expert")
				newOption = Option(False, "OP EXPERT EFFECT", False, False, True, False, False, False, False, False, False, False, "Atlanta", -1, False, False)
				cityOptions.append(newOption)
				optionIndex += 1

			for i in players[currentPlayer].cards:
				if i == players[currentPlayer].position:
					print(str(optionIndex) + " - build research station in " + i);
					newOption = Option(False, i, False, False, True, False, False, False, False, False, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;

			#store options for teleporting between research centers
			if boardCities[players[currentPlayer].position].hasResearchCenter == True:
				for i in boardCities:
					if boardCities[i].hasResearchCenter == True and i != players[currentPlayer].position:
						print(str(optionIndex) + " teleport to " + i + " via Research Station");
						newOption = Option(False, i, False, False, False, True, False, False, False, False, False, False, "Atlanta", -1, False, False);
						cityOptions.append(newOption);
						optionIndex = optionIndex + 1;

			#store options for using event cards
			for i in players[currentPlayer].cards:
				if i in eventCardList:
					print(str(optionIndex) + " - use " + i + " event card.");
					newOption = Option(False, i, False, False, False, False, True, False, False, False, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;		
	
			#store options for curing diseases
			#if player is DOCTOR, only needs 4 cards of same color
			if boardCities[players[currentPlayer].position].hasResearchCenter == True:
				numBlueCards = 0;
				numYellowCards = 0;
				numBlackCards = 0;
				numRedCards = 0;
				for i in players[currentPlayer].cards:
					if i in blueCities:
						numBlueCards = numBlueCards + 1;
					elif i in yellowCities:
						numYellowCards = numYellowCards + 1;
					elif i in blackCities:
						numBlackCards = numBlackCards + 1;
					elif i in redCities:
						numRedCards = numRedCards + 1;
				if numBlueCards >= 5 or (numBlueCards == 4 and players[currentPlayer].role == "Scientist"):
					print(str(optionIndex) + " - cure BLUE disease");
					newOption = Option(False, i, False, False, False, False, False, True, False, False, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;
				elif numYellowCards >= 5 or (numYellowCards == 4 and players[currentPlayer].role == "Scientist"):
					print(str(optionIndex) + " - cure YELLOW disease");
					newOption = Option(False, i, False, False, False, False, False, False, True, False, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;
				elif numBlackCards >= 5 or (numBlackCards == 4 and players[currentPlayer].role == "Scientist"):
					print(str(optionIndex) + " - cure BLACK disease");
					newOption = Option(False, i, False, False, False, False, False, False, False, True, False, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;
				elif numRedCards >= 5 or (numRedCards == 4 and players[currentPlayer].role == "Scientist"):
					print(str(optionIndex) + " - cure RED disease");
					newOption = Option(False, i, False, False, False, False, False, False, False, False, True, False, "Atlanta", -1, False, False);
					cityOptions.append(newOption);
					optionIndex = optionIndex + 1;
			
			#store options for trading cards
			for i in range(numPlayers):
				if i == currentPlayer:
					continue;
				if players[i].position == players[currentPlayer].position:
					for j in players[i].cards:
						if j == players[i].position or players[i].role == 'Researcher':
							print(str(optionIndex) + " - take " + j + " card from player " + str(i) + " - " + players[i].role);
							newOption = Option(False, i, False, False, False, False, False, False, False, False, False, True, j, i, False, False);
							cityOptions.append(newOption);
							optionIndex = optionIndex + 1;
					for j in players[currentPlayer].cards:
						if j == players[i].position or players[currentPlayer].role == 'Researcher':
							print(str(optionIndex) + " - give " + j + " card to player " + str(i) + " - " + players[i].role);
							newOption = Option(False, i, False, False, False, False, False, False, False, False, False, True, j, i, True, False);
							cityOptions.append(newOption);
							optionIndex = optionIndex + 1;
	

			#select an option
			playerOption = input("select an option:");	
			nextOption = cityOptions[int(playerOption)];
			if nextOption.cureBlue == True or nextOption.cureYellow == True or nextOption.cureBlack == True or nextOption.cureRed == True:
				print("curing a disease!");		
	
			#if player wants to remove a disease cube
			if nextOption.cure == True:
				for i in boardCities:
					if players[currentPlayer].position == boardCities[i].name:
						if players[currentPlayer].position in blueCities and blueCured == True:
							boardCities[i].numDiseaseCubes = 0;
						elif players[currentPlayer].position in yellowCities and yellowCured == True:
							boardCities[i].numDiseaseCubes = 0;
						elif players[currentPlayer].position in blackCities and blackCured == True:
							boardCities[i].numDiseaseCubes = 0;
						elif players[currentPlayer].position in redCities and redCured == True:
							boardCities[i].numDiseaseCubes = 0;
						elif players[currentPlayer].role == "Medic":
							print("Medic special ability: removes all disease cubes for current city");
							boardCities[i].numDiseaseCubes = 0;
						else:
							boardCities[i].numDiseaseCubes = boardCities[i].numDiseaseCubes - 1;
						print(boardCities[i].name + " now has " + str(boardCities[i].numDiseaseCubes) + " disease cubes");
		
			#if player wants to walk to nearby city
			elif nextOption.walk == True:
				print("you chose " + nextOption.city);
				players[currentPlayer].position = nextOption.city;
				print("moving to " + players[currentPlayer].position);
				#if player is medic, then remove any disease cubes if cure has been discovered
				for i in boardCities:
					if players[currentPlayer].position == boardCities[i].name:
						if boardCities[i].numDiseaseCubes != 0 and boardCities[i].name in blueCities and blueCured == True:
							print("Medic special ability: walking through blue city and blue disease cured, so automatically removes disease cubes!");
							boardCities[i].numDiseaseCubes = 0;
						elif boardCities[i].numDiseaseCubes != 0 and boardCities[i].name in yellowCities and yellowCured == True:
							print("Medic special ability: walking through yellow city and yellow disease cured, so automatically removes disease cubes!");
							boardCities[i].numDiseaseCubes = 0;
						elif boardCities[i].numDiseaseCubes != 0 and boardCities[i].name in blackCities and blackCured == True:
							print("Medic special ability: walking through black city and black disease cured, so automatically removes disease cubes!");
							boardCities[i].numDiseaseCubes = 0;	
						elif boardCities[i].numDiseaseCubes != 0 and boardCities[i].name in redCities and redCured == True:
							print("Medic special ability: walking through red city and red disease cured, so automatically removes disease cubes!");
							boardCities[i].numDiseaseCubes = 0;

			#if player wants to take a direct flight
			elif nextOption.direct_flight == True:
				#fly to city
				players[currentPlayer].position = nextOption.city;
				print("flying to " + players[currentPlayer].position);
				#delete the city card
				for i in players[currentPlayer].cards:
					if nextOption.city == i:
						playerDiscardPile.insert(0, i);
						players[currentPlayer].cards.remove(i);
						print("removed " + players[currentPlayer].position);

			#if player wants to build a research station
			elif nextOption.buildResearchStation == True:
				for i in boardCities:
					if players[currentPlayer].position == boardCities[i].name:
						boardCities[i].hasResearchCenter = True;
						print("built a research station at " + boardCities[i].name);
				#remove player's card - Op Expert doesn't discard a card
				if nextOption.city != 'OP EXPERT EFFECT':
					for i in players[currentPlayer].cards:
						if i == nextOption.city:
							playerDiscardPile.insert(0, i);
							players[currentPlayer].cards.remove(i);
							print("removed " + players[currentPlayer].position);

			#if player wants to teleport between stations
			elif nextOption.teleportBetweenStations == True:
				players[currentPlayer].position = nextOption.city;

			#if player wants to use an event Card
			elif nextOption.useEvent == True:
				#print("playing one quiet night card.");
				if nextOption.city == "ONE QUIET NIGHT":
					print("identified card as ONE QUEIT NIGHT. skipInfections is now true.");
					skipInfections = True;
				elif nextOption.city == "GOVERNMENT GRANT":
					#print("not the one quiet night card tho...");
					print("identified card as government grant.");
					citiesList = create_cities('cities.txt');
					cityOption = choose_city(citiesList);
					print("putting research center in " + citiesList[cityOption]);
					boardCities[citiesList[cityOption]].hasResearchCenter = True;
					print("research center placed in " + citiesList[cityOption]);
			
				#AIRLIFT EVENT CARD
				elif nextOption.city == "AIRLIFT":
					print("identified card as airlift.");
					citiesList = create_cities('cities.txt');
					cityOption = choose_city(citiesList);
					players[currentPlayer].position = citiesList[cityOption];
					print("player's current position is now " + players[currentPlayer].position);
				
				#RESILIENT POPULATION
				elif nextOption.city == "RESILIENT POPULATION":
					print("playing RESILIENT POPULATION card...");
					print("select a card from the infection Discard Pile to discard: ");
					infectionDiscardPileCounter = 0;
					for i in infectionDiscardPile:
						print(str(infectionDiscardPileCounter) + " - " + i);
						infectionDiscardPileCounter = infectionDiscardPileCounter + 1;
					infectionPileChoice = input("Select a city to remove: ");
					infectionDiscardPile.remove(infectionDiscardPile[int(infectionPileChoice)]);
					#debug
					print("here are the new contents of the infection Discard Pile: ");
					for i in infectionDiscardPile:
						print(i);	
					
				#FORECAST
				elif nextOption.city == "FORECAST":
					print("playing FORECAST card...");
					print("here are the top 6 cards of the infection Deck:");
					#draw from beginning (top) of infectionCards
					#insert in beginning (top) of forecast pile
					forecast_pile = [];
					for i in range(6):
						nextCard = infectionCards.pop(0);
						print("next card: " + nextCard);
						forecast_pile.insert(0, nextCard);
					for i in range(6):
						print("pick which card you want to go on top of infection Deck next: ");
						forecast_counter = 0;
						for j in forecast_pile:
							print(str(forecast_counter) + " - " + j);
							forecast_counter = forecast_counter + 1;
						forecast_choice = int(input("pick the next city card to go on top of the infection deck:"));
						nextInfectionCard = forecast_pile[forecast_choice];
						forecast_pile.remove(forecast_pile[forecast_choice]);
						infectionCards.insert(0, nextInfectionCard);

				#delete the event card
				for i in players[currentPlayer].cards:
					if nextOption.city == i:
						playerCardDiscardPile.insert(0, i);
						players[currentPlayer].cards.remove(i);
				
				#event cards dont take up an action
				numActions = numActions + 1;		
	

			#To cure diseases
			#cure blue disease
			elif nextOption.cureBlue == True:
				print("curing blue disease");
				removeBlue = 0;
				removeList = [];
				for i in players[currentPlayer].cards:
					if i in blueCities and removeBlue < 5:
						removeList.append(i);
						removeBlue = removeBlue + 1;
				for i in removeList:
					playerCardDiscardPile.insert(0, i);
					players[currentPlayer].cards.remove(i);
				blueCured = True;
				numCuredDiseases = numCuredDiseases + 1;
				if numCuredDiseases == 4:
					print("Players discovered cures for all 4 diseases! Game Won!");

			#cure yellow disease
			elif nextOption.cureYellow == True:
				print("curing yellow disease");
				removeYellow = 0;
				removeList = [];
				for i in players[currentPlayer].cards:
					if i in yellowCities and removeYellow < 5:
						removeList.append(i);
						removeYellow = removeYellow + 1;
				for i in removeList:
					playerCardDiscardPile.insert(0, i);
					players[currentPlayer].cards.remove(i);
				yellowCured = True;
				numCuredDiseases = numCuredDiseases + 1;
				if numCuredDiseases == 4:
					print("Players discovered cures for all 4 diseases! Game Won!");
			
			#cure black disease
			elif nextOption.cureBlack == True:
				print("curing black disease.");
				removeBlack = 0;
				removeList = [];
				for i in players[currentPlayer].cards:
					if i in blackCities and removeBlack < 5:
						removeList.append(i);
						removeBlack = removeBlack + 1;
				for i in removeList:
					playerCardDiscardPile.insert(0, i);
					players[currentPlayer].cards.remove(i);
				blackCured = True;
				numCuredDiseases = numCuredDiseases + 1;
				if numCuredDiseases == 4:
					print("Players discovered cures for all 4 diseases! Game Won!");

			#cure red disease
			elif nextOption.cureRed == True:
				print("curing red disease");
				removeRed = 0;
				removeList = [];
				for i in players[currentPlayer].cards:
					if i in redCities and removeRed < 5:
						removeList.append(i);
						removeRed = removeRed + 1;
				for i in removeList:
					playerCardDiscardPile.insert(0, i);
					players[currentPlayer].cards.remove(i);
				redCured = True;
				numCuredDiseases = numCuredDiseases + 1;
				if numCuredDiseases == 4:
					print("Players discovered cures for all 4 diseases! Game Won!");

			#if player wants to trade
			elif nextOption.trade == True:
				#if player wants to give card to another player
				if nextOption.tradeGive == True:
					players[nextOption.tradePartner].cards.insert(0, nextOption.tradeCard);
					players[currentPlayer].cards.remove(nextOption.tradeCard);
				#if player wants to take a card from another player
				elif nextOption.tradeGive == False:
					players[currentPlayer].cards.insert(0, nextOption.tradeCard);
					players[nextOption.tradePartner].cards.remove(nextOption.tradeCard);

			#if Operations Expert wants to jump from Research Center
			elif nextOption.opExpJump == True:
				players[currentPlayer].position = choose_city(citiesList)
				print("Operation Expert is jumping to " + players[currentPlayer].position)
				print("Now discard a card:")
				discardCard(players, currentPlayer, blueCities, blackCities, yellowCities, redCities)
				'''	
				for i in players[currentPlayer].cards:
					if nextOption.city == i:
						players[currentPlayer].cards.remove(i);
				'''	


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
			#if its an epidemic card
			if nextPlayerCard == "EPIDEMIC":
				
				#1. decrement free epidemic counter, possibly increment infection Counter
				# NOTE: this will only work for 4-6 epidemic cards only!
				totalEpidemicsOccured = totalEpidemicsOccured + 1;
				numFreeEpidemicMoves = numFreeEpidemicMoves - 1;
				print("performing " + str(totalEpidemicsOccured) + "th epidemic");
				if (infectionCounter == 2 and numFreeEpidemicMoves == 0):
					infectionCounter = 3;
					numFreeEpidemicMoves = 2;
					print("infection counter now at 3!");
				elif (infectionCounter == 3 and numFreeEpidemicMoves == 0):
					infectionCounter = 4;
					numFreeEpidemicMoves = -1;
					print("infection counter now at 4!");
				print("we are at infection Counter " + str(infectionCounter) + " with " + str(numFreeEpidemicMoves) + " free epidemics");
				
				#2. infect city at bottom of infection cards deck
				nextInfectedCity = infectionCards.pop();
				print("Drew an Epidemic - Epidemic in " + nextInfectedCity + ":(");
				
				'''
				medicSaveInfection = False
				for iter_player in players:
					if iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedBlue == True and nextInfectedCity in blueCities:
						medicSaveInfection = True
					elif iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedYellow == True and nextInfectedCity in yellowCities:
						medicSaveInfection = True
					elif iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedBlack == True and nextInfectedCity in blackCities:
						medicSaveInfection = True
					elif iter_player.role == 'Medic' and iter_player.position == nextInfectedCity and curedRed == True and nextInfectedCity in redCities:
						medicSaveInfection = True
				'''
				if medicSaveInfection(players, nextInfectedCity, blueCured, blueCities, yellowCured, yellowCities, blackCured, blackCities, redCured, redCities) == False:
					boardCities[nextInfectedCity].numDiseaseCubes = boardCities[nextInfectedCity].numDiseaseCubes + 3;
					if boardCities[nextInfectedCity].numDiseaseCubes > 3:
						boardCities[nextInfectedCity].numDiseaseCubes = 3;
						numOutbreaks = outbreak(boardCities[nextInfectedCity], numOutbreaks, boardCities, [], players[currentPlayer], players, blueCured, blueCities, yellowCured, yellowCities, blackCured, blackCities, redCured, redCities);
				else:
					print("Medic prevented epidemic in " + nextInfectedCity)
	
				#3. re-shuffle epidemic'd city card into infection discard pile, shuffle discards, and put at top of infection deck
				infectionDiscardPile.insert(0, nextInfectedCity);
				random.shuffle(infectionDiscardPile);
				while infectionDiscardPile:
					moveToInfectionDeck = infectionDiscardPile.pop(0);
					infectionCards.insert(0, moveToInfectionDeck);

			#normal playing card - not epidemic.
			else:
				print("you drew a " + nextPlayerCard + " card");
				players[currentPlayer].cards.append(nextPlayerCard);
		
	
		#if player didn't play ONE QUIET NIGHT card,
		#draw cards from infection deck.
		#structure of cards: draw from beginning of infectionCards deck
		#insert at beginning of infection discard pile
		print("skipInfections is now " + str(skipInfections));
		if skipInfections == False:
			i = 0;
			for i in range(infectionCounter):
				nextInfectedCity = infectionCards.pop(0);
				#print("drew " + nextInfectedCity " from infection Deck");
				infectionDiscardPile.insert(0, nextInfectedCity);
				#this if causes issues when there are epidemics but no outbreaks - uncomment for now.
				#if boardCities[j].numDiseaseCubes < 3:
				
				'''
				#if theres a medic and disease is cured, then dont put a disease cube
				for currentPlayer in players:
					if currentPlayer.role == "Medic" and currentPlayer.position == boardCities[j].name:
						if boardCities[j].name in blueCities and blueCured == True:
				'''
				#medic save
				if medicSaveInfection(players, nextInfectedCity, blueCured, blueCities, yellowCured, yellowCities, blackCured, blackCities, redCured, redCities) == False:
					if (boardCities[nextInfectedCity].numDiseaseCubes == 3):
						print("outbreak in " + boardCities[nextInfectedCity].name + "!");
						numOutbreaks = outbreak(boardCities[nextInfectedCity], numOutbreaks, boardCities, [], players[currentPlayer], players, blueCured, blueCities, yellowCured, yellowCities, blackCured, blackCities, redCured, redCities);
					else:
						boardCities[nextInfectedCity].numDiseaseCubes = boardCities[nextInfectedCity].numDiseaseCubes + 1;
						print(boardCities[nextInfectedCity].name + " now has " + str(boardCities[nextInfectedCity].numDiseaseCubes) + " disease cubes");


		#if the player has more than 7 cards, discard cards until he/she has 7. 
		while (len(players[currentPlayer].cards) > 7):
			print("you have more than 7 cards - discard until you get to 7.");
			discardCard(players, currentPlayer, blueCities, yellowCities, blackCities, redCities)
			'''
			for i in range(len(players[currentPlayer].cards)):
				if players[currentPlayer].cards[i] in blueCities:
					print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - BLUE");
				elif players[currentPlayer].cards[i] in yellowCities:
					print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - YELLOW");
				elif players[currentPlayer].cards[i] in blackCities:
					print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - BLACK");
				elif players[currentPlayer].cards[i] in redCities:
					print("\t" + str(i) + " - " + players[currentPlayer].cards[i] + " - RED");
				else:
					print("\t" + str(i) + " - " + players[currentPlayer].cards[i]);
			discardOption = int(input("Select a number to discard:")); 
			discardCard = players[currentPlayer].cards[discardOption];
			players[currentPlayer].cards.remove(discardCard);	
			print("you discarded your " + discardCard + " card");
			'''
	
		#inc current Player, wrap around if necessary
		currentPlayer = currentPlayer + 1;
		if (currentPlayer >= len(players)):
			currentPlayer = currentPlayer - len(players);
		
		'''
		#this should be removed - only useful for early version of game
		#check if there's no disease cubes - if so, players win
		numRemainingCubes = 0;
		for i in boardCities:
			numRemainingCubes = numRemainingCubes + boardCities[i].numDiseaseCubes;
		if (numRemainingCubes == 0):
			print("you eliminated all disease cubes - you win!");
			gameIsOver = True;
			gameWon = True;
		'''	

	return;		


main();


