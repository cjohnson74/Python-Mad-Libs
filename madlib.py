# Init Variables
theMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

profession = ["","","",""]
adj = ["","","",""]

# Get Input From User
print("Welcome user!");
print("Let's play a game of madlibs!");
neo = input("please share with me your name?\n");

print(f"Hello {neo}! are you ready?")
theMatrix = input("What is something you want to know more about?")

print(f"Ooooh! You want to know more about {theMatrix} huh?")
print(f"Okay well first, tell me what you already know about {theMatrix}")
system = input(f"What noun would you categorize {theMatrix} as:")

enemy = input(f"Give me an opposing noun to {system}")

inside = input(f"Now give me any relaxing noun (present tense)")

# Init Story
madlibsStory = (f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. But when you're {inside}, you look around, what do you see? {profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. The very minds of the people we are trying to {save}. But until we do, these people are still a part of that {system} and that makes them our {enemy}. You have to understand, most of these people are not ready to be {unplugged}. And many of them are so {adj[0]}, so hopelessly {adj[0]} on the {system}, that they will {fight} to protect it.")

# Print Story
print(madlibsStory)