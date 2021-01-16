############
# Part 1   #
############

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, 
                is_seedless, is_bestseller):
        """Initialize a melon."""
        
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairing = pairing
        self.pairings.append(self.pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("muskmelon", "musk", "1998", 
                        "green", True, True)
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType("casaba", "cas", "2003", "orange", False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType("crenshaw", "cren", "1996", "green", False, False)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yellow watermelon", "yw", "2013",
                                "yellow", False, True)
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in all_melon_types:
        if melon.pairings == []:
            print(None)
        
        else:
            print(f'{melon.name.title()} pairs with:')
            for item in melon.pairings:
                print(item)
        
        print('')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}

    for melon in melon_types:
        if melon.code not in melon_dictionary:
            melon_dictionary[melon.code] = melon
    
    return melon_dictionary

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, number, type, shape_rating, color_rating, 
                field, harvested_by,):

                self.number = number
                self.type = type
                self.shape_rating = shape_rating
                self.color_rating = color_rating
                self.field = field
                self.harvested_by = harvested_by

    def is_sellable(self):

        sellable = False

        if self.shape_rating > 5 and self.color_rating > 5:
            sellable = True

        self.sellable = sellable

        return self.sellable

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melons = []

    melon_1 = Melon(1, melon_types['yw'], 8, 7, 2, 'Sheila')
    melon_1.is_sellable()

    melon_2 = Melon(2, melon_types['yw'], 3, 4, 2, 'Sheila')
    melon_2.is_sellable()

    melon_3 = Melon(3, melon_types['yw'], 9, 8, 3, 'Sheila')
    melon_3.is_sellable()

    melon_4 = Melon(4, melon_types['cas'], 10, 6, 35, 'Sheila')
    melon_4.is_sellable()

    melon_5 = Melon(5, melon_types['cren'], 8, 9, 35, 'Michael')
    melon_5.is_sellable()

    melon_6 = Melon(6, melon_types['cren'], 8, 2, 35, 'Michael')
    melon_6.is_sellable()

    melon_7 = Melon(7, melon_types['cren'], 2, 3, 4, 'Michael')
    melon_7.is_sellable()

    melon_8 = Melon(8, melon_types['musk'], 6, 7, 4, 'Michael')
    melon_8.is_sellable()

    melon_9 = Melon(9, melon_types['yw'], 7, 10, 3, 'Sheila')
    melon_9.is_sellable()

    all_melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6,
                    melon_7, melon_8, melon_9])

    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.sellable == True:
            status = '(CAN BE SOLD)'
    
        else:
            status = '(NOT SELLABLE)'

        print(f'Harvested by {melon.harvested_by} from Field {melon.field} {status}')


if __name__ == '__main__':
    test_melon = MelonType('muskmelon', 'musk', '1998', 
                            'green', 'seedless', 'bestseller')
