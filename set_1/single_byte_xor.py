import string

message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

occurance_english = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}

def fixed_xor(chrstr1, chrstr2):
    """Takes two charachter strings of the same length and xors them against each other"""
    bar1 = bytes.fromhex(chrstr1)
    bar2 = (chrstr2).encode()
    return bytes(a ^ b for a, b in zip(bar1, bar2)).hex()

def generate_key(length):
    pos_keys = set(string.ascii_lowercase)
    for k in pos_keys:
        yield (k * length)

def decypher(m):
    clear_texts = []
    for key in generate_key(len(m)):
        clear_texts.append([bytes.fromhex(fixed_xor(m, key)).decode(), key])
    return clear_texts

def calc_fitting(text):


l = decypher(message)



print(l[1][0])
## TODO: use ioc to determine wich of the possible messages is the right one
