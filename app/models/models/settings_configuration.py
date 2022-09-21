from app.models.models.delay import Delay
from app.models.models.delay_mode import DelayMode
from app.utils.utils import get_dict


class SettingsConfiguration(object):
    def __init__(self,
                 supported_delay_modes: [DelayMode],
                 supported_delays: [Delay]):
        self.supported_delay_modes = supported_delay_modes
        self.supported_delays = supported_delays

    def get_dict(self):
        return {
            'supported_delay_modes': get_dict(self.supported_delay_modes),
            'supported_delays': get_dict(self.supported_delays)
        }
