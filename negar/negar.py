# Copyright SYS113 2019. MIT license , see README.md file.

# import libraries 
from re import search
from traceback import format_exc
from tzlocal import get_localzone
from datetime import datetime
from platform import system, release, machine
from getpass import getuser
from os.path import isfile
from inspect import getframeinfo, stack
from negar.countriesWithTheirCapital import countries


# helper function for country capital
def get_country(_city):
	data = countries
	if _city in data:
		return data[_city]
	else:
		return 'unknown'


# helper function for negar module errors printing
def err_temp_func(file_, line, problem):
	error_template = 'negar module - error | python file : {} | line : {} | problem : {}'
	return error_template.format(file_, line, problem)


# helper function for justify text center with fixed length
def justify_text(text_, length):
	return '{}{}{}'.format(int((length - len(str(text_))) / 2) * ' ', text_, length * ' ')[:length]


# helper function for create header row
def header_row(header_specs):
	sep = '—' * (len(header_specs) - 4)
	out = '\n  .{1}.\n {0}\n  |{1}|\n'.format(header_specs, sep)
	return out


# helper function for create each log row
def log_row(row_num, log_date, log_time, row_text, row_log_size, row_file_name, row_type, row_line_num):
	row_num = justify_text(row_num, 7)
	row_type = justify_text(row_type, 8)
	out = '  |{num}| {date} | {time} | {text}{pad}|{file}|{type}|{line}|\n'.format(
		num=row_num, date=log_date, time=log_time, text=row_text, file=row_file_name, type=row_type,
		line=row_line_num, pad=' ' * (row_log_size - (len(row_text) + 1)))
	out += '  |{}|\n'.format('—' * (len(out) - 5))
	return out


