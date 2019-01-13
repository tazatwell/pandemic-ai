#pandemic.py: The board game pandemic

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

	#class constructor
	def _init_(self, new_name, new_color, new_neighbors):
		self.name = new_name;
		self.color = new_color;
		self.neighbors = new_neighbors;
	
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
		print("there's an edge between " + i);
print("number of directed edges is " + str(numEdges));
print("number of bidirectional edges is " + str(numEdges/2));

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






