import os

from product_crawler.utils.file_utils import FileUtils


class UtilsTest(object):

    @staticmethod
    def get_test_resources_dir() -> str:
        project_dir = FileUtils.get_project_dir()

        return os.path.join(project_dir, "resources")

    @staticmethod
    def get_resource(resource_relative_path: str) -> str:
        return os.path.join(UtilsTest.get_test_resources_dir(), resource_relative_path)
