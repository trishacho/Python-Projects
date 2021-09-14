"""A collection of functions for working with cities."""

def city_state(city, state, population=0):
    """Return a string representing a city-state pair."""

    output_string = city.title() + ", " + state.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string
