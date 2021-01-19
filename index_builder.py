from entry import Entry
from catalogue import Catalogue

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
        elif inp == '/help':
            pass
        elif inp == '/delete':
            pass
        elif inp == '/check':
            print(catalogue)
        elif inp == '/save':
            break
        else:
            term = find_term(inp)
            pages = find_pages(inp)

            if term in catalogue:
                # Add new pages to existing entry
                entry_match = catalogue.get_entry(term)
                entry_match.add_pages(pages)
                print('Adjusted pages for \'{}\'.\n'.format(term))

            else:
                # Insert new entry into catalogue
                new_entry = Entry(term, pages)
                catalogue.insert_entry(new_entry)
                print('Added \'{}\' under {}.\n'.format(term, term[0].upper()))

def find_term(entered):
    comma_index = entered.find(',')
    if comma_index == -1:
        return entered
    
    return entered[:comma_index]

def find_pages(entered):
    comma_index = entered.find(',')
    if comma_index == -1:
        return []
    
    return entered[comma_index+1:].replace(' ', '').split(',')

if __name__ == '__main__':
    main()
