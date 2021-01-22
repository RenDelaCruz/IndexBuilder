from entry import Entry
from catalogue import Catalogue

def insert_entry(inp, catalogue):
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

    return catalogue

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

def delete_entry(term, catalogue):
    if term in catalogue:
        catalogue.delete_entry(term)
        print('Successfully deleted \'{}\'.\n'.format(term))

    else:
        print('Unknown entry.\n')

    return catalogue

def save_index(inp, catalogue):
    if len(inp) == 0:
        inp = 'Index'

    filename = inp + '.txt'
    with open(filename, 'w') as f:
        print(catalogue.print_textfile_format(), file=f)

    print('Saved index as {}.\n'.format(filename))
