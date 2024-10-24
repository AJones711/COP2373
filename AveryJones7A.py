
import re

def main():
    sentences = []
    # Establishing pattern
    pat = r'.*?[.?!]'

    print("Enter sentences (type 'exit' to finish):")

    # Collecting input until exit is typed
    while True:
        s = input()
        if s.lower() == 'exit':
            break
        sentences.append(s)

    # Joining all sentences into one string for processing
    combined_sentences = ' '.join(sentences)
    lst = re.findall(pat, combined_sentences, flags=re.DOTALL)

    # Stripping whitespace and printing entered sentences
    print("\nYou entered the following sentences:")
    for i, sentence in enumerate(lst, start=1):
        print(f"{i}: {sentence.strip()}")

    # Printing the sentence count
    print('There are', len(lst), 'sentences.')


main()