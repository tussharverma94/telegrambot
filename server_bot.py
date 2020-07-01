import socket
from desktop import call_desktop
import pickle


class throw:
    def __init__(self, mssg, game=0, david=0, browser=0, play_f=0):
        self.game = game
        self.david = david
        self.browser = browser
        self.play_f = play_f
        self.mssg = mssg
        self.dek = call_desktop(self.mssg)
        self.server = socket.gethostname()
        self.port = 4231
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # this fuction will provide the message that should be sent to the client
    def initial_var(self):
        if self.game == 1:
            self.dek.play_game()
        if self.browser == 1:
            self.dek.open_browser()
        if self.david == 1:
            self.dek.open_david()
        if self.play_f == 1:
            self.dek.play_file()
        try:
            self.s.bind((self.server, self.port))
            self.s.listen()
            print("waiting for the connection server started")

        except Exception as e:
            str(e)
            print("Falied due to some error")

    def give_false(self):
        return 0

    def give_true(self):
        return 1

    # this message sends the call_desktop object to the client
    def get_farther(self):

        try:
            conn, add = self.s.accept()
            print("connected to {}".format(self.server))

            """add a query"""
            conn.sendall(pickle.dumps(self.dek))
            conn.close()
            return self.give_true()
        except Exception as e:
            return self.give_false()

# thr = throw()
# r = thr.get_farther()
# print(r)
