"""Generate Markov text from text files."""

import random
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string, number=3):
    """Take input text as string and number for creating n-gram; 
        return dictionary of Markov chains. """

    # break string into words
    words = text_string.split()
    
    chains = {}
    
    # break words into n-grams & create the dictionary
    for i in range(len(words) - (number + 1)):
        key = tuple(words[i:(i + number)])
        print(key)
        value = words[i + 1 + number]
        print(value)
        chains[key] = (chains.get(key, []) + [value])
        # if key not in chains:
        #     chains[key] = []

        # chains[key].append(value)

        

        # chains[(words[i], words[i + 1])] = (chains.get((words[i], 
        # words[i + 1]), []) + [words[i + 2]])    
    
    #print(chains)
    return chains   


def make_text(chains, number=2):
    """Return text from chains."""

    word_list = []

    # # choose a first key put those words in the list
    #     # choice(chains)  # <-- Can I rando choose from a dict?
    link_one = random.choice(list(chains.keys()))
    word_list.extend(list(link_one))
    #print(word_list)

    pick = random.choice(chains[link_one])
    word_list.append(pick)

    key_error = False

    # Build the chain by creating more bigrams
    while key_error is False:
        try:
            next_link = tuple(word_list[-1 * number:])

            # Check if the bigram exists
            if chains[next_link] == chains.get(next_link):
                pick = random.choice(chains[next_link])
                word_list.append(pick)
                key_error = False   

            # If not, raise the error that will produce an output, instead of 
            # an error message    
            else:
                raise KeyError

        except KeyError:
            return(" ".join(word_list))
            key_error = True


input_path = sys.argv[1]
number = int(input("How many words in the n-gram?: "))

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
