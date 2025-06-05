my_name = 'Jatin Sheoran'
my_age = 16 #Become 17 from 1 month now. As today is 21 July 2025
my_height = 78 #In inches. It is when I measured a long time ago
my_weight = 165 # I need to lose some weight
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

#An tricky line appears here
print("If I add %d, %d and %d I get %d." %(
    my_age, my_height, my_weight, my_age + my_height + my_weight))