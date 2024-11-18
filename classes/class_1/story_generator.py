# Request user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
profession = input("Enter a profession: ")
item = input("Enter an object: ")
action = input("Enter an action: ")

# Story template
story = f"""
Once upon a time in a place called {place}, there lived a {profession} named {name}. 
One day, {name} found a magical {item} that could {action}. 
From that day on, {name}'s life changed forever.
"""

# Print the complete story
print(story)