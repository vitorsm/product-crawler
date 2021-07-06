import os
from typing import List


class FileUtils(object):
    file_utils = None

    @staticmethod
    def get_project_dir() -> str:
        dir_path = os.getcwd()
        return dir_path.split("product-crawler")[0] + "product-crawler"

    @staticmethod
    def get_all_file_paths_from_directory(directory: str) -> List[str]:
        file_names = os.listdir(directory)
        if not file_names:
            return file_names

        return [os.path.join(directory, name) for name in file_names]
