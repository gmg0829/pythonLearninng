from io import StringIO,BytesIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
ff=StringIO('hello \ngmg\nyr')
while True:
    s=ff.readline()
    if s=='':
        break
    print(s.strip())

