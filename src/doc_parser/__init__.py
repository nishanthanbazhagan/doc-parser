from .parser import DocumentParser, PDFPageConfig, DocumentParserError, UnsupportedFileError
from .llm import LLMError, UnsupportedModelError
from .utils import ImageExtractionError
from importlib.metadata import version, PackageNotFoundError
from .constants import SUPPORTED_MODELS

try:
    __version__ = version("doc-parser")
except PackageNotFoundError:
    # Use a development version when package is not installed
    __version__ = "0.0.0.dev0"

__all__ = [
    "DocumentParser",
    "PDFPageConfig",
    "ImageExtractionError",
    "DocumentParserError",
    "UnsupportedFileError",
    "UnsupportedModelError",
    "LLMError",
    "SUPPORTED_MODELS",
    "__version__",
]
