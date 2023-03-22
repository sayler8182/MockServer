from enum import Enum


class MockRequestRuleType(Enum):
    match_header = 'match_header'
    match_parameter = 'match_parameter'

    @property
    def description(self) -> str:
        return {
            MockRequestRuleType.match_header: 'Match header',
            MockRequestRuleType.match_parameter: 'Match parameter'
        }.get(self)

    @staticmethod
    def supported_rules():
        return [
            MockRequestRuleType.match_header,
            MockRequestRuleType.match_parameter
        ]

    def get_dict(self):
        return self.value
