import random
from guess import tebakangka

tebak = tebakangka()
jawaban = random.randint(1,10)
tebakan = int(input("tebak angka dari 1 s.d 10:"))  

if tebak.cek():
    print("jawaban kamu benar!")
else:
    print("jawaban kamu salah!")