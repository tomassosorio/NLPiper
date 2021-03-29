"""Transformers Module."""
from nlpiper.core.document import Document
from nlpiper.logger import log


class BaseTransformer:
    """Base class to all Transformers."""

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        log.info("[Created] %s", repr(self))

    def __repr__(self) -> str:
        """Create a string representation including init params."""
        params = ', '.join(
            ["%r" % a for a in self.args] +
            ["%s=%r" % (k, v) for k, v in self.kwargs.items()]
        )
        return "%s(%s)" % (self.__class__.__name__, params)

    def __call__(self, doc: Document) -> Document:
        raise NotImplementedError

    def _add_step(self, doc: Document) -> None:
        """Register a step transformation into the document object."""
        doc.steps.append(repr(self))
