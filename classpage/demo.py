import random
alphabet = 'ABCDEFGHIJKLMNOPQISTUVWXYZ'
import time

characters = ''.join(random.sample(alphabet, 5))

print(characters)

print(int(time.time()))