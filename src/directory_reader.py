import os


def dir_reader_generator(file_path):
    for root, dirs, files in os.walk(file_path):
        if files:
            for file in files:
                if len(file) > 11:
                    yield root + "\\" + file


class DirReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        return dir_reader_generator(self.file_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # def work(self):
    #     for root, dirs, files in self.walk:
    #         if files:
    #             for file in files:
    #                 if file.len > 11:
    #                     yield root + "\\" + file
    #
    # def __iter__(self):
    #     return self.work()