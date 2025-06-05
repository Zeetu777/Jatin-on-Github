#In next for line telling what x, binary, do_not, y are respectevely.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#Printing x and y.
print(x)
print(y)

#Same print is used here but it is including %r, %x, %s, %y.
print("I said : %r." % x)
print("I also said: '%s'." % y)

#Representing hilarious and joke_evaluation.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#printing hilarious and joke_evaluation.
print(joke_evaluation % hilarious)

#Representing w and e.
w = "This is the left side of..."
e = "a string with a right side."

#printing the sum of w and e.
print(w + e)