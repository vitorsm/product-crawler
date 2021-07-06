import json
import os
import unittest

from product_crawler.domain.entities.source import Source
from product_crawler.service.extract_product_service import ExtractProductService
from tests.utils_test import UtilsTest


class TestExtractProductService(unittest.TestCase):

    def setUp(self):
        self.source_dto_file_path1 = UtilsTest.get_resource(os.path.join("sources", "amazon_chromebook.json"))
        self.page_file_path1 = UtilsTest.get_resource(os.path.join("pages", "amazon_chromebook.html"))

    def test_extract_product1(self):
        source_dto_file1 = open(self.source_dto_file_path1, "r")
        source_dto = json.load(source_dto_file1)
        source_dto_file1.close()

        source = Source.instantiate_from_dto(source_dto)

        page_file1 = open(self.page_file_path1, "r")
        page1 = page_file1.read()
        page_file1.close()

        products = ExtractProductService.extract_product_from_html(page1, source.template)

        self.assertEqual(1, len(products))
        self.assertEqual("Chromebook Acer R721T-488H AMD A4-9120C 4GB 11,6&quot; Chrome OS", products[0].name)
        self.assertEqual("R$1.999,00", products[0].price)
