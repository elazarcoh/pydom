from typing import Unpack

from ..element import Element
from ..types.html import HTMLTableSectionElement
from ..types import ChildType


class TFoot(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableSectionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "tfoot"