# create text log function ...
def text(text_log=None, save=None, size=None , line=None , date=None , time=None , title=None):

	# find (filename or line) python file ...
	x = stack()[1]
	x = x[0]
	get_log_file_python_file_name_or_line = getframeinfo(x)

	# ----------------------------------------------------------------------------------------------------------------
	'''                                                    
	'find line in python file' variable is 'line_python_file'
	'find python file name' variable is 'python_file'
	'save log in a file' variable is 'log_file'
	'log text' variable is 'log_text'
	'set log file size' variable is 'log_file_size'
	'''
	# ----------------------------------------------------------------------------------------------------------------

	# set Flase and True value for show line python file in log file ...
	if (line is None) or (line is False):
		line_python_file = '-'
	elif line is True:
		line_python_file = str(get_log_file_python_file_name_or_line.lineno)
	else:
		print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), '"show" value is not boolean ...'))
		return

	# set value for find python file name ...
	python_file_name = str(get_log_file_python_file_name_or_line.filename.split('/')[-1])

	if python_file_name in ['<stdin>', '<input>']:
		python_file = 'interpreter'
	elif len(python_file_name) < 18:
		python_file = python_file_name
	else:
		print(err_temp_func(python_file_name, line_python_file, 'maximum size of python file name is 15 character ...'))
		return

	# set value for save log in a file ...
	if isinstance(save, str):
		log_file = save
	elif save is None:
		log_file = 'log.txt'
	else:
		print(err_temp_func(python_file_name, line_python_file, '"save" type is not str ...'))
		return

	# set value for log text ...
	if text_log is None:
		print(err_temp_func(python_file_name, line_python_file, '"text" value is empty ...'))
		return
	elif not isinstance(text_log, str):
		print(err_temp_func(python_file_name, line_python_file, '"text" type is not str ...'))
		return
	elif text_log == '':
		print(err_temp_func(python_file_name, line_python_file, '"text" value is empty ...'))
		return
	else:
		log_text = text_log

	# set value for log file size ...
	if size is None:
		log_size = 3
	elif not isinstance(size, int):
		print(err_temp_func(python_file_name, line_python_file, '"size" type is not str ...'))
		return
	elif size > 5:
		print(err_temp_func(python_file_name, line_python_file, '"size" value range is not (1 ... 5) ...'))
		return
	elif size == 0:
		print(err_temp_func(python_file_name, line_python_file, '"size" value is not in range (1 ... 5) ...'))
		return
	else:
		log_size = size

	# ----------------------------------------------------------------------------------------------------------------
	'''
	'write python file name in log file' variable is 'justified_python_file'
	'write line of python file in log file' variable is 'justified_line_python_file'
	'write log text in log file' variable is 'log_file_text'
	'log file name' variable is 'log_file_name'
	'log file size' variable is 'log_file_size'
	'''
	# ----------------------------------------------------------------------------------------------------------------

	# check character size ...
	if (log_size == 1) and (len(log_text) > 69):
		print(err_temp_func(python_file_name, line_python_file, '"size = 1" maximum 69 character support ...'))
		return
	elif (log_size == 2) and (len(log_text) > 93):
		print(err_temp_func(python_file_name, line_python_file, '"size = 2" maximum 93 character support ...'))
		return
	elif (log_size == 3) and (len(log_text) > 131):
		print(err_temp_func(python_file_name, line_python_file, '"size = 3" maximum 131 character support ...'))
		return
	elif (log_size == 4) and (len(log_text) > 199):
		print(err_temp_func(python_file_name, line_python_file, '"size = 4" maximum 199 character support ...'))
		return
	elif (log_size == 5) and (len(log_text) > 397):
		print(err_temp_func(python_file_name, line_python_file, '"size = 5" maximum 397 character support ...'))
		return

	# set value for write python file name in log file ...
	justified_python_file = justify_text(python_file, 18)

	# set value for write line of python file in log file ...
	if len(line_python_file) <= 6:
		justified_line_python_file = justify_text(line_python_file, 6)
	else:
		print(err_temp_func(python_file_name, line_python_file, 'maximum python line number support is 999999 ...'))
		return

	# set value for log file name ...
	log_file_name = log_file

	# set value for log file size ...
	log_file_size = round(((6 - 0.3) / 100) * ((5 - [0.1, 2.9, 3.9, 4.4, 4.7][log_size - 1]) * 20), 1)
	# ----------------------------------------------------------------------------------------------------------------

	# get continent ...
	continent = str(get_localzone()).lower().split('/')[0]

	# get city ...
	city = str(get_localzone()).lower().split('/')[1]

	# get country ...
	country = str(get_country(city))

	# get username ...
	username = str(getuser())

	# get os ...
	os = str(system().lower())

	# get version ...
	version = str(release().lower())

	# get architecture
	architecture = str(machine().lower())

	# log type
	log_type = 'text'

	# ----------------------------------------------------------------------------------------------------------------
	# set Flase and True value for time in log file ...
	if (time is None) or (time is True):
		time = str(datetime.now()).split(' ')[1].split('.')[0]
	elif time is False:
		time = '   -    '
	else:
		print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), '"time" value is not boolean ...'))
		return
	# ----------------------------------------------------------------------------------------------------------------
	# set Flase and True value for show date in log file ...
	if (date is None) or (date is True):
		date = str(datetime.now()).split(' ')[0]
	elif date is False:
		date = '    -     '
	else:
		print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), '"date" value is not boolean ...'))
		return
	# ----------------------------------------------------------------------------------------------------------------

	# show city , country , continent , username , os , version , architecture in log file ...
	sp_center = '%s < %s < %s | %s | %s > %s > %s' % (
		city, country, continent, username, os, version, architecture)
	spec_center = justify_text(sp_center, 2 * int(len(sp_center) / log_file_size) + len(sp_center))
	T = (len(spec_center)-len(sp_center))/2

	if title is not None:
		if len(title) > len(spec_center):
			print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), 'maximum \'title\' size is '+str(len(spec_center))+' ...'))
			return

	if (title is None) or (title is False):
		specifications = ' |  num  |    date    |   time   |' + spec_center + '|       file       |  type  | line | '
	else:
		specifications = ' |  num  |    date    |   time   |' + title.center(len(spec_center)) + '|       file       |  type  | line | '

	# if is not log file ...
	if not isfile(log_file_name):
		# create log file ...
		with open(log_file_name, 'w') as log_file:
			# write ' ___ ' to log file ...
			log_file.write(header_row(specifications))

			# write 'error & text' to log file ...
			log_file.write(
				log_row(1, date, time, text_log, len(spec_center), justified_python_file, log_type,
						justified_line_python_file))

	# if is log file ...
	elif isfile(log_file_name):
		with open(log_file_name, 'r') as f:
			if f.read().splitlines()[-1] != '  |' + '—' * (len(specifications) - 4) + '|':
				print(err_temp_func(python_file_name, line_python_file,
									"previously defined log file size , can't be resized ..."))
				return

		# find line number ...
		with open(log_file_name, 'r') as f:
			line_number = f.read().splitlines()[-2].split('|')[1]
			line_number = line_number.replace(' ', '')
			line_number = int(line_number) + 1

		# ckeck log file line number ...
		if len(str(line_number)) > 7:
			print(err_temp_func(python_file_name, line_python_file,
								"'size = 5' maximum line number support is 9999999 ..."))
			return

		# set value for log file line number ...
		if len(str(line_number)) <= 7:
			log_file_number = justify_text(line_number, 7)
		else:
			print(err_temp_func(python_file_name, line_python_file,
								'maximum number to numbering lines support is 9999999 ...'))
			return

		# open log file ...
		with open(log_file_name, 'a') as log_file:

			# add new 'error & text' to log file ...
			log_file.write(log_row(log_file_number, date, time, text_log, len(spec_center), justified_python_file,
								   log_type, justified_line_python_file))


