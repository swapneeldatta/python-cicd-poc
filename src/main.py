import time, threading


def foo():
    print(time.ctime())
    threading.Timer(0.5, foo).start()

print("Version 1.0.0 Beta")
print("This is a program designed to test CI-CD on python.")
foo()
