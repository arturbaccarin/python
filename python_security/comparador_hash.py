import hashlib

ARQUIVO1 = 'comp_hash_1.txt'
ARQUIVO2 = 'comp_hash_2.txt'

hash1 = hashlib.new('ripemd160') # tipo do algoritmo de hash

hash1.update(open(ARQUIVO1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(ARQUIVO2, 'rb').read())

print(hash2.hexdigest())

# 
if hash1.digest() != hash2.digest():
    print(f'Os arquivos são diferentes.')
else:
    print('Os arquivos são iguais')