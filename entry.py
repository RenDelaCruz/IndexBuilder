
class Entry:
    
    def __init__(self, term, pages):
        self._term = term
        self._pages = self._sort_pages(pages)

    def get_term(self):
        return self._term

    def get_pages(self):
        return self._pages

    def add_pages(self, new_pages):
        curr_pages = self._pages
        self._pages = self._sort_pages(curr_pages + new_pages)

    def _sort_pages(self, page_list):
        # Remove duplicates
        page_list = self._remove_duplicates(page_list)

        # Sort list with roman numerals at head, integer pages at tail
        alpha_num_separated = sorted(page_list, key = lambda x: (x[0].isdigit(), x))
        first_integer_index = self._find_first_integer_page(alpha_num_separated)

        # Separate alphabetical (roman numeral) and numeric page lists
        alpha_list = alpha_num_separated[:first_integer_index]
        num_list = alpha_num_separated[first_integer_index:]

        # Removed overlapping pages
        num_list_reduced = self._remove_overlap_pages(num_list)
        return alpha_list + num_list_reduced

    def _remove_duplicates(self, page_list):
        return list(dict.fromkeys(page_list))

    def _find_first_integer_page(self, page_list):
        return next((i for i, x in enumerate(page_list) if x[0].isdigit()), None)

    def _remove_overlap_pages(self, num_list):
        # Sort numeric list based on integer or first integer in a range
        num_list = sorted(num_list, key = lambda x: int(x.split('-')[0]))
        # Gets list of indices for pages with a range
        ranged_indexes = [i for i, page in enumerate(num_list) if '-' in page]

        reduced_list = num_list.copy()
        for index in ranged_indexes:
            # Low and high end of the range
            low, high = [int(e) for e in num_list[index].split('-')]

            # Removes redundant pages already in a range
            reduced_list = [e for e in reduced_list if '-' in e or not (low <= int(e) <= high)]
        
        return reduced_list

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
