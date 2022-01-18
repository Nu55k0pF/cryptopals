m = "1c0111001f010100061a024b53535009181c"
k = "686974207468652062756c6c277320657965"

def fixed_xor(chrstr1, chrstr2):
    """Takes two charachter strings of the same length and xors them against each other"""
    if len(chrstr1) == len(chrstr2):
        bar1 = bytes.fromhex(chrstr1)
        bar2 = bytes.fromhex(chrstr2)
        return bytes(a ^ b for a, b in zip(bar1, bar2)).hex()
    else:
        print("Message and key must be of same length")

print(fixed_xor(m, k))