# create error log function ...
def error(save=None, size=None, line=None , time=None , date=None , title=None):

	# find (filename or line) python file ...
	x = stack()[1]
	x = x[0]
	get_log_file_python_file_name_or_line = getframeinfo(x)

	# write exception to error_log variable ...
	error_log = format_exc()
	if len(error_log.splitlines()) < 2:
		return

	# error log ...
	error_text = str(error_log.splitlines()[-1])
	a = [*filter(lambda x: x.find('File') > -1, error_log.splitlines())]

	# file name ...
	python_file_name = search('File "(.*)", line (.*), in (.*)', a[-1]).groups()
	for i in a[:-1][::-1]:
		x = search('File "(.*)", line (.*), in (.*)', i).groups()
		if x and python_file_name[2] == x[2]:
			python_file_name = x
		else:
			break

	# set Flase and True value for show line python file in log file ...
	if (line is None) or (line is True):
		line_python_file = str(get_log_file_python_file_name_or_line.lineno)
	elif line is False:
		line_python_file = '-'
	else:
		print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), '"line" value is not boolean ...'))
		return

	# name python file ...
	python_file_name = str(python_file_name[0]).split('/')[-1]

	# ----------------------------------------------------------------------------------------------------------------
	'''                                                    
	'find line in python file' variable is 'line_python_file'
	'find python file name' variable is 'python_file'
	'save log in a file' variable is 'log_file'
	'log text' variable is 'log_text'
	'set log file size' variable is 'log_file_size'
	'''
	# ----------------------------------------------------------------------------------------------------------------

	if python_file_name in ['<stdin>', '<input>']:
		python_file = 'interpreter'
	elif len(python_file_name) < 18:
		python_file = python_file_name
	else:
		print(err_temp_func(python_file_name, line_python_file, 'maximum size of python file name is 15 character ...'))
		return

	# set value for save log in a file ...
	if isinstance(save, str):
		log_file = save
	elif save is None:
		log_file = 'log.txt'
	else:
		print(err_temp_func(python_file_name, line_python_file, '"save" type is not str ...'))
		return

	# set value for log file size ...
	if size is None:
		log_size = 3
	elif not isinstance(size, int):
		print(err_temp_func(python_file_name, line_python_file, '"size" type is not str ...'))
		return
	elif size > 5:
		print(err_temp_func(python_file_name, line_python_file, '"size" value range is not (1 ... 5) ...'))
		return
	elif size == 0:
		print(err_temp_func(python_file_name, line_python_file, '"size" value is not in range (1 ... 5) ...'))
		return
	else:
		log_size = size

	# ----------------------------------------------------------------------------------------------------------------
	'''
	'write python file name in log file' variable is 'justified_python_file'
	'write line of python file in log file' variable is 'justified_line_python_file'
	'write log text in log file' variable is 'log_file_text'
	'log file name' variable is 'log_file_name'
	'log file size' variable is 'log_file_size'
	'''
	# ----------------------------------------------------------------------------------------------------------------

	# check character size ...
	if (log_size == 1) and (len(error_text) > 69):
		print(err_temp_func(python_file_name, line_python_file, '"size = 1" maximum 69 character support ...'))
		return
	elif (log_size == 2) and (len(error_text) > 93):
		print(err_temp_func(python_file_name, line_python_file, '"size = 2" maximum 93 character support ...'))
		return
	elif (log_size == 3) and (len(error_text) > 131):
		print(err_temp_func(python_file_name, line_python_file, '"size = 3" maximum 131 character support ...'))
		return
	elif (log_size == 4) and (len(error_text) > 199):
		print(err_temp_func(python_file_name, line_python_file, '"size = 4" maximum 199 character support ...'))
		return
	elif (log_size == 5) and (len(error_text) > 397):
		print(err_temp_func(python_file_name, line_python_file, '"size = 5" maximum 397 character support ...'))
		return

	# set value for write python file name in log file ...
	justified_python_file = justify_text(python_file, 18)

	# set value for write line of python file in log file ...
	if len(line_python_file) <= 6:
		justified_line_python_file = justify_text(line_python_file, 6)
	else:
		print(err_temp_func(python_file_name, line_python_file, 'maximum python line number support is 999999 ...'))
		return

	# set value for log file name ...
	log_file_name = log_file

	# set value for log file size ...
	log_file_size = round(((6 - 0.3) / 100) * ((5 - [0.1, 2.9, 3.9, 4.4, 4.7][log_size - 1]) * 20), 1)
	# ----------------------------------------------------------------------------------------------------------------
	# get continent ...
	continent = str(get_localzone()).lower().split('/')[0]

	# get city ...
	city = str(get_localzone()).lower().split('/')[1]

	# get country ...
	country = str(get_country(city))

	# get username ...
	username = str(getuser())

	# get os ...
	os = str(system().lower())

	# get version ...
	version = str(release().lower())

	# get architecture
	architecture = str(machine().lower())

	# log type
	log_type = ' error'
	# ----------------------------------------------------------------------------------------------------------------
	# set Flase and True value for time in log file ...
	if (time is None) or (time is True):
		time = str(datetime.now()).split(' ')[1].split('.')[0]
	elif time is False:
		time = '   -    '
	else:
		print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), '"time" value is not boolean ...'))
		return
	# ----------------------------------------------------------------------------------------------------------------
	# set Flase and True value for show date in log file ...
	if (date is None) or (date is True):
		date = str(datetime.now()).split(' ')[0]
	elif date is False:
		date = '    -     '
	else:
		print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), '"date" value is not boolean ...'))
		return
	# ----------------------------------------------------------------------------------------------------------------
	'''
	# show city , country , continent , username , os , version , architecture in log file ...
	spec_center = '%s < %s < %s | %s | %s > %s > %s' % (
		city, country, continent, username, os, version, architecture)
	spec_center = justify_text(spec_center, 2 * int(len(spec_center) / log_file_size) + len(spec_center))
	specifications = ' |  num  |    date    |   time   |' + spec_center + '|       file       |  type  | line | '
	'''

	# show city , country , continent , username , os , version , architecture in log file ...
	sp_center = '%s < %s < %s | %s | %s > %s > %s' % (
		city, country, continent, username, os, version, architecture)
	spec_center = justify_text(sp_center, 2 * int(len(sp_center) / log_file_size) + len(sp_center))
	T = (len(spec_center)-len(sp_center))/2
	
	if title is not None:
		if len(title) > len(spec_center):
			print(err_temp_func(str(get_log_file_python_file_name_or_line.filename.split('/')[-1]), str(get_log_file_python_file_name_or_line.lineno), 'maximum \'title\' size is '+str(len(spec_center))+' ...'))
			return

	if (title is None) or (title is False):
		specifications = ' |  num  |    date    |   time   |' + spec_center + '|       file       |  type  | line | '
	else:
		specifications = ' |  num  |    date    |   time   |' + title.center(len(spec_center)) + '|       file       |  type  | line | '


	# if is not log file ...
	if not isfile(log_file_name):

		# create log file ...
		with open(log_file_name, 'w') as log_file:

			# write ' ___ ' to log file ...
			log_file.write(header_row(specifications))

			# write 'error & text' to log file ...
			log_file.write(
				log_row(1, date, time, error_text, len(spec_center), justified_python_file, log_type,
						justified_line_python_file))

	# if is log file ...
	elif isfile(log_file_name):
		with open(log_file_name, 'r') as f:
			if f.read().splitlines()[-1] != '  |' + '—' * (len(specifications) - 4) + '|':
				print(err_temp_func(python_file_name, line_python_file,
									"previously defined log file size , can't be resized ..."))
				return

		# find line number ...
		with open(log_file_name, 'r') as f:
			line_number = f.read().splitlines()[-2].split('|')[1]
			line_number = line_number.replace(' ', '')
			line_number = int(line_number) + 1

		# ckeck log file line number ...
		if len(str(line_number)) > 7:
			print(err_temp_func(python_file_name, line_python_file,
								"'size = 5' maximum line number support is 9999999 ..."))
			return

		# set value for log file line number ...
		if len(str(line_number)) <= 7:
			log_file_number = justify_text(line_number, 7)
		else:
			print(err_temp_func(python_file_name, line_python_file,
								'maximum number to numbering lines support is 9999999 ...'))
			return

		# open log file ...
		with open(log_file_name, 'a') as log_file:
			# add new 'error & text' to log file ...
			log_file.write(log_row(log_file_number, date, time, error_text, len(spec_center), justified_python_file,
								   log_type, justified_line_python_file))
