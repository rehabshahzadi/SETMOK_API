class Mention:
    def __init__(self):
        self.text = None
        self.display_name = None
        self.display_picture = None
        self.time = None
        self.reshare_count = None
        self.status_id=None
        self.source=None
        self.resharers=None


    def set_text(self, text):
        self.text = text

    def set_display_name(self, display_name):
        self.display_name = display_name

    def set_display_picture(self, display_picture):
        self.display_picture = display_picture

    def set_time(self, time):
        self.time = time

    def set_reshare_count(self, reshare_count):
        self.reshare_count = reshare_count

    def set_status_id(self, status_id):
        self.status_id = status_id

    def set_source(self, source):
        self.source = source

    def set_resharer(self, resharers):
        self.resharers = resharers

    def get_text(self):
        return self.text
    def get_display_name(self):
        return self.display_name

    def get_display_picture(self):
        return self.display_picture

    def get_time(self):
        return self.time

    def get_reshare_count(self):
        return self.reshare_count

    def get_status_id(self):
        return self.status_id

    def get_source(self):
        return self.source

    def get_resharer(self):
        return self.resharers