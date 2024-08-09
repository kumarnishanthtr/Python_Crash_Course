# 6-1. Person: Use a dictionary to store information about a person you know .
# Store their first name, last name, age, and the city in which they live . You
# should have keys such as first_name, last_name, age, and city . Print each
# piece of information stored in your dictionary 

swathi_dict = {
    'first_name' : 'Swathi',
    'last_name' : 'Hebbar',
    'age' : 33,
    'city' : 'Bangalore',
    }

print(swathi_dict['first_name'])
print(swathi_dict['last_name'])
print(swathi_dict['age'])
print(swathi_dict['city'])


# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers .
# Think of five names, and use them as keys in your dictionary . Think of a favorite
# number for each person, and store each as a value in your dictionary . Print
# each person’s name and their favorite number . For even more fun, poll a few
# friends and get some actual data for your program

fav_numbers = {
    'Nishanth' : 14,
    'Swathi' : 12,
    'Ronaldo' : 7,
    'Ozil' : 10,
    'Fabregas' : 4,
    'Robin van Persie' : 11,
    }

print("Favourite number of Nishanth is " + str(fav_numbers['Nishanth']))
print("Favourite number of Ozil is " + str(fav_numbers['Ozil']))


# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary .
# However, to avoid confusion, let’s call it a glossary .
# 
# Think of five programming words you’ve learned about in the previous
# chapters . Use these words as the keys in your glossary, and store their
# meanings as values .
#
# Print each word and its meaning as neatly formatted output . You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line . Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output .
german_dict = {
    'die Frau' : 'Woman',
    'Lustig' : 'Funny',
    'das Ort' : 'Place / Town',
    'die Welt' : 'World',
    'der Vater' : 'Father',
    }

print("'die Frau' in German means: \n " + german_dict['die Frau'])
print("'Lustig' in German means: \n " + german_dict['Lustig'])
print("'die Welt' : " + german_dict['die Welt'])

