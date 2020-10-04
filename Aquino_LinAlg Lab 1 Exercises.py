#!/usr/bin/env python
# coding: utf-8

# # Linear Algebra (CpE210A)

# ### Laboratory 1: Getting acquainted with Python

# Coded and submitted by:

# Aquino, John Benedict U.

# Section: 58010

# In[14]:



'''
GRADED CELL 1 (50 points)
Try to replicate the output shown below using the variables below.
Note: Shorter the code higher the points!

Score Matrix:
Working        |Lines        |Points
Yes            |3 or less    |100%
Yes            |4 or more    |90%
No             |1 or more    |70%
No             |0            |0%

Pro score: 1 line. --> +5 points (+10 with explanation)
party = ['Charmander', 'Pidgey', 'Sandshrew', 'Rattata', 'Abra']
levels = [15, 11, 18, 5, 14]
'''


# In[11]:


party = ["Charmander", "Pidgey", "Sandshrew", "Rattata", "Abra"]; levels =[15, 11, 18, 5, 14];
for parties, level in zip(party, levels):
    print(parties, "at level", level)


# CODE IMPLEMENTAION: The process of this code is the for loop will iterate the sets of string inside the zip(party) and zip(levels), and then print each iterated string of each.

# In[13]:


'''
GRADED CELL 2 (10 points)
Problem 1: You are missing 1 more pokémon to complete your team. Listed below are your reserves.
Identify the top 3  highest or lowest level pokémon and store them in a variable 'picks'. (Choose only one path)

Score Matrix:
Working        |Lines         |Points
Yes            |20 or less    |100%
Yes            |21 or more    |90%
No             |1 or more     |70%
No             |0             |0%

Pro score: 1 line --> +30 points (+50 with explanation)
Tip: try to search about sort(), sorted(), and append().
'''
reserves = [
    ('Onix',10),
    ('Slowpoke',18),
    ('Dialga', 2),
    ('Magikarp', 32),
    ('Feebas', 22),
    ('Swablu', 19),
    ('Regigigas', 3),
    ('Unown', 50)
]


# In[205]:


reserves = [
    ('Onix',10),
    ('Slowpoke',18),
    ('Dialga', 2)
    ('Magikarp', 32),
    ('Feebas', 22),
    ('Swablu', 19),
    ('Regigigas', 3),
    ('Unown', 50)
]
reserves.sort(key=lambda row: row[1])
print("['"+ str (reserves[0][0])+"', '"+ str (reserves[1][0])+"', '"+ str (reserves[2][0])+"']")
print("['"+ str (reserves[-1][0])+"', '"+ str (reserves[-2][0])+"', '"+ str (reserves[-3][0])+"']")


# CODE IMPLEMENTAION:On this program, I make a code to identify and separate the pokemons and group them according to their level.

# In[19]:


'''
GRADED CELL 3 (40 points)
Create a function named "create_party" that will add the chosen pokémon from graded cell 3 to the party from graded cell 1.
The function should display all the possible parties while keeping the original members of the party.
Note: A party should only have 6 pokémon.

Score Matrix:
Working        |Lines         |Points
Yes            |20 or less    |100% 
Yes            |21 or more    |90%
No             |1 or more     |70%
No             |0             |0%

Pro score: 1 line --> +30 points (+50 with explanation)
Tip: try to search about sort(), sorted(), and append().
'''
def create_party(party, candidates):
    return suggested_parties


# In[208]:


party = ["Charmande", "Pidgey", "Sandshrew", "Rattata", "Abra"]
candidates = ["Unown", "Magikarp", "Feebas" ]

def create_party(party, candidates):
    for item in candidates:
        (print(party + list(item)))
    return party
create_party(party, candidates)


# CODE IMPLEMENTATION: Here I defined a function create_party() function for the sets of the party and the candidates, and then combine the set party with each of the items inside the set candidate before printing. As seen in the result each item in the set candidate is now included in a set party.
