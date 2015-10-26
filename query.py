"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)
# another way
Brand.query.filter_by(id=8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name="Corvette").filter_by(brand_name="Chevrolet").all()


# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()


# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()


# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("Cor%")).all()


# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()
# another way
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()


# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued.isnot(None))).all()
# Getting this error UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 22: ordinal not in range(
#128)


# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet")
# Getting error: UnicodeEncodeError: ascii' codec can't encode character u'\xeb' in position 22: ordinal not in range(
#128)


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    info = (db.session.query(Model.brand_name,
                             Model.name,
                             Brand.headquarters)
            .join(Brand)
            .filter(Model.year == year).all())
    print "it works"

    for result in info:
        brand, model, headQ = result
        result = "{brand} {model} {headQ}"
        print "{brand}, {model}, {headQ}".format(brand, model, headQ)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    info = (db.session.query(Model.brand_name, Model.name)
            .group_by(Model.name)
            .order_by(Model.brand_name)
            .all())

    for result in info:
        brand, model = result
        print "{brand} {model}".format(brand, model)

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """takes given string and returns (list of brand) all brands whose name contains the given string"""
    info = (db.session.query(Brand)
            .filter(Brand.brand_name.like("%" + mystr + "%")).all())

    return info


def get_models_between(start_year, end_year):
    info = (db.session.query(Model)
            .filter(Model.year >= start_year,
                    Model.year <= end_year)
            .all())
    return info


# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#answer: this is just a query. It doesn't give any result. it shows flask_sqlalchemy.BaseQuery object. If I add .one() to the end then I get Brand object

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

#answer: association table is in a many to many relationship by referencing the primary keys of each data table. It contains number of foreign keys showing many to one relationship from the associaion table to individual data table.
