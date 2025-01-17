def main(text_path):
    with open(text_path, 'r') as f:
        def sort_on(dictionary):
            return dictionary["count"]

        text = f.read()
        text_lower = text.lower()
        character_count = {}
        list_of_characters = []

        for character in text_lower:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1

        for i in character_count:
            character_dict = {"character": i, "count": character_count[i]}
            list_of_characters.append(character_dict)
        list_of_characters.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {text_path} ---")
        for character in list_of_characters:
            if character["character"].isalpha():
                print(f'The "{character["character"]}" character was found {character["count"]} times')
        word_count = len(text.split())
        print(f"Word count: {word_count}")
        print(f"--- End of report ---")

        print(text)


main('books/frankenstein.txt')
