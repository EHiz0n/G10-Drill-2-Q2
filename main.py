# Working with sets
from pyscript import display

A = {'Robert, Victor, Tax, Alice'}
B = {'Robert', 'Seth', 'Alice', 'Abby'}

only_first = A - B
only_second = B - A
in_a_club = A | B
in_both = A & B
exactly_one = A ^ B

display("Fencing Club: " + str(A), target="output")
display("TKD Club: " + str(B), target="output")
display("Students only in Fencing: " + str(only_first), target="output")
display("Students only in TKD: " + str(only_second), target="output")
display("Students in a club: " + str(in_a_club), target="output")
display("Students in both clubs: " + str(in_both), target="output")
display("Students in exactly one club: " + str(exactly_one), target="output")