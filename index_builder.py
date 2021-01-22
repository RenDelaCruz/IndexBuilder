from entry import Entry
from catalogue import Catalogue
from actions import *

def main():
    print('_' * 15)
    print('\n Index Builder\n ver. 1.1')
    print('_' * 15)

    print('\nInstructions')

    catalogue = Catalogue()
    inp = ''

    while True:
        inp = input('> ')

        if len(inp) == 0:
            pass
        elif inp.startswith('/'):
            if inp == '/help':
                pass
            elif inp.startswith('/delete'):
                inp = inp.split("/delete ", 1)[1]
                catalogue = delete_entry(inp, catalogue)

            elif inp == '/check':
                print(catalogue)
                
            elif inp.startswith('/save'):
                if inp == '/save':
                    print('Invalid. Expected syntax: /save <filename>\n')
                else:
                    inp = inp.split("/save ", 1)[1]
                    save_index(inp, catalogue)
        else:
            catalogue = insert_entry(inp, catalogue)

if __name__ == '__main__':
    main()
