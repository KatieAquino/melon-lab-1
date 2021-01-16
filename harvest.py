############
# Part 1   #
############

import sys

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

    def __init__(self, type, shape_rating, color_rating, 
                field, harvested_by,):

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

def make_melons(melon_types, file):
    """Returns a list of Melon objects."""

    all_melons = []
    file_text = open(file)

    for line in file_text:
        line_info = [line.strip() for line in file_text]

        for item in line_info:
            melon_info = item.split(" ")

            shape_rating = melon_info[1]
            shape_rating = int(shape_rating)

            color_rating = melon_info[3]
            color_rating = int(color_rating)

            type = melon_info[5]
            harvested_by = melon_info[8]
            field = melon_info[-1]

            melon = Melon(melon_types[type], shape_rating, color_rating, 
                        field, harvested_by)
            
            melon.is_sellable()

            all_melons.append(melon)


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
    file = 'harvest_log.txt'
    melon_types = make_melon_types()
    melon_dictionary = make_melon_type_lookup(melon_types)
    melons_report = make_melons(melon_dictionary, file)
    sellability_report = get_sellability_report(melons_report)
