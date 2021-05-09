class HdmiCable:
    @staticmethod
    def connect_via_hdmi(device):
        return f"{device} is connected via hdmi"


class RcaCable:
    @staticmethod
    def connect_via_rca(device):
        return f"{device} is connected via rca"


class EthernetCable:
    @staticmethod
    def connect_via_ethernet(device):
        return f"{device} is connected via ethernet"


class PowerOutlet:
    @staticmethod
    def connect_to_power_outlet(device):
        return f"{device} is connected in power outlet"


class EntertainmentDevice:
    pass


class Television(EntertainmentDevice, RcaCable, HdmiCable, PowerOutlet):
    def connect_to_dvd(self, dvd_player):
        self.connect_via_rca(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_via_hdmi(game_console)

    def plug_in_power(self):
        self.connect_to_power_outlet(self.__class__.__name__)


class DvdPlayer(EntertainmentDevice, HdmiCable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def plug_in_power(self):
        self.connect_to_power_outlet(self.__class__.__name__)


class GameConsole(EntertainmentDevice, HdmiCable, EthernetCable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def connect_to_router(self, router):
        self.connect_via_ethernet(router)

    def plug_in_power(self):
        self.connect_to_power_outlet(self.__class__.__name__)


class Router(EntertainmentDevice, EthernetCable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_via_ethernet(television)

    def connect_to_game_console(self, game_console):
        self.connect_via_ethernet(game_console)

    def plug_in_power(self):
        self.connect_to_power_outlet(self.__class__.__name__)
