############
# Part 1   #
############


from operator import is_
from tkinter import N


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
# Reporting code: musk
# First harvest in 1998
# Color: green
# Pairs well with mint
# Seedless
# Bestseller
        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'crenshaw')
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'yellow watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon
    
    return melon_dict


############
# Part 2   #
############


class Melon(MelonType):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
# Melon type: yw
# Shape rating: 8
# Color rating: 7
# Harvested from Field 2
# Harvested by Sheila
    def __init__(
        self, code, shape_rating, color_rating, field, harvester
    ):
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

        super().__init__(
            code = code, 
            first_harvest = melon_dict[code].first_harvest, 
            color = melon_dict[code].color, 
            is_seedless = melon_dict[code].is_seedless, 
            is_bestseller = melon_dict[code].is_bestseller, 
            name = melon_dict[code].name
            )
    
    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else: return False


def make_melons():
    """Returns a list of Melon objects."""

    melons = []
    
    melon_1 = Melon('yw', 8, 7, 2, 'Sheila')
    melons.append(melon_1)

    melon_2 = Melon('yw', 3, 4, 2, 'Sheila')
    melons.append(melon_2)

    melon_3 = Melon('yw', 9, 8, 3, 'Sheila')
    melons.append(melon_3)

    melon_4 = Melon('cas', 10, 6, 35, 'Sheila')
    melons.append(melon_4)

    melon_5 = Melon('cren', 8, 9, 35, 'Michael')
    melons.append(melon_5)

    melon_6 = Melon('cren', 8, 2, 35, 'Michael')
    melons.append(melon_6)

    melon_7 = Melon('cren', 2, 3, 4, 'Michael')
    melons.append(melon_7)

    melon_8 = Melon('musk', 6, 7, 4, 'Michael')
    melons.append(melon_8)

    melon_9 = Melon('yw', 7, 10, 3, 'Sheila')
    melons.append(melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        msg = f"Harvested by {melon.harvester} from Field {melon.field} "
        if melon.is_sellable():
            msg = msg + '(CAN BE SOLD)'
        else: msg = msg + '(NOT SELLABLE)'
        print(msg)

def import_harvest_log(filename):
    melons = []

    for line in open(filename):
        line = line.rstrip()
        line = line.split()
        melon = Melon(
            line[5], int(line[1]), int(line[3]), int(line[11]), line[8]
            )
        melons.append(melon)

    return melons


melon_types = make_melon_types()

melon_dict = make_melon_type_lookup(melon_types)

# melons = make_melons()
melons = import_harvest_log('harvest_log.txt')

get_sellability_report(melons)