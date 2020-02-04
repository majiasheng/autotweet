class Tweet():

    def __init__(self, text: str, media: str = None):
        self.text = text
        self.media = media
        self.posted = False

    def set_posted(self):
        self.posted = True
