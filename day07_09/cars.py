from typing import Dict, List

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    text = ""
    last = (len(cars['Jeep']) - 1)
    for cnt, car in enumerate(cars['Jeep']):
        text += car
        if cnt != last:
            text += ", "
    return text


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    first_model_list = list()
    for manufacturer in cars:
        first_model = cars[manufacturer][0]
        first_model_list.append(first_model)
    
    return first_model_list


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    all_models = list()
    for model_list in cars.values():
        for model in model_list:
            model_lowercase = model.lower()
            if (model_lowercase.find(grep.lower()) != -1):
                all_models.append(model)

    return sorted(all_models)


def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    new_cars = dict()
    for manufacturer, models_list in cars.items():
        new_cars[manufacturer] =  sorted(models_list)

    return new_cars

if __name__ == "__main__":
    pass