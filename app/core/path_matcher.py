from app.utils.path_components import PathComponents, PathComponentType, PathComponent
from app.utils.utils import last


class PathMatcherResult(object):
    def __init__(self,
                 pattern: PathComponents,
                 path: str,
                 parameters: dict,
                 any_parameters: [str],
                 match: bool):
        self.pattern = pattern
        self.path = path
        self.parameters = parameters
        self.any_parameters = any_parameters
        self.match = match


class PathMatcherMatchItemResult(object):
    def __init__(self,
                 components: [str],
                 match: bool,
                 parameter: str = None,
                 any_parameters: [str] = None):
        self.components = components
        self.match = match
        self.parameter = parameter
        self.any_parameters = any_parameters


class PathMatcher(object):
    def __init__(self,
                 pattern: PathComponents,
                 path: str):
        self.pattern = pattern
        self.path = path
        self.components = path.split('/')
        self.parameters = {}
        self.any_parameters = []

    def match(self) -> PathMatcherResult:
        match = self.__validate() and self.__match()
        return PathMatcherResult(pattern=self.pattern,
                                 path=self.path,
                                 parameters=self.parameters,
                                 any_parameters=self.any_parameters,
                                 match=match)

    def __match(self):
        components = self.components
        for item in self.pattern.path_components:
            result = self.__match_item(item, components)
            if result.match:
                components = result.components
                if result.parameter:
                    self.parameters[item.parameter] = result.parameter
                if result.any_parameters:
                    self.any_parameters += result.any_parameters
            else:
                return False
        return True

    def __match_item(self, pattern: PathComponent, components: [str]) -> PathMatcherMatchItemResult:
        if pattern.type == PathComponentType.match:
            if components:
                component = components.pop(0)
                result = pattern.component == component
                return PathMatcherMatchItemResult(components, result)
        elif pattern.type == PathComponentType.match_any:
            if components:
                component = components.pop(0)
                return PathMatcherMatchItemResult(components, True, None, [component])
        elif pattern.type == PathComponentType.match_any_deep:
            return PathMatcherMatchItemResult([], True, None, components)
        elif pattern.type == PathComponentType.match_parameter:
            if components:
                component = components.pop(0)
                return PathMatcherMatchItemResult(components, True, component)
            pass
        return PathMatcherMatchItemResult(components, False)

    # validate
    def __validate(self) -> bool:
        # validation will path when
        # and mock pattern has at least the same elements count
        # and mock pattern has match_any_deep as last component (if pattent contains /**)
        return self.__validate_length() and self.__validate_match_any_deep()

    def __validate_length(self) -> bool:
        path_components = self.pattern.path_components
        items = list(filter(lambda item: item.type == PathComponentType.match_any_deep, path_components))
        if len(items) == 0:
            return len(path_components) == len(self.components)
        elif len(items) == 1:
            return len(path_components) <= len(self.components)
        else:
            return False

    def __validate_match_any_deep(self) -> bool:
        path_components = self.pattern.path_components
        items = list(filter(lambda item: item.type == PathComponentType.match_any_deep, path_components))
        if len(items) == 0:
            return True
        elif len(items) == 1:
            return last(path_components).type == PathComponentType.match_any_deep
        else:
            return False
