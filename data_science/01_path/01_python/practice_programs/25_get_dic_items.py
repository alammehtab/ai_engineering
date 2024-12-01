# problem
# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

# solution
friends_fav_languages = {}

name = input("Your name: ")
lang = input("Your fav language: ")
friends_fav_languages.update({name: lang})

name = input("Your name: ")
lang = input("Your fav language: ")
friends_fav_languages.update({name: lang})

name = input("Your name: ")
lang = input("Your fav language: ")
friends_fav_languages.update({name: lang})

name = input("Your name: ")
lang = input("Your fav language: ")
friends_fav_languages.update({name: lang})

print(friends_fav_languages)
