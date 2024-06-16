import unicodedata


def display_character_info(character):
    try:
        # Get the Unicode name of the character
        character_name = unicodedata.name(character)
        print(f"The Unicode name of '{character}' is: {character_name}")
    except ValueError:
        print(f"No Unicode name found for character: {character}")


def find_character_by_name(name):
    try:
        # Lookup the character by its Unicode name
        character = unicodedata.lookup(name)
        print(f"The character for Unicode name '{name}' is: {character}")
    except KeyError:
        print(f"No character found for Unicode name: {name}")


# Example usage for a book management system
display_character_info("A")  # Display info for the character 'A'
find_character_by_name("LEFT CURLY BRACKET")  # Find character by name
