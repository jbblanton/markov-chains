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


def make_chains(text_string, number=2):
    """Take input text as string and number for creating n-gram; 
        return dictionary of Markov chains. """

    # break string into words
    words = text_string.split()
    
    chains = {}
    
    # break words into n-grams & create the dictionary
    for i in range(len(words) - (number + 1)):
        key = tuple(words[i:(i + number)])
        
        value = [words[i + number]]
        
        chains[key] = (chains.get(key, []) + list(value))
        # if key not in chains:
        #     chains[key] = []

        # chains[key].append(value)

    chain_length = len(key)    

        # chains[(words[i], words[i + 1])] = (chains.get((words[i], 
        # words[i + 1]), []) + [words[i + 2]])    
    
    print(chains)
    return chains   


def make_text(chains, number=2):
    """Return text from chains."""

    word_list = []

    # # choose a first key put those words in the list
    link_one = random.choice(list(chains.keys()))
    word_list.extend(list(link_one))
    print("starting:", word_list)

    pick = random.choice(chains[link_one])
    word_list = word_list + [pick]
    print("next:", word_list)

    key_error = False

    # Build the chain by creating more n-grams
    while key_error is False:
        try:
            next_link = tuple(word_list[(-1 * number):])
            print("next link:", next_link)

            # Check if the n-gram exists
            if next_link in chains:
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
chains = make_chains(input_text, number)

# Produce random text
random_text = make_text(chains, number)

print(random_text)
