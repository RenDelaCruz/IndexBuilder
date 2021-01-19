from entry import Entry

class Catalogue:

    def __init__(self):
        self._index_dict = dict()

    def get_entry(self, term):
        first_letter = term[0].upper()
        letter_list = self._index_dict[first_letter]

        for entry in letter_list:
            if term == entry.get_term():
                return entry
        
        return None

    def insert_entry(self, entry):
        first_letter = entry.get_term()[0].upper()

        if first_letter in self._index_dict:
            self._index_dict[first_letter].append(entry)
        else:
            self._index_dict[first_letter] = [entry]

    def __contains__(self, term):
        for entries in self._index_dict.values():
            for entry in entries:
                if term == entry.get_term():
                    return True

        return False

    def __str__(self):
        formatted = '\t' + ('_' * 30) + '\n\n\tIndex'

        for letter in sorted(self._index_dict):
            formatted += '\n\n\t{}'.format(letter)

            for entry in sorted(self._index_dict[letter]):
                formatted += '\n\t{}'.format(entry.get_term())
                for page in entry.get_pages():
                    formatted += ', {}'.format(page)
        
        formatted += '\n\t' + '_' * 30
        return formatted + '\n'


