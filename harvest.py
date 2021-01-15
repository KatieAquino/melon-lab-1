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
        key = melon.code

        melon_dictionary[key] = melon
    
    return melon_dictionary

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


if __name__ == '__main__':
    test_melon = MelonType('muskmelon', 'musk', '1998', 
                            'green', 'seedless', 'bestseller')
