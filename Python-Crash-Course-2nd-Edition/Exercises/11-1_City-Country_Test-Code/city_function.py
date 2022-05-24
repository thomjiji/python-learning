def city_name(city_name, country_name, population=''):
    """Take city name and country name, return a full name."""
    if population:
        return f"{city_name}, {country_name} - population: {population}"
    else:
        return f"{city_name}, {country_name}"