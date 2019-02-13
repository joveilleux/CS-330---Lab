"""Lab 3: Regexes and reformatting."""

# Joanna Veilleux

#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
# Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
#
#######################################
import re

# this is the old contact list

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]

print('\nThis is the old list of contacts: \n')
for contact in contacts:
    print(contact)

print("\n\n_______________________________________________________________________________\n\n")

# for every contact, separate all information into a list, then append that list to a new list of contacts
split_contact_list = []
for contact in contacts:
    contact_split = re.split(r"(,)", contact)
    split_contact_list.append(contact_split)

print("This is a list of contact lists:\n ")
for contact in split_contact_list:
    print(contact)

print("\n\n_______________________________________________________________________________\n\n")

# create lists to hold the names, phone, and location of each contact
contact_name = []        # Name = [0]
contact_phone = []       # Phone = [2]
contact_location = []    # Location = [4]

for contact in split_contact_list:
    contact_name.append(contact[0])
    contact_phone.append(contact[2])
    contact_location.append(contact[4])

print("This is a list of all contact names:\n")
for name in contact_name:
    print(name)

print("\nThis is a list of all contact phone numbers:\n")
for phone in contact_phone:
    print(phone)

print("\nThis is a list of all contact locations:\n")
for location in contact_location:
    print(location)

print("\n\n_______________________________________________________________________________\n\n")

# strip phone of any parenths, dashes, spaces, and leading 1's so we can reformat later
format_phone_list = []
for phone in contact_phone:
    phone = re.sub(r"[()]", "", phone)
    phone = re.sub(r"[-]", "", phone)
    phone = re.sub(r"^1", "", phone)
    phone = re.sub(r" ", "", phone)

    # format to (XXX) XXX-XXXX
    split_phone = list(phone)
    format_phone = "(" + split_phone[0] + split_phone[1] + split_phone[2] + ")" + \
                   split_phone[3] + split_phone[4] + split_phone[5] + "-" + \
                   split_phone[6] + split_phone[7] + split_phone[8] + split_phone[9]
    format_phone_list.append(format_phone)

print("This is a list of all of the reformatted phone numbers:\n")
for phone in format_phone_list:
    print(phone)

print("\n\n_______________________________________________________________________________\n\n")

# split the names on the spaces
name_split_list = []
for name in contact_name:
    split = re.split(r"(\s)", name)
    name_split_list.append(split)

print("\nThis is the list of split names\n")
for name in name_split_list:
    print(name)

print("\n\n_______________________________________________________________________________\n\n")

# create lists to hold the first(and middle if exists) and last name
first_list = []     # First Name = [0]
last_list = []      # Last Name = [4]

# need to account for if there is no middle name
# if the length of name array is 3: has no middle name
for name in name_split_list:
    if len(name) == 3:
        first_list.append(name[0])
        last_list.append(name[2])
    else:
        last_list.append(name[4])
        first_name = name[0] + " " + name[2]    # Middle Name = [2]
        first_list.append(first_name)

print("This is a list of all contact's first(& middle if present) names:\n")
for first in first_list:
    print(first)

print("\nThis is a list of all contact's last names:\n")
for last in last_list:
    print(last)

print("\n\n_______________________________________________________________________________\n\n")

# put everything back together into one list where:
# last name = [0]
# first name (& middle) = [1]
# location = [2]
# phone = [3]

new_contact_list = []
for i in range(len(contacts)):
    new_contact = []
    new_contact.append(last_list[i])
    new_contact.append(first_list[i])
    new_contact.append(contact_location[i])
    new_contact.append(format_phone_list[i])
    new_contact_list.append(new_contact)

# this is the new contact list with name, location, phone
print("This is an iteration of the list of correctly formatted contacts:\n")
for item in new_contact_list:
    print(item[0] + ', ' + item[1] + '\n' + item[2] + '\n' + item[3])
    print('--------------------')

print("\n\n_______________________________________________________________________________\n\n")

# sort the names alphabetically, by last name, ascending (A-Z)

# this sorts, but from Z-A
temp = []
for i in range(len(new_contact_list) - 1):
    for j in range(len(new_contact_list) - 1):
        current_contact = new_contact_list[j][0]
        next_contact = new_contact_list[j+1][0]
        if current_contact < next_contact:
            temp = new_contact_list[j+1]
            new_contact_list[j+1] = new_contact_list[j]
            new_contact_list[j] = temp

# make the correctly sorted list by iterating new_contact_list backwards and appending to sorted_list
sorted_list = []
for i in range(len(new_contact_list) - 1, -1, -1):
    sorted_list.append(new_contact_list[i])

print("These are your contacts, sorted alphabetically by last name: \n")

for item in sorted_list:
    print(item[0] + ', ' + item[1] + '\n' + item[2] + '\n' + item[3])
    print('--------------------')
