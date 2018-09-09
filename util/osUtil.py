import os
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
#print(os.name)
#linux提供uname()
#print(os.uname())
print(os.environ.get('path'))