
# Mad Lib Exercise
# Demonstrate input and Output
# Demonstrate variables and strings
#
#
#
# Jack and Jill went up the hill to fetch a pail of water,
# Jack fell down and broke his crown and Jill came running after.
#
#
# Boy's name:
# Girl's name:
# Geologic formation:
# Verb:
# Container:
# Liquid:
# Body Part:
# ing verb:
#
# Example Output:
# John and Sam went up the mesa to run a lunchbox of pepsi.
# John fell down and broke his arm and Sam came running after.



# Now Create your own MadLib similar to the example below

boysName = input("Enter Boy's name: ")
girlsName = input("Enter Girl's name: ")
geologicFormation = input("Enter Geologic formation: ")
verb = input("Enter Verb: ")
container = input("Enter Container: ")
liquid = input("Enter Liquid: ")
bodyPart = input("Enter Body Part: ")
ing_verb = input("Enter verb ending in 'ing': ")

print(boysName,"and", girlsName, "went up the", geologicFormation,
      "to", verb, "a", container, "of", liquid + ".", boysName,
      "fell down and broke his", bodyPart, "and", girlsName, "came",
      ing_verb, "after.")


