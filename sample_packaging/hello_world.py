def hello():
    print 'Hello World !!!'


def hello_wo_importing():
    print 'Hello World without importing!!!'

'''
kiyyer-mbp:~ kiyyer$ python
Python 2.7.14 (default, Sep 25 2017, 09:53:17) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from sample_packaging import hello_world
>>> hello_world.hello()
Hello World !!!
>>> hello_world.hello_wo_importing()
Hello World without importing!!!
>>> exit()
kiyyer-mbp:~ kiyyer$ python
Python 2.7.14 (default, Sep 25 2017, 09:53:17) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sample_packaging
>>> sample_packaging.hello_world.hello()
Hello World !!!
>>> sample_packaging.hello_world.hello_wo_importing()
Hello World without importing!!!
>>> sample_packaging.hello()
Hello World !!!
>>> sample_packaging.hello_wo_importing()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'hello_wo_importing'
'''