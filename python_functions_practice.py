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

#FURTHER HOMEWORK

def volume_of_cube (side_length):
    return side_length ** 3

def reverse_a_string(the_string):
    return the_string[::-1]

def fahrenheit_to_celsius(fahrenheit):
    return fahrenheit - 273.15