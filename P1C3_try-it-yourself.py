# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:49:48 2024

@author: nikumar
"""

# 3-1. Names: Store the names of a few of your friends in a list called names . Print
# each person’s name by accessing each element in the list, one at a time .
names = ['Gunda', 'Avi', 'Devadatta', 'Pratheek', 'Nitish', 'Shreyamsha']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-2])
print(names[-1])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them . The text of each mes-
# sage should be the same, but each message should be personalized with the
# person’s name .

message = "Hey there, "
print(message + names[0])
print(message + names[-2])


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples . Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle .”
favourites = ['BMW', 'Triumph', 'Kawasaki', 'RE Himalayan']
print('I love riding a ' + favourites[1] + ' bike in a forest trail')

# Changing, adding, and removing elements
favourites[0] = 'TVS' # modified first element as TVS

# adding element to a list
# using Append (adding at the end)
favourites.append('Pulsar')
print(favourites)

tvshow_list = []
tvshow_list.append('Game of Thrones')
tvshow_list.append('Breaking Bad')
tvshow_list.append('Two and a Half Men')
tvshow_list.append('The Simpsons')

# using Insert (adding by specifying position)
tvshow_list.insert(0, 'Silli Lalli') # 0 is the index. This shifts the other elements to the right
tvshow_list.insert(-1, 'Full House') # this does not add to the last but adds at the one before last. 

# removing elements
# using del
del favourites[-1] # this removes pulsar 

# using pop
states_travelled = ['MH', 'GA', 'UK', 'TN', 'KL', 'AP']

pop_state = states_travelled.pop()
print(states_travelled)
print(pop_state)

# using pop, specify the index to remove the element
states_travelled = ['MH', 'GA', 'UK', 'TN', 'KL', 'AP']
north_india = states_travelled.pop(2)
print(north_india)

# using pop, by default it removes the last element in the list and returns the value unlike del
states_travelled = ['MH', 'GA', 'UK', 'TN', 'KL', 'AP']
states_travelled.pop() # removes and returns 'AP'
del states_travelled[-1] # removes 'AP' but does not return


# removing an Item by Value
# remove
asian_countries = ['india', 'china', 'japan', 'indonesia', 'finland', 'sri lanka']

# we need to remove 'finland' value
asian_countries.remove('finland')

asian_countries = ['india', 'china', 'japan', 'indonesia', 'finland', 'sri lanka']
not_asia = 'finland'
asian_countries.remove(not_asia)
print(not_asia.title() + ' is not in Asia!')

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner . Then use your list to print a message to each person, inviting
# them to dinner .
invite_list = ['Poorna Chandra Tejaswi', 'Shivarama Karanth', 'Arsene Wenger', 'J.R.R Tolkien']
print('Respected ' + invite_list[0] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[1] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[2] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[3] + ', this is an invitation for the dinner.')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations . You’ll have to think of
# someone else to invite 
invite_list = ['Poorna Chandra Tejaswi', 'Shivarama Karanth', 'Arsene Wenger', 'J.R.R Tolkien']
print('Sorry to have been known that Mr.'+invite_list[-2]+ ' will not be attending the dinner.')
invite_list[-2] = 'Narendra Modi'
print('Respected ' + invite_list[0] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[1] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[2] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[3] + ', this is an invitation for the dinner.')


# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available . Think of three more guests to invite to dinner 
invite_list = ['Poorna Chandra Tejaswi', 'Shivarama Karanth', 'Narendra Modi', 'J.R.R Tolkien']
invite_list.insert(0, 'Rukmini Vasanth')
invite_list.insert(3, 'Swathi HC')
invite_list.append('Mammootty')

print('Respected ' + invite_list[0] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[1] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[2] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[3] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[4] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[5] + ', this is an invitation for the dinner.')
print('Respected ' + invite_list[6] + ', this is an invitation for the dinner.')

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests 

invite_list = ['Rukmini Vasanth',
 'Poorna Chandra Tejaswi',
 'Shivarama Karanth',
 'Swathi HC',
 'Narendra Modi',
 'J.R.R Tolkien',
 'Mammootty']

print('Unfortunately, we can only have two guests for the dinner :(')

removed_guest = invite_list.pop()
print('Respected '+ removed_guest.title() + ', Sorry for inconvenience caused.')

removed_guest = invite_list.pop()
print('Respected '+ removed_guest.title() + ', Sorry for inconvenience caused.')

removed_guest = invite_list.pop()
print('Respected '+ removed_guest.title() + ', Sorry for inconvenience caused.')

removed_guest = invite_list.pop(0)
print('Respected '+ removed_guest.title() + ', Sorry for inconvenience caused.')

removed_guest = invite_list.pop(1)
print('Respected '+ removed_guest.title() + ', Sorry for inconvenience caused.')

print('Dear '+ invite_list[0] + ', Happy to inform you that you are still invited.')
print('Dear '+ invite_list[1] + ', Happy to inform you that you are still invited.')

del invite_list[0]
del invite_list[0]

print(invite_list)

# Organize a list
# sort method (permanent!)
tvshow_list
tvshow_list.sort()
print(tvshow_list)
tvshow_list.sort(reverse=True)
print(tvshow_list)

# sorted method (temporary)
print(names)
print(sorted(names))
print(sorted(names, reverse=True))

# reverse method (not alphabetically, just reverse order)
# permanent
print(names)
names.reverse()
print(names)


# finding the length of a list
# len
print(names)
len(names)

# Python counts the items in a list starting with one, so you shouldn’t run into any off-
# by-one errors when determining the length of a list.


# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit .
# Store the locations in a list . Make sure the list is not in alphabetical order
places = ['Finalnd', 'London', 'Philippines', 'Mauritius', 'Peru', 'Alaska', 'San Francisco']

# Print your list in its original order . Don’t worry about printing the list neatly,
# just print it as a raw Python list .
print(places)

# Use sorted() to print your list in alphabetical order without modifying the
# actual list .
sorted(places)

# Show that your list is still in its original order by printing it .
print(places)

# Use sorted() to print your list in reverse alphabetical order without chang-
# ing the order of the original list 
sorted(places, reverse=True)

# Show that your list is still in its original order by printing it again .
print(places)

# Use reverse() to change the order of your list . Print the list to show that its
# order has changed .
places.reverse()
print(places)

# Use reverse() to change the order of your list again . Print the list to show
# it’s back to its original order .
places.reverse()
print(places)

# Use sort() to change your list so it’s stored in alphabetical order . Print the
# list to show that its order has been changed .
places.sort()
print(places)

# Use sort() to change your list so it’s stored in reverse alphabetical order .
# Print the list to show that its order has changed 
places.sort(reverse=True)
print(places)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner 
print(invite_list)
print('We have a total of', len(invite_list), 'guests invited for dinner')

# 3-10. Every Function: Think of something you could store in a list . For example,
# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like . Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.
print("I'm going to have to respectfully disagree on this one mate!")



# index error
# when we ask for more than what we currently have
sample_list = ['mango', 'apple', 'banana']
print(len(sample_list))

# print 4th element
print(sample_list[4])
# IndexError: list index out of range

# better way to get the last element in a list
print(len(sample_list))
# we got 3 as output. so, to get the last element we usually think of 3rd element
print(sample_list[3])
# but python counts from zero. so, the last element is at index 2
print(sample_list[2])
# banana

# instead, we can get the last element by giving -1
print(sample_list[-1])
# banana

# 3-11. Intentional Error: If you haven’t received an index error in one of your
# programs yet, try to make one happen . Change an index in one of your pro-
# grams to produce an index error . Make sure you correct the error before clos-
# ing the program .

my_super_list= ['i', 'have', 'a', 'dream']
print(len(my_super_list))

my_super_list[4]
# IndexError: list index out of range

my_super_list[-1]
# dream