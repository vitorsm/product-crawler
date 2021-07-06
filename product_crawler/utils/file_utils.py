import os


class FileUtils(object):
    file_utils = None

    @staticmethod
    def get_project_dir() -> str:
        dir_path = os.getcwd()
        return dir_path.split("product-crawler")[0] + "product-crawler"
