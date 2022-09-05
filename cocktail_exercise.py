import requests
import logging
logging.basicConfig(level=logging.INFO)


def get_ingredient_by_name(ingredient_name):

    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?', params={'i': ingredient_name})
    return response.json()['ingredients'][0]


def get_cocktail_by_name(cocktail_name):

    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?', params={'s': cocktail_name})
    return response.json()['drinks'][0]


def test_ingredients_by_name(ingredient_name):
    # Given the ingredient name is provided
    # When the ingredient_name is passed as a parameter in ingredient_by_name_response
    # Then the ingredient_by_name_response is populated with these fields: idIngredient,
    # ingredient, description, ingredient_type, alcohol and strABV

    ingredient_by_name_response = get_ingredient_by_name(ingredient_name)
    logging.info(f'The ingredient_by_name_response is {ingredient_by_name_response}')

    idIngredient = ingredient_by_name_response['idIngredient']
    ingredient = ingredient_by_name_response['strIngredient']
    description = ingredient_by_name_response['strDescription']
    ingredient_type = ingredient_by_name_response['strType']
    alcohol = ingredient_by_name_response['strAlcohol']
    strABV = ingredient_by_name_response['strABV']
    logging.info(f'The idIngredient is {idIngredient}')
    assert idIngredient == '1'
    logging.info(f'The ingredient is {ingredient}')
    assert ingredient == 'Vodka'
    logging.info(f'The description is {description}')
    logging.info(f'The ingredient_type is {ingredient_type}')
    assert ingredient_type == 'Vodka'
    logging.info(f'The alcohol is {alcohol}')
    assert alcohol == 'Yes'
    logging.info(f'The strABV is {strABV}')
    assert strABV == '40'


test_ingredients_by_name('Vodka')


def test_ingredient_is_alcoholic_or_non_alcoholic(ingredient_name):
    # Given the ingredient name is provided
    # When the ingredient_name is passed as a parameter in ingredient_by_name_response
    # And if the ingredient has No alcohol and No ABV
    # Then the ingredient is non-alcoholic else the ingredient is alcoholic

    ingredient_by_name_response = get_ingredient_by_name(ingredient_name)

    ingredient = ingredient_by_name_response['strIngredient']
    alcohol = ingredient_by_name_response['strAlcohol']
    strABV = ingredient_by_name_response['strABV']

    if ingredient == ingredient_name and alcohol == 'No' and strABV == None:
        logging.info(f'The ingredient {ingredient_name} is non-alcoholic')
        assert alcohol == 'No'
    else:
        logging.info(f'The ingredient {ingredient_name} is alcoholic')
        assert alcohol == 'Yes'


test_ingredient_is_alcoholic_or_non_alcoholic('Salt')
test_ingredient_is_alcoholic_or_non_alcoholic('vodka')


def test_ingredients_exists_or_not(ingredient_name):
    # Given the ingredient name is provided
    # When the ingredient_name is passed as a parameter in cocktail_by_name_response
    # And if the ingredient name is found
    # Than the ingredient exists else it doesn't exist

    ingredient_by_name_response = get_ingredient_by_name(ingredient_name)

    ingredient = ingredient_by_name_response['strIngredient']

    if ingredient == ingredient_name:
        logging.info(f'Than the ingredient {ingredient_name} exists')
        assert ingredient == ingredient_name
    else:
        logging.info(f'Than the ingredient {ingredient_name} does not exist')
        assert ingredient != ingredient_name


test_ingredients_exists_or_not('Salt')
test_ingredients_exists_or_not('butter')


