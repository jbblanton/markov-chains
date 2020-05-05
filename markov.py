"""Generate Markov text from text files."""

from random import choice

input_path = "green-eggs.txt"

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents
    #print(contents.split())

#print(open_and_read_file(input_path))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains. """

    # break string into words
    words = open_and_read_file(text_string).split()

    # break words into pairs
    chains = {}
    
    for i in range(len(words) - 2):
        chains[(words[i], words[i + 1])] = words[i + 2]
    
    # return chains
    print(chains)

print(make_chains(input_path))    

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
##chains = make_chains(input_text)

# Produce random text
##random_text = make_text(chains)

##print(random_text)
