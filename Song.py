#Drake Pierce-Demksi


def custom_song(verb1, noun1, adjective1, noun2, verb2, adjective2, noun3, place1):
    song = f"""
    Because I'm {verb1}, {noun1} along if you feel like a room without a roof
    Because I'm {verb1}, {noun1} along if you feel like happiness is the truth
    Because I'm {verb1}, {noun1} along if you know what happiness is to you
    Because I'm {verb1}, {noun1} along if you feel like that's what you wanna do

    Here comes bad {noun2}, {verb2} this and that, yeah!
    Well, give me all you got, don't hold back, yeah!
    Well, I should probably warn you I'll be just fine, yeah!
    No offense to you, don't waste your time. Here's why...

    Because I'm {adjective1}, clap along if you feel like a {adjective2} {noun3} in the {place1}
    """
    print(song)

# Collect user input
verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")
adjective2 = input("Enter another adjective: ")
noun3 = input("Enter yet another noun: ")
place1 = input("Enter a place: ")

# Call the custom_song function with user inputs as named arguments
custom_song(verb1, noun1, adjective1, noun2, verb2, adjective2, noun3, place1)
