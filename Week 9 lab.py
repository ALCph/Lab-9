#1.) Course Information

# Making the Dictionaries
rooms = {'CS101' : 3004, 
        'CS102' : 4501, 
        'CS103' : 6755,
        'NT110' : 1244,
        'CM241' : 1411,}

teachers = {'CS101' : 'Haynes', 
        'CS102' : 'Alvarado', 
        'CS103' : 'Rich',
        'NT110' : 'Burke',
        'CM241' : 'Lee',}

time = {'CS101' : '8:00 am', 
        'CS102' : '9:00 am', 
        'CS103' : '10:00 am',
        'NT110' : '11:00 am',
        'CM241' : '1:00 pm',}

# Getting user input
orig = input('Enter a course number:')
selection = orig.upper()
# Printing the output
if selection in rooms and selection in teachers and selection in time:
    print(f'{selection} meets in room: {rooms[selection]}')
    print(f'The instructor is: {teachers[selection]}')
    print(f'The meeting time is: {time[selection]}')
else:
    print('Enter a valid course number')
#==============================================

#2.) Capital Quiz

# A massive dictionary
state_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

# Counter variables
num_states = 5
correct_answer = 0
incorrect_answer = 0

# a loop to select a random state and get some input
for i in range(num_states):
    state, capital = state_capitals.popitem()
    print('What is the capital of ', state, '?')
    user_answer = input('')

    if user_answer.lower() == capital.lower():
        correct_answer += 1
        print('Correct!')
    else:
        incorrect_answer += 1
        print('Incorrect!')

# Printing the output
print(f'The total number of correct answers is: {correct_answer} out of 5')
#==============================================

#3.) File decryption and codes
# I wasn't sure if you wanted us to do this problem
#==============================================

#4.) Unique words

# An empty set to store the unique words
unique_words = set()

# Opening the file and a loop to get the words
with open('words.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            unique_words.add(word.lower())

# Printing the output
print("Unique words in the file:")
print(unique_words)
#==============================================

#5.) Word Frequency

# Empty dictionary for the loop
word_count = {}

# Opening the file, getting the words, and running a loop
# The words are being turned into lowercase to ensure they are counter properly
with open('words.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# Printing the output
for word, count in word_count.items():
    print(f"The word {word} was repeated: {count} times.")
#==============================================

#6.) File analysis
# A problem about comparing two files

# Opening two files and putting their contents into a set
# I went with words1 and words2 to keep it simple
with open('words1.txt', 'r') as file1:
    words1 = set(file1.read().split())
with open('words2.txt', 'r') as file2:
    words2 = set(file2.read().split())

# Operations to compare the sets, and printing the output
words_combined = words1.union(words2)
print("All words in words1 and words2 in one set:")
print(words_combined)

words_both = words1.intersection(words2)
print("Words that appear in both files:")
print(words_both)

words1_only = words1.difference(words2)
print("Words that are only found in words1:")
print(words1_only)

words2_only = words2.difference(words1)
print("Words that only appear in words2:")
print(words2_only)

words_unshared = words1.symmetric_difference(words2)
print("Words that are in words1 and words2, but not in both:")
print(words_unshared)

