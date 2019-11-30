# Copyright SYS113 2019. MIT license , see readme file.

# import librarys ...

from tzlocal import get_localzone
from datetime import datetime
from platform import system , release , machine
from getpass import getuser
from os.path import isfile
from time import tzname , daylight
from inspect import getframeinfo , stack

# create log function ...

def log(text=None,save=None,size=None):

	# find (filename or line) python file ...

	x = stack()[1]
	x = x[0]
	get_log_file_python_file_name_or_line = getframeinfo(x)

	# -----------------------------------------------------------------------------------------------------------------------------------------------------------
	'''                                                    
													'find line in python file' variable is 'line_python_file'
													'find python file name' variable is 'python_file'
													'save log in a file' variable is 'log_file'
													'log text' variable is 'log_text'
													'set log file size' variable is 'log_file_size'
	'''
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------

	# set valur for find line in python file ...

	line_python_file = str(get_log_file_python_file_name_or_line.lineno)

	# set value for find python file name ...

	python_file_name = str(get_log_file_python_file_name_or_line.filename)

	if python_file_name == '<stdin>':
		python_file = 'interpreter'
	elif len(python_file_name) < 18:
		python_file = python_file_name
	elif len(python_file_name) > 18:
		print('negar module - error | python file : '+python_file_name+' | line : '+line_python_file+' | problem : maximum size of python file name is 15 character ...')
		return

	# set value for save log in a file ...

	if type(save) == str:
		log_file = save
	elif save == None:
		log_file = 'log.txt'
	elif type(save) != str:
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'save\' type is not str ...')
		return

	# set value for log text ...

	if text == None:
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'text\' value is empty ...')
		return
	elif text == '':
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'text\' value is empty ...')
		return
	elif type(text) != str:
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'text\' type is not str ...')
		return
	elif type(text) == str:
		log_text = text

	# set value for log file size ...

	if size == None:
		log_size = 2
	elif type(size) != int:
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size\' type is not str ...')
		return
	elif size > 5:
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size\' value range is not (1 ... 5) ...')
		return
	elif size == 0:
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size\' value is not in range (1 ... 5) ...')
		return
	elif type(size) == int:
		log_size = size

	# -----------------------------------------------------------------------------------------------------------------------------------------------------------
	'''
													'write python file name in log file' variable is 'log_file_python_file_name'
													'write line of python file in log file' variable is 'log_file_python_file_line'
													'write log text in log file' variable is 'log_file_text'
													'log file name' variable is 'log_file_name'
													'log file size' variable is 'log_file_size'
	'''
	# -----------------------------------------------------------------------------------------------------------------------------------------------------------

	# check cheacter size ...

	if (log_size == 1) and (len(log_text) > 69):
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size = 1\' maximum 69 character support ...')
		return
	elif (log_size == 2) and (len(log_text) > 93):
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size = 2\' maximum 93 character support ...')
		return
	elif (log_size == 3) and (len(log_text) > 131):
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size = 3\' maximum 131 character support ...')
		return
	elif (log_size == 4) and (len(log_text) > 199):
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size = 4\' maximum 199 character support ...')
		return
	elif (log_size == 5) and (len(log_text) > 397):
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size = 5\' maximum 397 character support ...')
		return

	# set value for write python file name in log file ...

	if len(python_file) == 3:
		log_file_python_file_name = '        '+str(python_file)+'       '
	elif len(python_file) == 4:
		log_file_python_file_name = '       '+str(python_file)+'       '
	elif len(python_file) == 5:
		log_file_python_file_name = '      '+str(python_file)+'       '
	elif len(python_file) == 6:
		log_file_python_file_name = '      '+str(python_file)+'      '
	elif len(python_file) == 7:
		log_file_python_file_name = '     '+str(python_file)+'      '
	elif len(python_file) == 8:
		log_file_python_file_name = '     '+str(python_file)+'     '
	elif len(python_file) == 9:
		log_file_python_file_name = '    '+str(python_file)+'     '
	elif len(python_file) == 10:
		log_file_python_file_name = '    '+str(python_file)+'    '
	elif len(python_file) == 11:
		log_file_python_file_name = '   '+str(python_file)+'    '
	elif len(python_file) == 12:
		log_file_python_file_name = '   '+str(python_file)+'   '
	elif len(python_file) == 13:
		log_file_python_file_name = '  '+str(python_file)+'   '
	elif len(python_file) == 14:
		log_file_python_file_name = '  '+str(python_file)+'  '
	elif len(python_file) == 15:
		log_file_python_file_name = ' '+str(python_file)+'  '
	elif len(python_file) == 16:
		log_file_python_file_name = ' '+str(python_file)+' '
	elif len(python_file) == 17:
		log_file_python_file_name = str(python_file)+' '
	elif len(python_file) == 18:
		log_file_python_file_name = str(python_file)

	# set value for write line of python file in log file ...

	if len(line_python_file) == 1:
		log_file_python_file_line = '   '+str(line_python_file)+'  '
	elif len(line_python_file) == 2:
		log_file_python_file_line = '  '+str(line_python_file)+'  '
	elif len(line_python_file) == 3:
		log_file_python_file_line = '  '+str(line_python_file)+' '
	elif len(line_python_file) == 4:
		log_file_python_file_line = ' '+str(line_python_file)+' '
	elif len(line_python_file) == 5:
		log_file_python_file_line = ' '+str(line_python_file)
	elif len(line_python_file) == 6:
		log_file_python_file_line = str(line_python_file)
	elif len(line_python_file) > 6:
		print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : maximum python line number support is 999999 ...')

	# set value for write log text in log file ...

	log_file_text = log_text

	# set value for log file name ...

	log_file_name = log_file

	# set value for log file size ...

	if log_size == 1:
		log_file_size = round(((6-0.3)/100)*((5-0.1)*20),1)
	elif log_size == 2:
		log_file_size = round(((6-0.3)/100)*((5-2.9)*20),1)
	elif log_size == 3:
		log_file_size = round(((6-0.3)/100)*((5-3.9)*20),1)
	elif log_size == 4:
		log_file_size = round(((6-0.3)/100)*((5-4.4)*20),1)
	elif log_size == 5:
		log_file_size = round(((6-0.3)/100)*((5-4.7)*20),1)

	# -----------------------------------------------------------------------------------------------------------------------------------------------------------

	# get continent ...

	continent = str(get_localzone()).lower().split('/')[0]

	# get country ...

	def get_country():
		data = {"Kabul": "Afghanistan", "Tirana": "Albania", "Alger": "Algeria", "Fagatogo": "American Samoa", "Andorra la Vella": "Andorra", "Luanda": "Angola", "The Valley": "Anguilla", "null": "United States Minor Outlying Islands", "Saint John's": "Antigua and Barbuda", "Buenos Aires": "Argentina", "Yerevan": "Armenia", "Oranjestad": "Aruba", "Canberra": "Australia", "Wien": "Austria", "Baku": "Azerbaijan", "Nassau": "Bahamas", "al-Manama": "Bahrain", "Dhaka": "Bangladesh", "Bridgetown": "Barbados", "Minsk": "Belarus", "Bruxelles [Brussel]": "Belgium", "Belmopan": "Belize", "Porto-Novo": "Benin", "Hamilton": "Bermuda", "Thimphu": "Bhutan", "La Paz": "Bolivia", "Sarajevo": "Bosnia and Herzegovina", "Gaborone": "Botswana", "Bras\u00edlia": "Brazil", "Bandar Seri Begawan": "Brunei", "Sofia": "Bulgaria", "Ouagadougou": "Burkina Faso", "Bujumbura": "Burundi", "Phnom Penh": "Cambodia", "Yaound": "Cameroon", "Ottawa": "Canada", "Praia": "Cape Verde", "George Town": "Cayman Islands", "Bangui": "Central African Republic", "N'Djam": "Chad", "Santiago de Chile": "Chile", "Peking": "China", "Flying Fish Cove": "Christmas Island", "West Island": "Cocos (Keeling) Islands", "Santaf": "Colombia", "Moroni": "Comoros", "Brazzaville": "Congo", "Avarua": "Cook Islands", "San Jos": "Costa Rica", "Zagreb": "Croatia", "La Habana": "Cuba", "Nicosia": "Cyprus", "Praha": "Czech Republic", "Copenhagen": "Denmark", "Djibouti": "Djibouti", "Roseau": "Dominica", "Santo Domingo de Guzm": "Dominican Republic", "Dili": "East Timor", "Quito": "Ecuador", "Cairo": "Egypt", "San Salvador": "El Salvador", "London": "United Kingdom", "Malabo": "Equatorial Guinea", "Asmara": "Eritrea", "Tallinn": "Estonia", "Addis Abeba": "Ethiopia", "Stanley": "Falkland Islands", "T\u00f3rshavn": "Faroe Islands", "Suva": "Fiji Islands", "Helsinki [Helsingfors]": "Finland", "Paris": "France", "Cayenne": "French Guiana", "Papeete": "French Polynesia", "Libreville": "Gabon", "Banjul": "Gambia", "Tbilisi": "Georgia", "Berlin": "Germany", "Accra": "Ghana", "Gibraltar": "Gibraltar", "Athenai": "Greece", "Nuuk": "Greenland", "Saint George's": "Grenada", "Basse-Terre": "Guadeloupe", "Aga": "Guam", "Ciudad de Guatemala": "Guatemala", "Conakry": "Guinea", "Bissau": "Guinea-Bissau", "Georgetown": "Guyana", "Port-au-Prince": "Haiti", "Citt": "Holy See (Vatican capital State)", "Tegucigalpa": "Honduras", "Victoria": "Seychelles", "Budapest": "Hungary", "Reykjav": "Iceland", "New Delhi": "India", "Jakarta": "Indonesia", "Tehran": "Iran", "Baghdad": "Iraq", "Dublin": "Ireland", "Jerusalem": "Israel", "Roma": "Italy", "Yamoussoukro": "Ivory Coast", "Kingston": "Norfolk Island", "Tokyo": "Japan", "Amman": "Jordan", "Astana": "Kazakhstan", "Nairobi": "Kenya", "Bairiki": "Kiribati", "Kuwait": "Kuwait", "Bishkek": "Kyrgyzstan", "Vientiane": "Laos", "Riga": "Latvia", "Beirut": "Lebanon", "Maseru": "Lesotho", "Monrovia": "Liberia", "Tripoli": "Libyan Arab Jamahiriya", "Vaduz": "Liechtenstein", "Vilnius": "Lithuania", "Luxembourg [Luxemburg/L": "Luxembourg", "Macao": "Macao", "Skopje": "North Macedonia", "Antananarivo": "Madagascar", "Lilongwe": "Malawi", "Kuala Lumpur": "Malaysia", "Male": "Maldives", "Bamako": "Mali", "Valletta": "Malta", "Dalap-Uliga-Darrit": "Marshall Islands", "Fort-de-France": "Martinique", "Nouakchott": "Mauritania", "Port-Louis": "Mauritius", "Mamoutzou": "Mayotte", "Ciudad de M": "Mexico", "Palikir": "Micronesia, Federated States of", "Chisinau": "Moldova", "Monaco-Ville": "Monaco", "Ulan Bator": "Mongolia", "Plymouth": "Montserrat", "Rabat": "Morocco", "Maputo": "Mozambique", "Rangoon (Yangon)": "Myanmar", "Windhoek": "Namibia", "Yaren": "Nauru", "Kathmandu": "Nepal", "Amsterdam": "Netherlands", "Willemstad": "Netherlands Antilles", "Noum": "New Caledonia", "Wellington": "New Zealand", "Managua": "Nicaragua", "Niamey": "Niger", "Abuja": "Nigeria", "Alofi": "Niue", "Pyongyang": "North Korea", "Belfast": "Northern Ireland", "Garapan": "Northern Mariana Islands", "Oslo": "Norway", "Masqat": "Oman", "Islamabad": "Pakistan", "Koror": "Palau", "Gaza": "Palestine", "Ciudad de Panam": "Panama", "Port Moresby": "Papua New Guinea", "Asunci": "Paraguay", "Lima": "Peru", "Manila": "Philippines", "Adamstown": "Pitcairn", "Warszawa": "Poland", "Lisboa": "Portugal", "San Juan": "Puerto Rico", "Doha": "Qatar", "Saint-Denis": "Reunion", "Bucuresti": "Romania", "Moscow": "Russian Federation", "Kigali": "Rwanda", "Jamestown": "Saint Helena", "Basseterre": "Saint Kitts and Nevis", "Castries": "Saint Lucia", "Saint-Pierre": "Saint Pierre and Miquelon", "Kingstown": "Saint Vincent and the Grenadines", "Apia": "Samoa", "San Marino": "San Marino", "S": "Sao Tome and Principe", "Riyadh": "Saudi Arabia", "Edinburgh": "Scotland", "Dakar": "Senegal", "Freetown": "Sierra Leone", "Singapore": "Singapore", "Bratislava": "Slovakia", "Ljubljana": "Slovenia", "Honiara": "Solomon Islands", "Mogadishu": "Somalia", "Pretoria": "South Africa", "Seoul": "South Korea", "Juba": "South Sudan", "Madrid": "Spain", "Khartum": "Sudan", "Paramaribo": "Suriname", "Longyearbyen": "Svalbard and Jan Mayen", "Mbabane": "Swaziland", "Stockholm": "Sweden", "Bern": "Switzerland", "Damascus": "Syria", "Dushanbe": "Tajikistan", "Dodoma": "Tanzania", "Bangkok": "Thailand", "Lom": "Togo", "Fakaofo": "Tokelau", "Nuku'alofa": "Tonga", "Port-of-Spain": "Trinidad and Tobago", "Tunis": "Tunisia", "Ankara": "Turkey", "Ashgabat": "Turkmenistan", "Cockburn Town": "Turks and Caicos Islands", "Funafuti": "Tuvalu", "Kampala": "Uganda", "Kyiv": "Ukraine", "Abu Dhabi": "United Arab Emirates", "Washington": "United States", "Montevideo": "Uruguay", "Toskent": "Uzbekistan", "Port-Vila": "Vanuatu", "Caracas": "Venezuela", "Hanoi": "Vietnam", "Road Town": "Virgin Islands, British", "Charlotte Amalie": "Virgin Islands, U.S.", "Cardiff": "Wales", "Mata-Utu": "Wallis and Futuna", "El-Aai": "Western Sahara", "Sanaa": "Yemen", "Beograd": "Yugoslavia", "Lusaka": "Zambia", "Harare": "Zimbabwe"}
		if str(get_localzone()).split('/')[1] in data:
			return data['Tehran'].lower()

	country = str(get_country())

	# get city ...

	city = str(get_localzone()).lower().split('/')[1]

	# get username ...

	username = str(getuser())

	# get os ...

	os = str(system().lower())

	# get version ...

	version = str(release().lower())

	# get architecture

	architecture = str(machine().lower())

	# get date ...

	date = str(datetime.now()).split(' ')[0]

	# get time ...

	time = str(datetime.now()).split(' ')[1].split('.')[0]

	# -----------------------------------------------------------------------------------------------------------------------------------------------------------

	# show city , country , continent , username , os , version , architecture in log file ...

	specifications_center = city+' < '+country+' < '+continent+' | '+username+' | '+os+' > '+version+' > '+architecture
	specifications = ' |  num  |    date    |   time   |'+' '*int(len(specifications_center)/log_file_size)+specifications_center+' '*int(len(specifications_center)/log_file_size)+'|       file       | line | '

	# if is not log file ...

	if not isfile(log_file_name):

		# create log file ...

		log_file = open(log_file_name,'w')

		# write ' ___ ' to log file ...

		log_file.write('\n'+'  .'+'_'*(len(specifications)-4)+'.'+'\n')

		#write 'specifications' to log file ...

		log_file.write(' '+specifications+'\n')

		# write ' ___ ' to log file ...

		log_file.write('  .'+'_'*(len(specifications)-4)+'.'+'\n')

		# write 'log' to log file ...

		log_file.write('  |   '+str(1)+'   | '+date+' | '+time+' | '+str(text)+' '*(len(specifications)-(len(log_file_text)+len(log_file_python_file_name)+45))+'|'+log_file_python_file_name+'|'+log_file_python_file_line+'|'+'\n')
		
		# write ' ___ ' to log file ...

		log_file.write('  .'+'_'*(len(specifications)-4)+'.'+'\n')

		# save and close log file ..

		log_file.close()

	# if is log file ...

	elif isfile(log_file_name):

		with open(log_file_name, 'r') as f:
		    if f.read().splitlines()[-1] != '  .'+'_'*(len(specifications)-4)+'.':
		    	print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | previously defined log file size , can\'not be resized ...')
		    	return

		# find line number ...

		with open(log_file_name, 'r') as f:
			number_line = f.read().splitlines()[-2].split('| '+str(datetime.now().year)+'-', 1)[0]
			number_line = number_line.replace('|','')
			number_line = number_line.replace(' ','')
			number_line = int(number_line)+1

		# ckeck log file line number ...

		if len(str(number_line)) > 7:
			print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : \'size = 5\' maximum line number support is 9999999 ...')
			return

		# set value for log file line number ...

		if len(str(number_line)) == 1:
			log_file_number = '   '+str(number_line)+'   '
		elif len(str(number_line)) == 2:
			log_file_number = '  '+str(number_line)+'   '
		elif len(str(number_line)) == 3:
			log_file_number = '  '+str(number_line)+'  '
		elif len(str(number_line)) == 4:
			log_file_number = ' '+str(number_line)+'  '
		elif len(str(number_line)) == 5:
			log_file_number = ' '+str(number_line)+' '
		elif len(str(number_line)) == 6:
			log_file_number = str(number_line)+' '
		elif len(str(number_line)) == 7:
			log_file_number = str(number_line)
		else:
			print('negar module - error | python file : '+python_file+' | line : '+line_python_file+' | problem : maximum number to numbering lines support is 9999999 ...')
			return

		# open log file ...

		log_file = open(log_file_name,'a')

		# add new 'log' to log file ...

		log_file.write('  |'+log_file_number+'| '+date+' | '+time+' | '+str(text)+' '*(len(specifications)-(len(log_file_text)+len(log_file_python_file_name)+45))+'|'+log_file_python_file_name+'|'+log_file_python_file_line+'|'+'\n')
		
		# write ' ___ ' to log file ...

		log_file.write('  .'+'_'*(len(specifications)-4)+'.'+'\n')
		
		# save and close log file ..

		log_file.close()
