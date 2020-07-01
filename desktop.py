class call_desktop:
    def __init__(self, mssg, game=0, david=0, browser=0, play_f=0):
        self.game = game
        self.david = david
        self.browser = browser
        self.play_f = play_f
        self.mssg = mssg

    def get_mssg(self):
        return self.mssg

    def get_game(self):
        return self.game

    def get_david(self):
        return self.david

    def get_browser(self):
        return self.browser

    def get_play_file(self):
        return self.play_f

    def play_file(self):
        self.play_f = 1

    def play_game(self):
        self.game = 1

    def open_david(self):
        self.david = 1

    def open_browser(self):
        self.browser = 1
