# Implemented IOC detection and the IOC gets calculated correctly, but for this task it seems not to be the best method to find the answer because of to many non letters.
# Becuase I could not find a propper source for fitting qutioent, I copied someone elses impelementation: https://arpit.substack.com/p/deciphering-single-byte-xor-ciphertexts

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
    """Takes two charachter strings of the same length and xors them against
    each other"""
    bar1 = bytes.fromhex(chrstr1)
    bar2 = (chrstr2).encode()
    return bytes(a ^ b for a, b in zip(bar1, bar2)).hex()

def generate_key(length):
    pos_keys = set(string.ascii_lowercase)
    for k in pos_keys:
        yield (k * length)

def decypher(m):
    """Decypher a given message with single charachter key form lowercase
    letters"""
    clear_texts = []
    for key in generate_key(len(m)):
        clear_texts.append([bytes.fromhex(fixed_xor(m, key)).decode(), key])
    return clear_texts

def get_occurance(text):
    """Count all letters of a given text and return a dict with
    letter %"""
    occurance_text = {
        'a': 0,    'b': 0,    'c': 0,    'd': 0,
        'e': 0,    'f': 0,    'g': 0,    'h': 0,
        'i': 0,    'j': 0,    'k': 0,    'l': 0,
        'm': 0,    'n': 0,    'o': 0,    'p': 0,
        'q': 0,    'r': 0,    's': 0,    't': 0,
        'u': 0,    'v': 0,    'w': 0,    'x': 0,
        'y': 0,    'z': 0
    }

    for letter in text:
        if str.lower(letter) in occurance_text:
            occurance_text[str.lower(letter)] += 1
        else:
            pass
    occ = {k: v / len(text) * 100 for k, v in occurance_text.items()}
    return occ

def compute_fitting_quotient(dist_expected, dist_messured):
    """Messure the letterfrequency of a text compared to english"""
    expected_values = list(dist_expected.values())
    messured_values = list(dist_messured.values())
    return sum([abs(a - b) for a, b in zip(expected_values, messured_values)]) / len(dist_messured)


# This needs to be turend into a function that works more generalized
l = decypher(message)

fitted = list()

for pair in l:
    occurence_messured = get_occurance(pair[0])
    q = compute_fitting_quotient(occurance_english, occurence_messured)
    fitted.append([q, [pair[0], pair[1]]])

fitted.sort()
for most_likely in fitted[:2]:
    print("======================================")
    print(str(most_likely[0]) + "\n" + most_likely[1][0] + "\n" + most_likely[1][1] )




## Implement pearson's chi squared test
