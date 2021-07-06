import requests
from time import sleep

from product_crawler.domain.exceptions.request_exception import RequestException


WAIT_CALL_REQUEST_AGAIN = 20


class PageDownloadService(object):

    @staticmethod
    def download_page_and_retry(address: str, attempt: int = 10) -> str:
        try:
            return PageDownloadService.download_page(address)
        except RequestException as ex:
            if attempt < 0:
                raise ex
            else:
                sleep(WAIT_CALL_REQUEST_AGAIN)
                return PageDownloadService.download_page_and_retry(address, attempt - 1)

    @staticmethod
    def download_page(address: str) -> str:
        print(f"will get page: {address}")

        response = requests.get(address)

        if response.status_code < 200 or response.status_code >= 300:
            raise RequestException(response.status_code, "Error to download page")

        return response.text
