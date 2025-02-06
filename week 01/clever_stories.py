"""
Author: Santiago Bergerat
Purpose: Clever Stories Task 02
This program generates a fun story by filling in a template with user-provided words.
I added the option to choose between two templates to make it more interesting.

"""

def choose_preposition(word):
    vowels = 'aeiou'
    return 'an' if word[0].lower() in vowels else 'a'


print("Welcome to Clever Stories!")
print("You will be asked for some words to create your own story.\n")



# Story selection by user
print("Choose a story template:")
print("1. The hallway adventure")
print("2. The backyard surprise")
option = input("Enter 1 or 2: ").strip()



# Ask the user for words in vars
print("\nPlease enter the following words:")
adjective = input("Adjective: ").strip().lower()
animal = input("Animal: ").strip().lower()
verb_1 = input("Verb: ").strip().lower()
exclamation = input("Exclamation: ").strip().capitalize()
verb_2 = input("Another verb: ").strip().lower()
verb_3 = input("One more verb: ").strip().lower()



# Generate the story based on the selected option
if option == "1":
    story = (
        f"The other day, I was really in trouble. It all started when I saw {choose_preposition(adjective)} "
        f"{adjective} {animal} {verb_1} down the hallway. \"{exclamation}!\" I yelled. But all I could think to do "
        f"was to {verb_2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_3} "
        f"right in front of my family."
    )
elif option == "2":
    story = (
        f"One sunny afternoon, I saw {choose_preposition(adjective)} {adjective} {animal} {verb_1} in my backyard. "
        f"\"{exclamation}!\" I screamed. Without thinking, I started to {verb_2}. To my surprise, it began to {verb_3}!"
    )
else:
    story = "Invalid choice. Please restart the program and try again."

# Display the story
print("\nYour story is:\n")
print(story)