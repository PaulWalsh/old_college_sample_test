import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv

    print("Hello, world")
    
    print('\nGood morning!')
    print('Vietnam!')
    print('Good morning,','Vietnam!')
    print('Good morning,', 'Vietnam!')
    print("Good morning,", "Vietnam!")

    return 0