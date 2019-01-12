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
	citiesList.append(i);

#works
#for i in citiesList:
#	print(i);

print(len(citiesList));












