import random


hdr2 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}

hdr4 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr = 0

if random.randint(1, 4) == 1:
    hdr = hdr2
elif random.randint(1, 4) == 2:
    hdr = hdr3
else:
    hdr = hdr4
print(hdr)