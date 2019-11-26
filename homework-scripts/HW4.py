'''
------ HW4 ------
Due date: 15.03.2019 09:00

------ Part I 10% ------
Write a function that takes a list in the format below (old_list) and returns a list in a new format (new_list)

old_list = ['EcoRI,GAATTC', 'XbaI,TCTAGA', 'EcoRV,GATATC', 'DpnI,GATC', 'SmaI,CCCGGG']
new_list =[['EcoRI', 'GAATTC'], ['XbaI', 'TCTAGA'], ['EcoRV', 'GATATC'], ['DpnI', 'GATC'], ['SmaI', 'CCCGGG']]

------ Part II 10% ------
Write a function that takes a list in the format below (old_new_list) and returns a list in a new format (new_old_list)

old_new_list =[['EcoRI', 'GAATTC'], ['XbaI', 'TCTAGA'], ['EcoRV', 'GATATC'], ['DpnI', 'GATC'], ['SmaI', 'CCCGGG']]
new_old_list = ['EcoRI,GAATTC', 'XbaI,TCTAGA', 'EcoRV,GATATC', 'DpnI,GATC', 'SmaI,CCCGGG']

------ Part III 20% ------
Write a function that takes a list in the format below (old_list) and turns it into a dictionary with the following
format

old_list = ['EcoRI,GAATTC', 'XbaI,TCTAGA', 'EcoRV,GATATC', 'DpnI,GATC', 'SmaI,CCCGGG']
new_dict = {'EcoRI' : 'GAATTC', 'XbaI' : 'TCTAGA', 'EcoRV' : 'GATATC', 'DpnI' : 'GATC', 'SmaI' : 'CCCGGG'}

----- Part IV 40% ------
Write a function that will take the name, sex, age, marital status and number of children of several individuals and
returns a dictionary with the keys outlined in example output.

Example input:
peeps_list = [
				['Hakki Bulut', 'M', 36, 'married', 1],
				['Nadide Cicek, 'F', 65, 'divorced', 2],
		        ['Luigi Tenco, 'M', 29, 'single', 0]
		     ]

peeps_dict = {
			  'Bulut' : {'Name' : 'Bulut', 'sex' : 'M', 'age' : 36, 'children' : 1},
			  'Cicek' : {'Name' : 'Nadide', 'sex' : 'F', 'age' : 65, 'children' : 2},
			  'Tenco' : {'Name' : 'Luigi', 'sex' : 'M', 'age' : 29, 'children' : 0}
			  }

------ Part V 40% ------
Write a function that will take the peeps_dict and change it to peeps_list in Part IV and return the list.
'''

old_list = ['EcoRI,GAATTC', 'XbaI,TCTAGA', 'EcoRV,GATATC', 'DpnI,GATC', 'SmaI,CCCGGG']
new_list = [['EcoRI', 'GAATTC'], ['XbaI', 'TCTAGA'], ['EcoRV', 'GATATC'], ['DpnI', 'GATC'], ['SmaI', 'CCCGGG']]


def old_to_new_list(old_list):
	rv = []
	for elem in old_list:
		name, seq = elem.split(',')
		rv.append([name, seq])
	return rv


def new_to_old_list(new_list):
	rv = []
	for elem in new_list:
		rv.append(','.join(elem))
	# name, seq = elem
	# rv.append(f'{name},{seq}')
	return rv


def list_to_dict(old_list):
	rv = {}
	for elem in old_list:
		name, seq = elem.split(',')
		rv[name] = seq
	return rv


def peeps_list_to_dict(a_list):
	rv = {}
	for elem in a_list:
		name, surname = elem[0].split(' ')
		sex, age, marital_stat, kids = elem[1], elem[2], elem[3], elem[4]
		rv[surname] = {'Name': name, 'sex': sex, 'age': age, 'children' : kids }
	return rv


def peeps_dict_to_list(a_dict):
	rv = []
	for surname in a_dict:
		name = a_dict[surname]['name']
		sex = a_dict[surname]['sex']
		age = a_dict[surname]['age']
		children = a_dict[surname]['children']
		# name_surname = name + ' ' + surname
		name_surname = f'{name} {surname}'
		rv.append([name_surname, sex, age, children])
	return rv




