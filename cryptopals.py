# Library of all working crypto functions

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
    if len(chrstr1) == len(chrstr2):
        bar1 = bytes.fromhex(chrstr1)
        bar2 = bytes.fromhex(chrstr2)
        return bytes(a ^ b for a, b in zip(bar1, bar2)).hex()
    else
        print("Message and key must be of same length")

def hex_to_base64(crstr):
    """Takes a hex charachter string and
    returns a base64 encoded bytes-object"""
    return base64.b64encode(bytes.fromhex(crstr))

def get_lcount(text):
    """count all letters in text"""
    letter_count = {
    'a': 0,    'b': 0,    'c': 0,    'd': 0,
    'e': 0,    'f': 0,    'g': 0,    'h': 0,
    'i': 0,    'j': 0,    'k': 0,    'l': 0,
    'm': 0,    'n': 0,    'o': 0,    'p': 0,
    'q': 0,    'r': 0,    's': 0,    't': 0,
    'u': 0,    'v': 0,    'w': 0,    'x': 0,
    'y': 0,    'z': 0,    ' ': 0
    }

    for letter in text:
        if str.lower(letter) in letter_count:
            letter_count[str.lower(letter)] += 1
        else:
            pass
    return letter_count

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

def get_ioc(l_count):
    """Calculate index of coincidence"""
    return sum( n * (n - 1) for n in l_count.values()) / (sum(l_count.values()) * (sum(l_count.values()) - 1) / len(occurance_english))

def match(lst):
    """Returns the value that matches best to an expected value, used for ioc"""
    # ioc_english = 1.73
    # ioc_german = 2.05
    # ioc_french = 2.02
    expected_value = 1.73
    return min(lst, key = lambda x : abs(x - expected_value))

def compute_fitting_quotient(dist_expected, dist_messured):
    """Messure the letterfrequency of a text compared to english"""
    expected_values = list(dist_expected.values())
    messured_values = list(dist_messured.values())
    return sum([abs(a - b) for a, b in zip(expected_values, messured_values)]) / len(dist_messured)
