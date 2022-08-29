import re


class PathComponentType(object):
    match = 'match'
    match_any = 'match_any'
    match_any_deep = 'match_any_deep'
    match_parameter = 'match_parameter'


class PathComponent(object):
    def __init__(self, component: str):
        self.component = component
        self.type = None
        self.parameter = None
        self.__parse()

    def __parse(self):
        if self.__parse_match_parameter():
            pass
        elif self.__parse_match_any_deep():
            pass
        elif self.__parse_match_any():
            pass
        elif self.__parse_match():
            pass

    def __parse_match_parameter(self):
        regex = re.compile('(^#{)(.*)(})')
        match = regex.match(self.component)
        if match:
            self.parameter = match.group(2)
            self.type = PathComponentType.match_parameter
            return True
        return False

    def __parse_match_any_deep(self):
        if self.component == '**':
            self.type = PathComponentType.match_any_deep
            return True
        return False

    def __parse_match_any(self):
        if self.component == '*':
            self.type = PathComponentType.match_any
            return True
        return False

    def __parse_match(self):
        self.type = PathComponentType.match
        return True

    def __repr__(self):
        return f'\ncomponent: {self.component}' \
               f' \ntype: {self.type}' \
               f' \nparameter: {self.parameter}'


class PathComponents(object):
    def __init__(self, path: str):
        self.path = path
        self.__create_components()

    def __create_components(self):
        components = self.path.split('/')
        self.path_components = list(map(lambda item: PathComponent(item), components))
        pass

    def __eq__(self, other):
        return self.path == other.path

    def __repr__(self):
        return f'{self.path_components}'
