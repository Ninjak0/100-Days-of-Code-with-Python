cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ",".join(cars["Jeep"])



def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    models = []
    for key, value in cars.items():
        models.append(value[0])
    return models


def get_all_matching_models(grep='CO'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matches = []
    for model in cars.values():
        for value in model:
            if grep.lower() in value.lower():
                matches.append(value)
    matches.sort()
    return matches


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for key, value in cars.items():
        value.sort()
    return cars

#print(get_all_jeeps())
#print(get_first_model_each_manufacturer())
print(get_all_matching_models())
#print(sort_car_models())