def test_cocktails_by_name(cocktail_name):
    # Given the cocktail name is provided
    # When the cocktail_name is passed as a parameter in cocktail_by_name_response
    # Then cocktail_by_name_response is populated with these required fields strDrink, strTags
    # strCategory, strAlcoholic, strGlass, strInstructions, strIngredient1,
    # strMeasure1, strCreativeCommonsConfirmed, dateModified

    cocktail_by_name_response = get_cocktail_by_name(cocktail_name)
    logging.info(f'The cocktail_by_name_response is {cocktail_by_name_response}')

    strDrink = cocktail_by_name_response['strDrink']
    strTags = cocktail_by_name_response['strTags']
    strCategory = cocktail_by_name_response['strCategory']
    strAlcoholic = cocktail_by_name_response['strAlcoholic']
    strGlass = cocktail_by_name_response['strGlass']
    strInstructions = cocktail_by_name_response['strInstructions']
    strIngredient1 = cocktail_by_name_response['strIngredient1']
    strMeasure1 = cocktail_by_name_response['strMeasure1']
    strCreativeCommonsConfirmed = cocktail_by_name_response['strCreativeCommonsConfirmed']
    dateModified = cocktail_by_name_response['dateModified']
    logging.info(f'The strDrink is {strDrink}')
    assert strDrink == 'Margarita'
    logging.info(f'The strTags is {strTags}')
    assert strTags == 'IBA,ContemporaryClassic'
    logging.info(f'The strCategory is {strCategory}')
    assert strCategory == 'Ordinary Drink'
    logging.info(f'The strAlcoholic is {strAlcoholic}')
    assert strAlcoholic == 'Alcoholic'
    logging.info(f'The strGlass is {strGlass}')
    assert strGlass == 'Cocktail glass'
    logging.info(f'The strInstructions is {strInstructions}')
    assert strInstructions == 'Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.'
    logging.info(f'The strIngredient1 is {strIngredient1}')
    assert strIngredient1 == 'Tequila'
    logging.info(f'The strMeasure1 is {strMeasure1}')
    logging.info(f'The strCreativeCommonsConfirmed is {strCreativeCommonsConfirmed}')
    assert strCreativeCommonsConfirmed =='Yes'
    logging.info(f'The dateModified is {dateModified}')
    assert dateModified == '2015-08-18 14:42:59'


test_cocktails_by_name('Margarita')


def test_cocktail_exists_or_not(cocktail_name):
    # Given the cocktail name is provided
    # When the cocktail_name is passed as a parameter in cocktail_by_name_response
    # And if cocktail name is found
    # Than the cocktail exists else it doesn't exist

    cocktail_by_name_response = get_cocktail_by_name(cocktail_name)

    strDrink = cocktail_by_name_response['strDrink']
    logging.info(f'The strDrink is {strDrink}')

    if strDrink == cocktail_name:
        logging.info(f'The cocktail {cocktail_name} exists')
        assert strDrink == cocktail_name
    else:
        logging.info(f'The cocktail {cocktail_name} does not exist')
        assert strDrink != cocktail_name


test_cocktail_exists_or_not('Butter')
test_cocktail_exists_or_not('Strawberry Margarita')


def test_cocktail_is_alcoholic_or_non_alcoholic(cocktail_name):
    # Given the cocktail name is provided
    # When the cocktail_name is passed as a parameter in cocktail_by_name_response
    # And if the strAlcoholic is Alcoholic
    # Then the cocktail is Alcoholic else its Non-Alcoholic

    cocktail_by_name_response = get_cocktail_by_name(cocktail_name)

    strAlcoholic = cocktail_by_name_response['strAlcoholic']
    strDrink = cocktail_by_name_response['strDrink']

    if strDrink == cocktail_name and strAlcoholic == 'Alcoholic':
        logging.info(f'The cocktail_name {cocktail_name} is Alcoholic')
        assert strAlcoholic == 'Alcoholic'
    else:
        logging.info(f'The cocktail_name {cocktail_name} is non-alcoholic')
        assert strAlcoholic == 'Non alcoholic'


test_cocktail_is_alcoholic_or_non_alcoholic('Banana Strawberry')
test_cocktail_is_alcoholic_or_non_alcoholic('Whiskey Sour')



