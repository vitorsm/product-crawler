from typing import List, Optional, Tuple

from product_crawler.domain.entities.product import Product
from product_crawler.domain.entities.template import Template
from product_crawler.domain.exceptions.extract_pattern_exception import ExtractPatternException


class ExtractProductService(object):

    @staticmethod
    def extract_product_from_html(html_page: str, template: Template) -> List[Product]:
        max_index = len(html_page) - 1
        index = 0

        products: List[Product] = list()
        while index < max_index:
            result = ExtractProductService.__extract_content_and_next_index(html_page, index, True, template)
            if not result:
                break

            product = Product()
            products.append(product)

            content, index = result

            if template.first_name:
                product.name = content
            else:
                product.price = content

            result = ExtractProductService.__extract_content_and_next_index(html_page, index, False, template)
            if not result:
                break

            content, index = result
            if template.first_name:
                product.price = content
            else:
                product.name = content

        return products

    @staticmethod
    def __extract_content_and_next_index(html_page: str, index: int, is_first: bool,
                                         template: Template) -> Optional[Tuple[str, int]]:
        pattern_start, pattern_end = ExtractProductService.__select_pattern_start_and_end(is_first, template)

        next_index_start = ExtractProductService.__find_next_occurrence_index(html_page, index, pattern_start)
        if next_index_start < 0:
            return None

        next_index_start += index

        next_index_end = ExtractProductService.__find_next_occurrence_index(html_page, next_index_start, pattern_end)
        if next_index_end < 0:
            raise ExtractPatternException(f"End pattern not found: {pattern_end}")

        next_index_end += next_index_start - len(pattern_end)

        content = ExtractProductService.__extract_content(html_page, next_index_start, next_index_end)

        return content, next_index_end + len(pattern_end)

    @staticmethod
    def __select_pattern_start_and_end(is_first: bool, template: Template) -> Tuple[str, str]:
        if is_first:
            pattern_start = template.before_name if template.first_name else template.before_price
            pattern_end = template.after_name if template.first_name else template.after_price
        else:
            pattern_start = template.before_price if template.first_name else template.before_name
            pattern_end = template.after_price if template.first_name else template.after_name

        return pattern_start, pattern_end

    @staticmethod
    def __extract_content(html_page: str, start_index: int, end_index: int) -> str:
        text = html_page[start_index:end_index]
        return text.strip()

    @staticmethod
    def __find_next_occurrence_index(html_page: str, index: int, pattern: str) -> int:
        next_index = html_page[index:].find(pattern)

        if next_index < 0:
            return next_index

        return next_index + len(pattern)
