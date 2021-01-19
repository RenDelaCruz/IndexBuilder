
class Entry:
    
    def __init__(self, term, pages):
        self._term = term
        self._pages = pages

    def get_term(self):
        return self._term

    def get_pages(self):
        return self._pages

    def add_pages(self, new_pages):
        self._pages.extend(new_pages)

    def _remove_page_duplicates(self, page_list):
        pass

    def __eq__(self, other):
        return self.get_term() == other.get_term()

    def __lt__(self, other):
        entry1 = self.get_term()[0].upper()
        entry2 = other.get_term()[0].upper()
        return ord(entry1) < ord(entry2)

    def __str__(self):
        return self._term

    def __repr__(self):
        return self._term + ' - ' + str(self._pages)