from entry import Entry

class Catalogue:

    def __init__(self):
        self._index_dict = dict()
        self._num_entries = 0

    def get_entry(self, term):
        letter_list = self._get_letter_list(term)

        for entry in letter_list:
            if term == entry.get_term():
                return entry
        
        return None

    def insert_entry(self, entry):
        self._num_entries += 1
        first_letter = entry.get_term()[0].upper()

        if first_letter in self._index_dict:
            self._index_dict[first_letter].append(entry)
        else:
            self._index_dict[first_letter] = [entry]

    def delete_entry(self, term):
        letter_list = self._get_letter_list(term)

        for entry in letter_list:
            if term == entry.get_term():
                letter_list.remove(entry)
                self._num_entries -= 1
                break
        
        # Reset index dictionary
        if self._num_entries == 0:
            self._index_dict = dict()

        # Otherwise remove letter list from dictionary
        elif len(letter_list) == 0:
            del self._index_dict[term[0].upper()]

    def _get_letter_list(self, term):
        first_letter = term[0].upper()
        return self._index_dict[first_letter]

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


