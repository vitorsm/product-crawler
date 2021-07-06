from dataclasses import dataclass


@dataclass
class Template(object):
    before_name: str
    after_name: str
    before_price: str
    after_price: str
    first_name: bool

    @staticmethod
    def instantiate_from_dto(dto: dict):
        return Template(before_name=dto["before_name"], after_name=dto["after_name"], before_price=dto["before_price"],
                        after_price=dto["after_price"], first_name=dto["first_name"])
