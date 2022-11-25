from datetime import date
from functools import partial
from typing import Any, Dict, Type

from factory import Factory
from factory.base import StubObject

DATE_FORMAT = "%Y-%m-%d"


def _convert_dict_from_stub(stub: StubObject) -> Dict[str, Any]:
    stub_dict = stub.__dict__
    for key, value in stub_dict.items():
        if isinstance(value, StubObject):
            stub_dict[key] = _convert_dict_from_stub(value)
        if isinstance(value, date):
            stub_dict[key] = value.strftime(DATE_FORMAT)
    return stub_dict


def _dict_factory(factory_class, **kwargs):
    stub = factory_class.stub(**kwargs)
    stub_dict = _convert_dict_from_stub(stub)
    return stub_dict


def create_dict_factory(factory_class: Type[Factory]):

    return partial(_dict_factory, factory_class)
