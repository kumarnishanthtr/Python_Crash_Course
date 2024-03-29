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
