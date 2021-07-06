import json
import os
from typing import List
from time import sleep
import traceback

from product_crawler.domain.entities.product import Product
from product_crawler.domain.entities.source import Source
from product_crawler.service.extract_product_service import ExtractProductService
from product_crawler.service.page_download_service import PageDownloadService
from product_crawler.utils.file_utils import FileUtils


WAIT_TIME_SECONDS = 60


class MonitoringProductService(object):

    @staticmethod
    def start_monitoring():
        sources = MonitoringProductService.__get_sources()

        while True:
            for source in sources:
                try:
                    products = MonitoringProductService.__get_products_from_source(source)
                    print(f"found {len(products)} products")
                    MonitoringProductService.__notify_product(products)
                except Exception as ex:
                    traceback.print_exc()
                    print(f"Error: {ex}")

            print(f"will wait {WAIT_TIME_SECONDS} seconds to get again")
            sleep(WAIT_TIME_SECONDS)

    @staticmethod
    def __notify_product(products: List[Product]):
        for product in products:
            if product.price:
                print(f"Notify {product.name}, price: {product.price}")

    @staticmethod
    def __get_products_from_source(source: Source) -> List[Product]:
        html_page = PageDownloadService.download_page_and_retry(source.address)
        return ExtractProductService.extract_product_from_html(html_page, source.template)

    @staticmethod
    def __get_sources() -> List[Source]:
        file_paths = MonitoringProductService.__get_source_files()
        sources: List[Source] = list()

        for file_path in file_paths:
            file = open(file_path, "r")
            sources.append(Source.instantiate_from_dto(json.load(file)))
            file.close()

        return sources

    @staticmethod
    def __get_source_files() -> List[str]:
        directory = os.path.join(FileUtils.get_project_dir(), "resources", "sources")
        return FileUtils.get_all_file_paths_from_directory(directory)
