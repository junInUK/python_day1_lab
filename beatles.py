# Meet the Beatles:

def get_all_member_names(band):
    name_array = []
    for member in band:
        name_array.append(member["name"])
    return name_array 

def get_all_alive_member(band):
    members = []
    for member in band:
        if None == member["death_year"]:
            members.append(member)
    
    return members


# user = {
# 	"name": "John",
# 	"age": 37,
# 	"pupils": ["Gill", "Gerry", "Mike", "Sally"]
# }

# Use the `beatles` list above to answer the following questions:

# 1. John Lennon also plays guitar. Access the `instrument` key in his dictionary and change its value: OK

# 2. Write a function which takes in the list of band members as a parameter,
#    and returns a list of all the Beatles' names:
# Expected result: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr'] OK

# 3. Write a function which takes in the list of band members as a parameter,
#    and returns a list of the members who are still alive
#    (i.e. they have no value for `death_year`)
#    Return the full dictionary for each member
# Expected result: [
#    {'name': 'Paul McCartney', 'birth_year': 1942, 'death_year': None, 'instrument': 'bass'},
#    {'name': 'Ringo Starr', 'birth_year': 1940, 'death_year': None, 'instrument': 'drums'}
# ]   OK

# 4. Combine the above two functions to return the names of all the members who are alive:
# Expected result: ['Paul McCartney', 'Ringo Starr']  OK
