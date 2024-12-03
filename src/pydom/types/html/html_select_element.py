from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLSelectElement(HTMLElementProps, total=False):
    auto_complete: Optional[str]
    auto_focus: Optional[bool]
    disabled: Optional[bool]
    form: Optional[str]
    multiple: Optional[bool]
    name: Optional[str]
    required: Optional[bool]
    size: Optional[int]
