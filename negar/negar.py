# Copyright SYS113 2019. MIT license , see README.md file.

# import libraries ...
from tzlocal import get_localzone
from datetime import datetime
from platform import system, release, machine
from getpass import getuser
from os.path import isfile
from inspect import getframeinfo, stack
from negar.countriesWithTheirCapital import countries


# create log function ...
def text(text_log=None, save=None, size=None):
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
    def log_row(row_num, log_date, log_time, row_text, row_log_size, row_file_name, row_line_num):
        out = '  |{}| {} | {} | {}{}|{}|{}|\n'.format(justify_text(row_num, 7), log_date, log_time, row_text,
                                                      ' ' * (row_log_size - (len(log_file_text) + 1)),
                                                      row_file_name, row_line_num)
        out += '  |{}|\n'.format('—' * (len(out) - 5))
        return out

    # find (filename or line) python file ...
    x = stack()[1]
    x = x[0]
    get_python_file_name_or_line = getframeinfo(x)

    # set valur for find line in python file ...
    line_python_file = str(get_python_file_name_or_line.lineno)

    # set value for find python file name ...
    python_file_name = str(get_log_file_python_file_name_or_line.filename.split('/')[-1])

    if python_file_name == '<stdin>':
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
        print(err_temp_func(python_file_name, line_python_file, '\'save\' type is not str ...'))
        return

    # set value for log text ...
    if text is None:
        print(err_temp_func(python_file_name, line_python_file, '\'text\' value is empty ...'))
        return
    elif not isinstance(text, str):
        print(err_temp_func(python_file_name, line_python_file, '\'text\' type is not str ...'))
        return
    elif text == '':
        print(err_temp_func(python_file_name, line_python_file, '\'text\' value is empty ...'))
        return
    else:
        log_text = text

    # set value for log file size ...
    if size is None:
        log_size = 2
    elif not isinstance(size, int):
        print(err_temp_func(python_file_name, line_python_file, '\'size\' type is not str ...'))
        return
    elif size > 5:
        print(err_temp_func(python_file_name, line_python_file, '\'size\' value range is not (1 ... 5) ...'))
        return
    elif size == 0:
        print(err_temp_func(python_file_name, line_python_file, '\'size\' value is not in range (1 ... 5) ...'))
        return
    else:
        log_size = size

        # set value for speed ...
        if speed is None:
            speed = 0.040
        elif speed is not None:
            if type(speed) is not int:
                error('\'speed\' argument must be number range of 1 to 10 ...')
                return
            elif speed == 1:
                speed = 0.020
            elif speed == 2:
                speed = 0.030
            elif speed == 3:
                speed = 0.040
            elif speed == 4:
                speed = 0.050
            elif speed == 5:
                speed = 0.060
            elif speed == 6:
                speed = 0.070
            elif speed == 7:
                speed = 0.080
            elif speed == 8:
                speed = 0.090
            elif speed == 9:
                speed = 0.200
            elif speed == 10:
                speed = 0.350
            elif speed > 10:
                error('\'speed\' argument must be number range of 1 to 10 ...')
                return

        # cannot use simultaneously 'sleep' and 'function' argument ...
        if sleep is not None:
            error(
                'if use \'sleep\' argument , cannot use \'function\' argument and vice versa ...')
            return

        # argument has value ...
        if argument is not None:
            if type(argument) is not list:
                error('argument \'argument\' must be a list type ...')
                return

        # output no value ...
        if output is None:
            output = True

        # output has value ...
        elif output is not None:
            if type(output) is not bool:
                error('argument \'output\' must be boolean type ...')
                return

    # function no value ...
    elif function is None:

        # sleep no value ...
        if sleep is None:

            # sleep has value ...
            if speed is not None:
                error(
                    'need \'sleep\' or \'function\' argument to use the \'speed\' argument ...')
                return

            # method has value ...
            elif method is not None:
                error(
                    'need \'sleep\' or \'function\' argument to use the \'method\' argument ...')
                return

        # argument has value ...
        if argument is not None:
            error('need \'function\' argument to use the \'argument\' argument ...')
            return

        # output has value ...
        if output is not None:
            error('need \'function\' argument to use the \'output\' argument ...')
            return

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    # show city , country , continent , username , os , version , architecture in log file ...
    spec_center = '%s < %s < %s | %s | %s > %s > %s' % (
        city, country, continent, username, os, version, architecture)
    spec_center = justify_text(spec_center, 2 * int(len(spec_center) / log_file_size) + len(spec_center))
    specifications = ' |  num  |    date    |   time   |' + spec_center + '|       file       | line | '

    # if is not log file ...
    if not isfile(log_file_name):
        # create log file ...
        with open(log_file_name, 'w') as log_file:
            # write ' ___ ' to log file ...
            log_file.write(header_row(specifications))

            # write 'log' to log file ...
            log_file.write(
                log_row(1, date, time, text, len(spec_center), justified_python_file, justified_line_python_file))

    # if is log file ...
    elif isfile(log_file_name):
        with open(log_file_name, 'r') as f:
            if f.read().splitlines()[-1] != '  |' + '—' * (len(specifications) - 4) + '|':
                print(err_temp_func(python_file_name, line_python_file,
                                    "previously defined log file size , can't be resized ..."))
                return

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    # fix show text color ...
    system('')

    # if finished is True break animate function ...
    finished = False

        # open log file ...
        with open(log_file_name, 'a') as log_file:
            # add new 'log' to log file ...
            log_file.write(log_row(log_file_number, date, time, text_log, len(spec_center), justified_python_file,
                                   log_type, justified_line_python_file))
