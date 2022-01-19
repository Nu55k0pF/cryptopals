# https://gist.github.com/mikeecb/0d75f46521fe526a0138ae5265392505
message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
bmessage = bytearray.fromhex(message)

def generate_keys(msg):
    keys = []
    for i in range(256):
        keys.append(bytearray(([i]) * len(msg)))
    return keys

def xor(bar1, bar2):
    return bytes(a ^ b for a, b in zip(bar1, bar2))

def single_byte_xor(msg):
    b_msg = bytearray.fromhex(msg)
    plain_texts = []
    keys = generate_keys(msg)
    for key in keys:
        plain_texts.append(xor(b_msg, key).decode(encoding='ASCII', errors='ignore'))
    return plain_texts

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

def get_ioc(l_count):
    """Calculate index of coincidence"""
    try:
        return sum( n * (n - 1) for n in l_count.values()) / (sum(l_count.values()) * (sum(l_count.values()) - 1) / len(l_count))
    except ZeroDivisionError:
        return 0

def match(lst):
    """Returns the value that matches best to an expected value, used for ioc"""
    # ioc_english = 1.73
    # ioc_german = 2.05
    # ioc_french = 2.02
    expected_value = 1.73
    return min(lst, key = lambda x : abs(x - expected_value))

def break_single_byte_xor(message):

    plain_texts = single_byte_xor(message)
    scores = []
    keys = generate_keys(message)

    for text in plain_texts:
        scores.append(get_ioc(get_lcount(text)))

    i = scores.index(match(scores))
    print(match(scores))
    print(plain_texts[i])
    print(keys[i])

break_single_byte_xor(message)
