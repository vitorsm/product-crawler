from dataclasses import dataclass

from product_crawler.domain.entities.template import Template


@dataclass
class Source(object):
    address: str
    template: Template

    @staticmethod
    def instantiate_from_dto(dto: dict):
        return Source(address=dto["address"], template=Template.instantiate_from_dto(dto["template"]))
