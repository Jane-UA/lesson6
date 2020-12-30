def make_country(country_name, capital):
    return {'country': country_name, 'capital': capital}


def print_values(any_dict):
    print(any_dict.values())


if __name__ == '__main__':
    d = make_country('Ukraine', 'Kiev')
    print_values(d)
