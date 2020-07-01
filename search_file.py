import glob, os


class search_f:
    def __init__(self, name, extension=".mkv", base_path="E:\\"):
        self.base_path = base_path
        self.extension = extension
        self.name = name
        self.path = self.base_path + "**\\*" + self.extension
        # path = "E:\**" + "\*" + extension
        files = glob.iglob(self.path, recursive=True)
        # print(len(files))
        # print(files)

        while True:
            value_of_it = next(files)
            if name in value_of_it.lower():
                os.startfile(value_of_it)
                # print(value_of_it)
                break

# f = search_f("extraction")
