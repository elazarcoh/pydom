from typing import Unpack

from ..element import Element
from ..types.html import HTMLElementProps
from ..types import ChildType


class Figure(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLElementProps"]):
        super().__init__(*children, **kwargs)

    tag_name = "figure"
