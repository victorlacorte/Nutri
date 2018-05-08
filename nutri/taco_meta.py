from collections import namedtuple


# The TACO itself is in portuguese; does it make sense to utilize an english
# header?
TacoHeader = namedtuple('TacoHeader',
                        ['num',
                         'description',
                         'moisture',
                         'energy_kcal',
                         'energy_j',
                         'protein',
                         'fat',
                         'cholesterol',
                         'carbohydrate',
                         'fiber',
                         'ash_content',
                         'calcium',
                         'magnesium',
                         'manganese',
                         'phosphorus',
                         'iron',
                         'sodium',
                         'potassium',
                         'copper',
                         'zinc',
                         'retinol',
                         're',  # no clue what are these
                         'rae',
                         'thiamin',
                         'riboflavin',
                         'pyridoxine',
                         'niacin',
                         'vitamin_c'])
