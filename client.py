import pickle
from desktop import call_desktop
import socket
import webbrowser
from dir import give_path
from call_script import callpy
from search_file import search_f
from temp import david_helper
# import os

class throw:
    def __init__(self):
        self.server = socket.gethostname()
        self.port = 4231
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.connect((self.server, self.port))
            self.get_mssg()
        except Exception as e:
            pass

    def get_mssg(self):
        result = pickle.loads(self.s.recv(4096 * 2))
        mssg_ = result.get_mssg().strip()
        print("{} reached before if".format(mssg_))
        david_fi = result.get_david()
        brows_fi = result.get_browser()
        play_fi = result.get_play_file()
        game_fi = result.get_game()
        print("david_fi = {}\nbrows_fi = {}\nplay_fi = {}\ngame_fi = {}".format(david_fi, brows_fi, play_fi, game_fi))

        try:
            if game_fi == 1:
                print("Playing Game")
                provide_path = give_path()
                path = provide_path.p_path()
                call_obj = callpy(path)
                call_obj.call_python_file()
        except Exception as e:
            pass

        try:
            if david_fi == 1: #C:\Python\Python38\python.exe C:/Users/tussh/PycharmProjects/jarvis/main.py
                david = david_helper()
                david.call_david()

                """not able to call david from this commented code
                path_for_david = "C://Users//tussh//PycharmProjects//jarvis//main.py"
                david_py = callpy()
                david_py.call_python_file(path_for_david)
                """

                # open_david = mssg_
                # if open_david == "open":
                # else:
                #     open_david == "close"
                #     pass
        except Exception as e:
            pass

        try:
            if brows_fi == 1:
                print("opening Browser")
                file_to_be_searched = mssg_.replace(" ", "+")
                link_to_be_searched = "http://google.com/search?q=" + file_to_be_searched
                webbrowser.open(link_to_be_searched)
        except Exception as e:
            pass

        try:
            if play_fi == 1:
                # print("reached")
                file_to_be_searched = result.get_mssg().strip()
                sear_obj = search_f(file_to_be_searched)
                # print(file_to_be_searched)
                # print("playing file")
        except Exception as e:
            print(e)


while True:
    tr = throw()
