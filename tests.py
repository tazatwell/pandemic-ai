#tests.py: unit testing w Travis CI
#using py.test framework

import pandemic;
import Test_values;



#test if creating cities correctly w sample of cities
def t1_create_cities(filename):
	ans_citiesList = Test_values.Test_values.ans_citiesList;		
	test_create_cities = pandemic.create_cities(filename);
	if ans_citiesList == test_create_cities:
		print("t1_create_cities test: ...PASSED");
		return True;
	else:
		print("t1_create_cities test: ...FAILED");
		return False;


#run tests
t1_create_cities('t_cities.txt');

#pandemic.main();

