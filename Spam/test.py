import sys


print set();

sys.exit();

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 108, 'Sloth' : 105, 'Burmese Python' : 106}

residents.update({'Nikhil':2121});

if('Sloth' in residents):
    print "sloth exists";

sys.exit();


print residents['Puffin'] # Prints Puffin's room number

for a in residents:
    print a,"::",residents[a]

print len(residents)

sys.exit();

#Add element dynamically in dictinaory



print residents

# Your code here!

aSet = set()
aSet = set("one") # a set containing three letters
#set(['e', 'o', 'n'])

aSet = set(['one', 'two', 'three'])
#set(['three', 'two', 'one'])
#a set containing three words

#iterate over set
for v in aSet:
    print v

sys.exit()

bSet = set(['three','four', 'five'])

#union
cSet = aSet | bSet
#set(['four', 'one', 'five', 'three', 'two'])

#intersection
dSet = aSet & bSet

#find elements in aSet not bSet
eSet = aSet.difference(bSet)

#add element
bSet.add("six")
#set(['four', 'six', 'five', 'three'])