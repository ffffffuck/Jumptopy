buf = ['[ { "seq" : 0, "content" : "abcd"',
'[ { "seq" : 0, "content" : "abcd" }, { "seq" : 1, "content" : "d"',
'[ { "seq" : 0, "content" : "abcd" }, { "seq" : 1, "content" : "dsfswde" }, { "seq" : 2, "content"',
'[ { "seq" : 0, "content" : "abcd" }, { "seq" : 1, "content" : "dsfswde" }, { "seq" : 2, "content" : "dfdfdfd" }']


start = 0
bufsize = len(buf[0])
p = 0
for data in buf:
    for i in range(p, len(data)):
        if data[i] == '{':
            start = i
        elif data[i] == '}':
            print('[' + data[start:i+1] + ']')
            start = i + 1

    p += bufsize

