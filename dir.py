import os


# from call_script import callpy

class give_path:
    def __init__(self):
        pass

    def p_path(self):
        path = os.getcwd()
        os.chdir(path + "{}".format("\\spaceinvader"))
        path = path + "{}".format("\\spaceinvader\\main.py")
        return path

# callable_obj = callpy(path)
# callable_obj.call_python_file()
