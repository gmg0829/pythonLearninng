import hashlib
def md(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    b=md5.hexdigest()
    # sha1=hashlib.sha1()
    # sha1.update(str.encode('utf-8'))
    # sha.hexdigest()
    return b
print(md('13716098126'))