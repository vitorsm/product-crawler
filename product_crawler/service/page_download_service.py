import requests

from product_crawler.domain.exceptions.request_exception import RequestException


class PageDownloadService(object):

    @staticmethod
    def download_page(address: str) -> str:
        response = requests.get(address)

        if response.status_code < 200 or response.status_code >= 300:
            RequestException(response.status_code, response.text)

        return response.text
