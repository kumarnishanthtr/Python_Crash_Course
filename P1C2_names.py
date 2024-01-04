# `title()` displays each word in titlecase, where each word begins with a capital letter.

name = "danny TaNNer"
print(name.title())

# other methods dealing with case
print(name.upper())
print(name.lower())

first_name = "danny"
last_name = "tanner"

full_name = first_name + last_name
print(full_name)
# this just prints without any spaces because it simply concatenates the two strings

full_name = first_name + ' ' + last_name
print(full_name)
# here we have added a space to respect the naming conventions

first_name = "danny"
last_name = "tanner"
full_name = first_name + ' ' + last_name
print('Hello ' + full_name.title() + ', ' + 'Welcome to the course!')


greeting = 'Hello ' + full_name.title() + ', ' + 'Welcome to the course!'
print(greeting)

# adding a tab to the text \t
print('Bangalore')
print('\tBangalore')

# adding a newline \n
print('New line coming \nSoon')

# we can combine both newline and tab
print('My favorite characters in Full House \n\tSteph \n\tJesse \n\tJoey (Cut. It. Out)')

# removing whitespaces
fav_character = 'Steph '
'Steph' == fav_character # this comes False because one string has an extra space in the right which is not visible easily
fav_character = fav_character.rstrip()
'Steph' == fav_character # now it is True

fav_show = ' Full House'
'Full House' == fav_show # this comes False because one string has an extra space in the left which is not visible easily
fav_show = fav_show.lstrip()
'Full House' == fav_show # now it is True

# removing whitespace from both direction
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

