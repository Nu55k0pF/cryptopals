import base64

# Sample string
m = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex_to_base64(crstr):
    """Takes a hex charachter string and
    returns a base64 encoded bytes-object"""
    return base64.b64encode(bytes.fromhex(crstr))

print((hex_to_base64(m).decode()))
