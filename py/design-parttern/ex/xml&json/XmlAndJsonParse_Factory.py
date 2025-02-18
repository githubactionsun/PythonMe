import xml.etree.ElementTree as etree
import json


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connetor_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))

    return connector(filepath)


def connect_to(filepath):
    factory = None

    try:
        factory = connetor_factory(filepath)
    except ValueError as ve:
        print(ve)

    return factory


def main():
    sqllite_factory = connect_to('data/person.sq3')


# /* excute */
main()
