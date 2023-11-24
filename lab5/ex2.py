import random
import re


def extract_words(input_file):
    with open(input_file, 'r') as file:
        text = file.read()
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        return words


def create_word_dictionary(words):  # function to create dictionary of unique words
    word_set = set(word.lower() for word in words)
    return list(word_set)


def generate_poem(word_dict, lines_per_strophe, words_per_line):  # function to generate a poem from the dictionary
    poem = []
    for _ in range(lines_per_strophe):
        line = ' '.join(random.choice(word_dict) for _ in range(words_per_line))
        poem.append(line)
    return poem


def save_poem(poem, output_file):  # function to save the poem into a file
    with open(output_file, 'w') as file:
        for line in poem:
            file.write(line + '\n')


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output_poem.txt"
    lines_per_strophe = int(input("Enter the number of lines per strophe: "))
    words_per_line = int(input("Enter the number of words per line: "))

    words = extract_words(input_file)  # extract the words from the file

    word_dict = create_word_dictionary(words)  # create the dictionary

    poem = generate_poem(word_dict, lines_per_strophe, words_per_line)  # create the poem

    save_poem(poem, output_file)  # save the poem

    print("Poem has been generated and saved to", output_file)
