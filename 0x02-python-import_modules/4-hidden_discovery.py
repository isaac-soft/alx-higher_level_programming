#!/usr/bin/python3
if __name__ == "__main__":
    hidden = __import__('hidden_4')
    for name in dir(hidden):
        if name[:2] != "__":
            print (name)
