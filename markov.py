"""Generate Markov text from text files."""
import random

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    return contents

    #return 'Contents of your file as one long string'

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    chains = {}

    for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        value = words[i+2]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]
    return chains


def make_text(chains):
    """Return text from chains."""
    words = [] #create an empty list of strings

    keys_list = chains.keys()
    random_key = (random.choice(list(keys_list))) #tuple
   
    value = random.choice(chains[random_key]) #string
    
    link = [random_key[0], random_key[1], value] #list

    words.extend(link) #list of strings

    key = (words[-2], words[-1])
    
    while key in chains:
        value = random.choice(chains[key]) #string
        words.append(value)
        key = (words[-2], words[-1]) #tuple
   
    word_string = " ".join(words)
    return word_string


# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)
# chains = make_chains(input_text)
# text = make_text(chains)

# ***make_chains(text)
# # Produce random text
# #random_text = make_text(chains)

# #print(random_text)
input_path = 'green-eggs.txt'
input_text = open_and_read_file(input_path)
chains = make_chains(input_text)
random_text = make_text(chains)
print(random_text)

# for make_chains:
# incorporate none object  (checking if keys = none)
# add none into words
# if not none: keep going. if none, then stop