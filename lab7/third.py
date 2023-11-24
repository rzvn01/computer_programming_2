import re


def count_sentences_and_nouns(text):
    # Split the text into sentences
    sentences = re.split(r'\.\s*', text)

    # Initialize counters
    sentence_count = len(sentences)
    noun_count = 0

    # Define a pattern for matching articles (THE, A, AN) followed by a noun
    pattern = re.compile(r'\b(?:THE|A|AN)\s+([A-Za-z]+)\b')

    # Iterate through sentences to find and count nouns
    for sentence in sentences:
        matches = pattern.findall(sentence)
        noun_count += len(matches)


    return sentence_count, noun_count


def print_results(sentence_count, noun_count):
    print("Number of Sentences:", sentence_count)
    print("Number of Nouns (substantives):", noun_count)


def main():
    # Get input string containing English sentences
    input_text = input("Enter the string containing English sentences: ")

    # Calculate the number of sentences and nouns
    sentence_count, noun_count = count_sentences_and_nouns(input_text)

    # Print the results
    print_results(sentence_count, noun_count)


if __name__ == "__main__":
    main()
