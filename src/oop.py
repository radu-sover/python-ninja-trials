import functools


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, item):
        """
        Add an item to queue
        :param item:
        """
        self.items.insert(0, item)

    def pop(self):
        """
        Retrieve the item from the queue -> item
        :return: The oldest item
        """
        return self.items.pop()

    def size(self):
        return len(self.items)

class PriorityQueue(Queue):

    def add(self, item, priority=False):
        if priority:
            self.items.append(item)
        else:
            super().add(item)


# Design a configuration reader library API and implement it.
# The reader should read a configuration file from disk and expose its values through the API you choose.
class Configuration:
    """
    A class to handle simple ini file configurations.
    Usage:
        a = Configuration()
        a.read('file path to read')
        a.read_string('...')

        section = a['section']
        properties = a.properties['section']
        value = a.['section']['property']

        # other option to read config
        # config has inside section named: ip.addresses and property home.pc1
        value = a.section__property(with_default)
        value = a.ip_addresses__home_pc1()


    """

    def __init__(self):
        self.configurations = {}

    def read(self, file_path):
        """
        Poor man implementation
        :param file_path:
        :return: None
        """
        section_start = '['
        property_not_start = [';', '', '\n']

        with open(file_path, 'r') as f:
            section_name = '__none__'
            for line in f:
                line = line.strip('\n')
                if len(line) == 0:
                    continue

                if section_start == line[0]:
                    section_name = line[1:-1]
                    self.configurations[section_name] = {}
                elif line[0] not in property_not_start:
                    property_name, property_value = line.split('=')
                    self.configurations[section_name][property_name] = property_value

    def sections(self):
        # return the sections from the config
        return self.configurations.keys()

    def properties(self, section_key):
        return self.configurations[section_key]

    def __getitem__(self, item):
        return self.configurations[item]

    def found_property_or_default(found_value, default_value=None):
        if found_value is None:
            return default_value
        return found_value

    def __getattr__(self, item):
        found = None
        section_property = [str.replace(x, '_', '.') for x in item.split('__')]
        if len(section_property) == 2:
            if (section_property[0] in self.configurations.keys()) and (section_property[1] in self.configurations[section_property[0]].keys()):
                found = self.configurations[section_property[0]][section_property[1]]
        elif len(section_property) == 1:
            if section_property[0] in self.configurations.keys():
                found = self.configurations[section_property[0]]

        return functools.partial(Configuration.found_property_or_default, found)


# Design a logging library API and implement it.
class SemanticLogger:
    """
    Usage:
    l = Logger('component')
    l = Logger(frame?)

    to define
    sink
    Event
    decorators
    ... sau plain old logging..
    """

    def __init__(self):
        pass

    pass

class EventSource:

    pass

if __name__ == '__main__':
    config = Configuration()
    config.read('config.ini')

    # print('1 - ', config.owner__name())
    # print('1 - ', config['owner']['name'])
    #
    # print('2 - ', config.database())
    # print('2 - ', config['database'])
    #
    print('3 - ', config.database__file())
    print('3 - ', config['database']['file'])

    print('4 - ', config.ip_addresses())
    print('5 - ', config.ip_addresses__home_pc('192.168.0.1'))
    print('6 - ', config.cucu_bambucu('bau bau'))
