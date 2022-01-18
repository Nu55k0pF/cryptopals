# Library of all working crypto functions

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
