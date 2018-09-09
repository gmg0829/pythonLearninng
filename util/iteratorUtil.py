import sys
list=[3,'gmg',5]
it=iter(list)
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
