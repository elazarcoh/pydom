from .component import Component
from .context.context import Context, set_default_context
from .html import *
from .rendering import render
from .version import version as __version__

set_default_context(Context.standard())

__all__ = [
  "A",
  "Abbr",
  "Address",
  "Area",
  "Article",
  "Aside",
  "B",
  "Base",
  "BlockQuote",
  "Body",
  "Br",
  "Button",
  "Canvas",
  "Cite",
  "Code",
  "Col",
  "Component",
  "Context",
  "Div",
  "Em",
  "Embed",
  "Footer",
  "Form",
  "Fragment",
  "H1",
  "H2",
  "H3",
  "H4",
  "H5",
  "H6",
  "Head",
  "Header",
  "Hr",
  "Html",
  "I",
  "Img",
  "Input",
  "Label",
  "Li",
  "Link",
  "Main",
  "Meta",
  "Nav",
  "Ol",
  "Option",
  "P",
  "Param",
  "Pre",
  "Script",
  "Section",
  "Select",
  "Small",
  "Source",
  "Span",
  "Strong",
  "Style",
  "Sub",
  "Sup",
  "Table",
  "TBody",
  "Td",
  "TextArea",
  "Th",
  "THead",
  "Time",
  "Title",
  "Tr",
  "Track",
  "U",
  "Ul",
  "Wbr",
  "render",
  "__version__",
]
