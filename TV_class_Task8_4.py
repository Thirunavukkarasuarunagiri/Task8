class TVClass:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on_off_status = False

    def increase_volume(self):
        self.volume = min(self.volume + 1, 100)

    def decrease_volume(self):
        self.volume = max(self.volume - 1, 0)

    def set_channel(self, new_channel):
        if 1 <= new_channel <= 50:
            self.channel = new_channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50
        self.on_off_status = False

    def get_status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"
