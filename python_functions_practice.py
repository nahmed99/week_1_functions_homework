import calendar

def return_10():
    #pass #intentionally left empty
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(the_string):
    return len(the_string)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number( str_1, str_2 ):
    return int(str_1) + int(str_2)

def number_to_full_month_name( month ):
    return calendar.month_name[month]

def number_to_short_month_name(month):
    return calendar.month_abbr[month]
