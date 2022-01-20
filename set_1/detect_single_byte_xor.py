from single_bytes_xor import break_single_byte_xor, get_ioc, get_lcount, match
import single_bytes_xor


cypher_texts = []

with open('C:/Users/User/Programieren/Python/cryptopals/set_1/text4.txt') as f:
   lines = f.readlines()

   for line in lines:
       cypher_texts.append(line)

def detect_sbxor(cypher_texts):
    score_temp = []
    plain_texts = []
    keys = []
    scores = []
    
    
    for text in cypher_texts:
        s, p, k = break_single_byte_xor(text)
        score_temp.append(s)
        plain_texts.append(p)
        keys.append(k)

#TODO: Test above for loop again and test bottom loop again, script runs
# but gives garbage answer

    for text in plain_texts:
        scores.append(get_ioc(get_lcount(text)))

    i = scores.index(match(scores))
    return match(scores), plain_texts[i], keys[i]

print(detect_sbxor(cypher_texts))