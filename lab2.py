
# Due: February 6th at the beginning of class

# Joanna Veilleux

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re

solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print(s0 + "\n")

print(solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = r"^T"
s0 = "The quick brown fox"
if re.search(pattern, s0):
    print("It starts with 'T'!" + "\n")
else:
    print("My regex is incorrect, it should detect the 'T'!" + "\n")

print(solution_separator)

# 2) Use a regular expression to decompose the string into words and place those words into a list.
#    Extract the first word into a variable and print it
pattern = r"\s"
words = re.split(pattern, s0)
first_word = words[0]
print("The first word is: '" + first_word + "'\n")

print(solution_separator)

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
pattern = r'\s'
words = re.split(pattern, s0)
for word in words:
    print(word + "\n")

print(solution_separator)

# 4)
s1 = "Mary was born on September 17, 1986"

# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
if re.match(r"(Mary)\s", s1):
    print("I found Mary!")
else:
    print("I did not find Mary!")

# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
pattern = r'\d{4}'
if re.search(pattern, s1):
    print("I found the year!")
else:
    print("I did not find the year!")

# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
b_year = re.search(pattern, s1)
print("The person was born in", b_year.group(0))

print(solution_separator)

# 5)
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."

# a) Write a regular expression to match the word "dog", but not the name "Dog"
pattern = r'\bdog\b'

# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
dog_list = re.findall(pattern, s2)

# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
dog2_list = re.findall(pattern, s2, re.I)

# d) Write a regular expression to match "dog" or "fog"
pattern = r'\bdog\b|\bfog\b'
dog_fog_list = re.findall(pattern, s2)

# e) Print all outputs.
print("This is the first list of returned matches:", dog_list)
print("This is the second list of returned matches:", dog2_list)
print("This is the third list of matches:", dog_fog_list)

print(solution_separator)

# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
pattern = r'\d{5}?'
first_num = re.match(pattern, s3)
print("This is the first number that matches:", first_num.group())

# b) Write a regular expression to extract all numbers, store them in an j, then print the array.
pattern = r'\d{5}?'
all_nums = re.findall(pattern, s3)
print("These are all the 5 digit numbers that I found:")
for number in all_nums:
    print(number)

print(solution_separator)

# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
trimmed_string = re.sub(r'\A\s+|\s*\Z', "", s4)
print("This is the old string:")
print(s4)
print("This is the new string:")
print(trimmed_string)

print(solution_separator)

# 8)
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"

# a) Write a regular expression to print everything from the first "begin" to the last "end".
pattern = r'begin.*end'
begin_end_1 = re.search(pattern, s5)

# b) Write a regular expression to print only the text from the first "begin" to the first "end"
pattern = r'begin.*?end'
begin_end_2 = re.search(pattern, s5)

# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
pattern = r'begin.*?end'
begin_end_list = re.findall(pattern, s5)
# d) Print all outputs.
print(begin_end_1.group(0))
print(begin_end_2.group())
print(begin_end_list)

print(solution_separator)

# 9)
s6 = "The date 5/17/1982 is trickier to get"

# a) Write a regular expression to extract the date.
pattern = r'\d{1}\/\d{2}\/\d{4}'

# b) Capture the date in a variable f_date
f_date = re.search(pattern, s6)

# c) Split the date and store it as month, day, year
split_date = re.split(r"(/)", f_date.group(0))
month = split_date[0]
day = split_date[2]
year = split_date[4]

# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
pattern2 = r'\d{2}'

comp_date = year + "-"
if re.match(pattern2, month):
    comp_date += month + "-"
else:
    comp_date += '0' + month + "-"
if re.match(pattern2, day):
    comp_date += day
else:
    comp_date += '0' + day

# e) Print comp_date
print(comp_date)

print(solution_separator)

# 10) Extra Credit:
s8 = "These are some dates: 1/23/2011, 2/1/2006, 12/31/2007, 9/15/1993, 04/23/1797."

# a) Use a regex to collect the dates into a list
pattern = r'\d\/\d\/\d{4}|\d\/\d{2}\/\d{4}|\d{2}\/\d{2}\/\d{4}'
date_list = re.findall(pattern, s8)

# b) Use the code above to convert them into yyyy-mm-dd format.
pattern2 = r'\d{2}'
convert_date_list = []
for date in date_list:
    split_date = re.split(r"(/)", date)
    month = split_date[0]
    day = split_date[2]
    year = split_date[4]
    comp_date = year + "-"
    if re.match(pattern2, month):
        comp_date += month + "-"
    else:
        comp_date += '0' + month + "-"
    if re.match(pattern2, day):
        comp_date += day
    else:
        comp_date += '0' + day
    convert_date_list.append(comp_date)

# c) Print the dates in chronological order
convert_date_list.sort()
for date in convert_date_list:
    print(date)

print(solution_separator)
