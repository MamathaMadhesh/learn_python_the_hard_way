print("Let's Practice Everything")
print("you\' d need to know \'bout escapes with  \\ that do :")
print("\n newline and \t tabs")

poem="""
\t the Lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)

print("-------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,carets = secret_formula(start_point)

#remember that this is another way to format a string
print("With a Starting point of: {}".format(start_point))
#it's just likw with an f"" string
print(f"we\'d have {beans} beans, {jars} jars and {carets} carets.")
start_point = start_point / 10
print("we can also do that this way")
formula = secret_formula(start_point)
print("we\'d have {} beans,{} jars  and {} carets".format(*formula))