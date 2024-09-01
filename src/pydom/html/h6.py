from typing import Unpack

from ..element import Element
from ..types.html import HTMLHeadingElement
from ..types import ChildType


class H6(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLHeadingElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "h6"
