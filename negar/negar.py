# import libs ...
import sys
from os import system
from platform import system as ostype
from cursor import hide, show
from sys import stdout
from subprocess import check_output
from threading import Thread
from time import sleep as zzz
from inspect import getframeinfo, stack
from random import choice
from queue import Queue

# loading function ...
def loading(sleep=None, function=None, speed=None, method=None, argument=None, output=None):

    # show error function ...
    def error(problem):
        print('tekrar module - error | python file : '+python_file_name +
              ' | line : '+line_python_file+' | problem : '+problem)

    # colored stars animate functions ...
    class star:
        BLUE = '{blue}*'.format(blue='\033[94m')
        GREEN = '{green}*'.format(green='\033[92m')
        RED = '{red}*'.format(red='\033[91m')
        YELLOW = '{yellow}*'.format(yellow='\033[33m')

    # find (filename or line) python file ...
    x = stack()[1]
    x = x[0]
    get_python_file_name_or_line = getframeinfo(x)

    # set valur for find line in python file ...
    line_python_file = str(get_python_file_name_or_line.lineno)

    # set value for find python file name ...
    python_file_name = str(get_python_file_name_or_line.filename)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # all argument is None ...
    if sleep is None:
        if function is None:
            if speed is None:
                if method is None:
                    if argument is None:
                        if output is None:
                            error('please use arguments ...')

    # function has value ...
    if function is not None:

        # set method , default 1 ...
        if method is None:
            method = 1
        elif type(method) is not int:
            error('\'method\' argument must be number range of 1 to 2 ...')
            return
        elif method == 1:
            method = 1
        elif method == 2:
            method = 2
        elif method > 2:
            error('\'method\' argument must be number range of 1 to 2 ...')
            return

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

        # output has value ...
        if output is not None:
            error('need \'function\' argument to use the \'output\' argument ...')
            return

    # sleep has value ...
    if sleep is not None:
        if type(sleep) is not int:
            error('argument \'sleep\' must be a int type ...')
            return

        # set method , default 1 ...
        if method is None:
            method = 1
        elif type(method) is not int:
            error('\'method\' argument must be number range of 1 to 2 ...')
            return
        elif method == 1:
            method = 1
        elif method == 2:
            method = 2
        elif method > 2:
            error('\'method\' argument must be number range of 1 to 2 ...')
            return

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

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

    # fix show text color ...
    system('')

    # if finished is True break animate function ...
    finished = False

    # check command prompet columns size
    if ostype().upper() == 'WINDOWS':
        resize = str(check_output("mode con:", shell=True))
        resize = resize.split('\\r\\n    K', 1)[0]
        a = resize[-3]
        b = resize[-2]
        c = resize[-1]
        resize = a+b+c
        resize = resize.replace(' ', '')
    elif ostype().upper() == 'LINUX':
        resize = str(check_output("resize", shell=True))
        resize = resize[10], resize[11], resize[12]
        resize = str(resize)
        resize = resize.replace(' ', '')
        resize = resize.replace(',', '')
        resize = resize.replace('\'', '')
        resize = resize.replace(')', '')
        resize = resize.replace('(', '')
        resize = resize.replace(';', '')

    #  command prompet size method 1 ...
    command_line_size_method_1 = int(resize)

    # command prompet half size method 2 ...
    half_command_line_size_method_1 = (command_line_size_method_1 - 3)//2

    # command prompet size method 2 ...
    command_line_size_method_2 = int(resize)-4

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # b is blue , g is green , r is red , y is yellow in animate method 1 comment ...

    # animate method 1 function ...
    def animate_method_1(speed):

        # hide command line cursor ...
        hide()

        # infinite repetition until forced exit ...
        while True:

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |      bgy r     |
                stdout.write(' '*half_command_line_size_method_1 +
                             star.BLUE+star.GREEN+star.YELLOW+' '*space+star.RED)

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # add star to 3 stars from left varable
                reverse = (half_command_line_size_method_1-1)-space

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |     r bgy     |
                stdout.write(' '*space+star.RED+' '*reverse +
                             star.BLUE+star.GREEN+star.YELLOW)

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |     rbg y     |
                stdout.write(' '*half_command_line_size_method_1 +
                             star.RED+star.BLUE+star.GREEN+' '*space+star.YELLOW)

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # add star to 3 stars from left varable
                reverse = (half_command_line_size_method_1-1)-space

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |     y rgbg     |
                stdout.write(' '*space+star.YELLOW+' '*reverse +
                             star.RED+star.BLUE+star.GREEN)

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |     yrb g     |
                stdout.write(' '*half_command_line_size_method_1 +
                             star.YELLOW+star.RED+star.BLUE+' '*space+star.GREEN)

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # add star to 3 stars from left varable ...
                reverse = (half_command_line_size_method_1-1)-space

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |     g yrb     |
                stdout.write(' '*space+star.GREEN+' '*reverse +
                             star.YELLOW+star.RED+star.BLUE)

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*command_line_size_method_1+'\033[0m\r')
                    return

                    # end color ...
                    stdout.write('\033[0m')

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |     gyr b     |
                stdout.write(' '*half_command_line_size_method_1 +
                             star.GREEN+star.YELLOW+star.RED+' '*space+star.BLUE)

            # show loading ...
            for space in range(half_command_line_size_method_1):

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*command_line_size_method_1+'\033[0m\r')
                    return

                    # end color ...
                    stdout.write('\033[0m')

                # add star to 3 stars from left varable
                reverse = (half_command_line_size_method_1-1)-space

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*command_line_size_method_1+'\r')

                # show loading , |     b gyr     |
                stdout.write(' '*space+star.BLUE+' '*reverse +
                             star.GREEN+star.YELLOW+star.RED)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # animate method 2 function ...
    def animate_method_2(speed):

        # hide command line cursor ...
        hide()

        # infinite repetition until forced exit ...
        while True:

            # move stars from left to right
            for space in range(command_line_size_method_2):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\033[D \033[D'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # stars variable ...
                stars = ' '*space+"***"

                # set stars random color ...
                colors = ['\x1b[34m', '\x1b[36m', '\x1b[32m', '\x1b[90m',
                          '\x1b[94m', '\x1b[96m', '\x1b[92m', '\x1b[95m',
                          '\x1b[91m', '\x1b[97m', '\x1b[93m', '\x1b[35m',
                          '\x1b[31m', '\x1b[39m', '\x1b[37m', '\x1b[33m']

                # delete line ...
                stdout.flush()
                stdout.write('\033[D \033[D'*int(resize))
                zzz(speed)
                stdout.write(' '*int(resize)+'\r')

                # show stars random color ...
                stdout.write(
                    ''.join([choice(colors) + char for char in stars]))

            # move stars from right to left
            for space in range(command_line_size_method_2):

                # end color ...
                stdout.write('\033[0m')

                # exit from animate function method 2 , if runtime ended ...
                if (not thread.isAlive()) or (finished):

                    # show command line cursor ...
                    show()

                    # delete line and close animate function ...
                    stdout.write('\r\b \b'*int(resize))
                    stdout.write(' '*int(resize)+'\r')
                    return

                # stars variable ...
                stars = ' '*(command_line_size_method_2-space)+"***"

                # set stars random color ...
                colors = ['\x1b[34m', '\x1b[36m', '\x1b[32m', '\x1b[90m',
                          '\x1b[94m', '\x1b[96m', '\x1b[92m', '\x1b[95m',
                          '\x1b[91m', '\x1b[97m', '\x1b[93m', '\x1b[35m',
                          '\x1b[31m', '\x1b[39m', '\x1b[37m', '\x1b[33m']

                # delete line ...
                stdout.flush()
                stdout.write('\b \b'*int(resize))
                zzz(speed)
                stdout.write(' '*int(resize)+'\r')

                # show stars random color ...
                stdout.write(
                    ''.join([choice(colors) + char for char in stars]))

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # create loading by sleep ...
    if sleep is not None:

        # animate method function selection ...
        if method == 1:

            # show animate function method 1 ...
            thread = Thread(target=animate_method_1, args=[speed])
            thread.start()

            # if sleep time ended break animate function ...
            zzz(sleep)

            # delete line ...
            stdout.write('\b \b'*int(resize))
            stdout.write(' '*int(resize)+'\033[0m\r')

            # if finished is True breaked animate method 1 function ...
            finished = True

        elif method == 2:

            # show animate function method 2 ...
            thread = Thread(target=animate_method_2, args=[speed])

            # start thread ...
            thread.start()

            # if sleep time ended break animate function ...
            zzz(sleep)

            # delete line ...
            stdout.write('\b \b'*int(resize))
            stdout.write(' '*int(resize)+'\033[0m\r')

            # if finished is True breaked animate method 2 function ...
            finished = True

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # create loading by function ...
    elif function is not None:

        # check function return value ...
        return_value = Queue()

        def storeInQueue(function):
            def returned(*args):
                try:
                    return_value.put(function(*args))
                except TypeError:
                    error(
                        'content of the \'argument\' argument does not match the arguments for \'function\' ...')
            return returned

        # redirect function stdout ...
        def redirect(f):
            def wrapper(*args, **kwargs):
                default_stdout = sys.stdout
                if ostype().upper() == 'LINUX':
                    sys.stdout = open('/dev/null', 'w')

                elif ostype().upper() == 'WINDOWS':
                    sys.stdout = open('file', 'w')
                try:
                    return f(*args, **kwargs)
                except TypeError:
                    error(
                        'content of the \'argument\' argument does not match the arguments for \'function\' ...')
                    return
                finally:
                    sys.stdout.close()
                    sys.stdout = default_stdout

            return wrapper

        # output is False , redirect function output ...
        if output is False:

            # if is arguments ...
            if argument is not None:

                # if type 'argument' is not list show error ...
                if type(argument) is not list:
                    error('argument \'argument\' must be a list type ...')
                    return

                # create thread ...
                thread = Thread(target=storeInQueue(
                    redirect(function)), args=argument)

            # if is not arguments ...
            elif argument is None:

                # create thread ...
                thread = Thread(target=storeInQueue(redirect(function)))

        # output is True , can't  redirect function output ...
        elif output is True:

            # if is argument ...
            if argument is not None:

                # create thread ...
                thread = Thread(target=storeInQueue(function), args=argument)

            # if is not arguments ...
            elif argument is None:

                # create thread ...
                thread = Thread(target=storeInQueue(function))

        # start thread and show loading ...
        thread.start()

        # if function is running ...
        while thread.isAlive():

            # selection method to show animate ...
            if method == 1:
                animate_method_1(speed)
            elif method == 2:
                animate_method_2(speed)

        # return function value ...
        return return_value.get()
