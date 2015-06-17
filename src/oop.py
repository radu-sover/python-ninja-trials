import traceback
import sys

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

    __len__ = size

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
        a = Configuration(fobj)

        # other option to read config
        # config has inside section named: ip.addresses and property home.pc1
        value = a.section__property(with_default)
        value = a.ip_addresses__home_pc1()

    """

    def __init__(self, config_and_section):
        self.configurations = {}
        try:
            for sec in iter(config_and_section):
                self.configurations[sec] = {}
                for prop in iter(config_and_section[sec]):
                    self.configurations[sec][prop] = config_and_section[sec][prop]
        except TypeError:
            raise

    def __getitem__(self, item):
        return self.configurations[item]

    def __getattr__(self, item):
        found = None
        section_property = [str.replace(x, '_', '.') for x in item.split('__')]

        if len(section_property) == 2:
            sec = section_property[0]
            prop = section_property[1]
            found = self.configurations.get(sec, {}).get(prop)

        elif len(section_property) == 1:
            sec = section_property[0]
            found = self.configurations.get(sec)

        if not found:
            raise AttributeError

        return found


def ConfigurationFromFile(fobj):
    """
    Poor man implementation
    :param file_path:
    :return: None
    """
    configuration = {}

    section_start = '['
    property_not_start = [';', '', '\n']

    section_name = '__none__'
    for line in fobj:
        line = line.strip('\n')
        if len(line) == 0:
            continue

        if section_start == line[0]:
            section_name = line[1:-1]
            configuration[section_name] = {}
        elif line[0] not in property_not_start:
            property_name, property_value = line.split('=')
            configuration[section_name][property_name] = property_value

    return Configuration(configuration)


# Design a logging library API and implement it.
class LoggerSink:
    def __init__(self):
        pass

    def write(self, message):
        print(message)


class FileLoggerSink(LoggerSink):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, message):
        with open(self.file_path, mode='a') as f:
            f.write('%s\n' % message)


class Logger:
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

    ERROR = 1
    INFO = 2
    DEBUG = 3

    def __init__(self, component, level=ERROR, sink=LoggerSink):
        self.component = component
        self.level = Logger.ERROR
        self.sink = sink

    @classmethod
    def logger_with_sink(cls, component, sink) -> 'Logger':
        """
        Create a new logger with custom sink
        :param component:
        :param sink:
        :return: Logger
        """
        log = cls(component)
        log.set_sink(sink)
        return log

    def set_sink(self, sink_instance):
        self.sink = sink_instance

    def set_level(self, level):
        """
        :param level: one of the Logger.ERROR, INFO, DEBUG
        :return: None
        """
        self.level = level

    def log_error(self, message=None):
        if self.level >= Logger.ERROR:
            exception_formatted = None
            if sys.exc_info()[0] is not None:
                exception_formatted = traceback.format_exc()

            self.sink.write(
                "ERROR in {component} | Exception: {exception}; message: {message}".format(
                    exception=exception_formatted, message=message, component=self.component))

    def log_info(self, message):
        if self.level >= Logger.INFO:
            self.sink.write(
                "INFO in {component} | message: {message}".format(
                    message=message, component=self.component))

    def log_debug(self, verbose):
        if self.level >= Logger.DEBUG:
            self.sink.write(
                "DEBUG in {component} | verbose: {verbose}".format(
                    verbose=verbose, component=self.component))

    pass


if __name__ == '__main__':
    # q = Queue()
    # print(len(q))

    with open('config.ini', 'r') as f:
        config = ConfigurationFromFile(f)

    print('1 - ', config.owner__name)
    print('1 - ', config['owner']['name'])

    print('2 - ', config.database)
    print('2 - ', config['database'])

    print('3 - ', config.database__file)
    print('3 - ', config['database']['file'])

    print('4 - ', config.ip_addresses)
    print('5 - ', getattr(config, 'ip_addresses__home_pc', '192.168.0.1'))
    print('6 - ', getattr(config, 'cucu_bambucu', 'bau bau'))

    log2 = Logger.logger_with_sink(__name__, FileLoggerSink('e:\logger.txt'))
    log = Logger(__name__)
    log.set_level(Logger.DEBUG)

    log2.log_info('started the program')
    log2.log_debug('inca o logare....')
    log2.log_error('inca o eroare for stack de eroare....')

    try:
        d = 34 / 0
    except ZeroDivisionError:
        log2.log_error()
