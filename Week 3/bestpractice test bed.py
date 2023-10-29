print("Testing")
def main():
    dog()

def dog():
    print("This is a dog.")
    print('this functions is defined before main so this needs to be printed last')

if __name__ == '__main__':
    
    print('When does this get called')
    main()   