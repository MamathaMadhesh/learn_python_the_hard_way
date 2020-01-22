#Prompting and passing

from sys import argv

script,user_name=argv

print(f"Hi {user_name} I'm the{script} script")
print("I'd like you to ask few questions")
print("Do like me {}?".format(user_name))

likes=input()
print(f"Where do you live {user_name}?")
place=input()

print("What kind of computer do you have?")
computer=input()

print(f"""
      All right you said {likes} about liking me.
      You live in {place}.Not sure where it is
      And you have {computer} computer.Nice""")