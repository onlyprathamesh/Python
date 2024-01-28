# Nesting Dictionary in a Dictionary
dict = {
    "India" : {"Cities" : ["Pune", "Bengluru", "Delhi"],
               "Hign_Population" : ["UttarPradesh", "MadhyaPradesh"],
               "Best Cities" : {"Pune", "Mumbai", "Benguluru", "Kerla", "Delhi"},
               "Salary" : 50000
                },
    "USA" : {"Cities" : ["NewYork", "Texas", "Washington", "California"],
               "Hign_Population" : ["Don't know", "Don't know"],
               "Best Cities" : {"Los Angeles", "NewYork", "Las Vegas", "California", "Texas"},
               "Salary" : 100000
                }
}

# print(dict["India"])
# print(dict["USA"])

# Nesting a dictionary inside a list

list = [
    {"Country" : "India",
     "Cities" : ["Pune", "Bengluru", "Delhi"],
     "Hign_Population" : ["UttarPradesh", "MadhyaPradesh"],
     "Best Cities" : {"Pune", "Mumbai", "Benguluru", "Kerla", "Delhi"},
     "Salary" : 50000
            
    },
    {"Country" : "USA",
     "Cities" : ["NewYork", "Texas", "Washington", "California"],
     "Hign_Population" : ["Don't know", "Don't know"],
     "Best Cities" : {"Los Angeles", "NewYork", "Las Vegas", "California", "Texas"},
     "Salary" : 100000
    }
]

print(list[1])