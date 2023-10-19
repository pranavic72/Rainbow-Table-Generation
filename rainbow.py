import hashlib

with open('rainbow.txt', 'w') as result:
    for word in open('passwords.txt').read().split():
        encodeword = hashlib.md5(word.encode()).hexdigest()
        result.write(word + ':'+ encodeword +'\n')
