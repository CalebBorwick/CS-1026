#Only hold unique values
cast = {"luigi", "Mario", "Peach"}

# can make a set from a list
names = ["luigi", "Mario", "Peach"]
cast = set(names)

#to create a empty set
cast = set()

#can use len of a set
#can use in or not in for a set


#to use sort function it returns a list not a set

#adding elements
cast.add("bowser")

#removing elements
cast.discard("Peach")
# can use .remove but may raise an exception

#empty the set
cast.clear()

#subsets
canadian = { "Red", "White" }
british = { "Red", "Blue", "White" }
italian = { "Red", "White", "Green" }

# True
if canadian.issubset(british) :
    print("All Canadian flag colors occur in the British flag.")
# True
if not italian.issubset(british) :
    print("At least one of the colors in the Italian flag does not.")

#can use == only if elements are the same
french = { "Red", "White", "Blue" }
if british == french :
    print("The British and French flags use the same colors.")

#union() returns a new set with all elements from boths sets without duplicates
inEither = british.union(italian)

#intersection() gives a set with values that are sharred between 2 sets
inBoth = british.intersection(italian)

#differnce() gives a set of all elements that are in the first set but not the second
print("Colors that are in the Italian flag but not the British:")
print(italian.difference(british)) 
