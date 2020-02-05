class Tweet():

    def __init__(self, status: str, media: str = None):
        self.status = status
        self.media = media
        self.posted = False

    def set_posted(self):
        self.posted = True
