# Q1
# Guests. If you could invite anyone, living or dead, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to dinner. Then 
# use your list to print a message to each person, inviting them to dinner.
Guests=['Kyle Lowry' ,'Masai Ujiri' ,'Fred Vanvleet']
Message = "! How are you?, Would you like to join me for dinner?"
print ("Hey " + (Guests[0]) + Message )
print ("Hey " + (Guests[1]) + Message)
print ("Hey " + (Guests[2]) + Message)
# Q2
# You just heard that one of the guests can't make the dinner, so you need to send out 
# a new set of invitiations. You'll have to think of someone else to invite
Guests.remove('Masai Ujiri')
Guests.append('Norman Powell')
Message = "! How are you? Join me for dinner."
print ( "\n\n Question 2")
print ("Hey " + (Guests[0]) + Message )
print ("Hey " + (Guests[1]) + Message)
print ("Hey " + (Guests[2]) + Message)


# - Start with your program from Q1. Add a print() call at the end of your program 
# stating the name of the guest who can't make it.
# - Modify your list, replacing the name of the guest who can't make it with the name 
# of the new person you are inviting.
# - Print a second send of invitation messages, one for each person who is still in your list.


# Q3
# You just found a bigger dinner table, so now more space is available. Think of three more 
# guests to invite to dinner.
#
# - Start with your program from Q1 and Q2. Add a print() call to the end of your program 
# informing people that you found a bigger dinner table
# - Use insert() to add one new guest to the beginning of your list.
# - Use insert() to add one new guest to the middle of your list.
# - Use append() to add one new guest to the end of your list.
# - Print a new set of inivitation messages, one for each person in your list.
print ( "\n\n Question 3")
Message = "! Let's party tonight."
Guests.append('Chris Boucher')
Guests.insert(0, 'Matt Thomas')
Guests.insert(3,'Aron Baynes')
print ("Hey " + (Guests[0]) + Message )
print ("Hey " + (Guests[1]) + Message )
print ("Hey " + (Guests[2]) + Message )
print ("Hey " + (Guests[3]) + Message )
print ("Hey " + (Guests[4]) + Message ) 
print ("Hey " + (Guests[5]) + Message ) 

# Q4
# Shrinking the guest list. You just found out that your new dinner table won't arrive in 
# time for the dinner, and you have space for only two guests.
#
# - Start with your program from Q3. Add a new line that prints a message saying that you 
# can invite only two people for the dinner.
# - Use pop() to remove guests from your list one at a time until only two names remain in 
# your list. Each time you pop a name from your list, print a message to that person letting 
# them know you are sorry that you can't invite them to dinner
# - Print a message to each of the two people still on your list, letting them know they 
# are still invited.
# - Use del to remove the last two names from your list, so you have an empty list. Print 
# your list to make sure you actually have an empty list at the end of your prog
print ( "\n\n Question 4")
print(' Sorry the new table did not arrive in time.')
Message = '! Sorry, I cannot invite you to dinner this time.'
popped_Guests=Guests.pop()
print ("Hey " + popped_Guests + Message )
popped_Guests=Guests.pop()
print ("Hey " + popped_Guests + Message )
popped_Guests=Guests.pop()
print ("Hey " + popped_Guests + Message )
popped_Guests=Guests.pop()
print ("Hey " + popped_Guests + Message )

Guests.sort()
Message = '! You are still invited.'
print ("Hey " + (Guests[0]) + Message )
print ("Hey " + (Guests[1]) + Message )


