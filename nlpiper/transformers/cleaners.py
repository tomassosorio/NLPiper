"""Cleaner Module."""

import re
from string import punctuation
from typing import Union

from nlpiper.core.document import Document

__all__ = ["RemoveEmail", "RemoveNumber", "RemoveUrl", "RemovePunctuation"]


class Cleaner:
    """Abstract class to Cleaners."""

    def __init__(self, *args, **kwargs):
        args = {"args": list(args)} if len(args) != 0 else {}
        self.log = {**kwargs, **args}

    def __call__(self, text: Union[str, Document]) -> Document:
        raise NotImplementedError


class RemoveUrl(Cleaner):
    """Remove URLs."""

    def __call__(self, text: Union[str, Document]) -> Document:
        """Remove text URLs.

        Args:
            text (Union[str, Document]): text to be cleaned.

        Returns: Document
        """
        if isinstance(text, str):
            doc = Document(text)
        else:
            doc = text

        if doc.cleaned is None:
            doc.cleaned = doc.text

        doc.cleaned = re.sub(r"http\S+", "", doc.cleaned)
        doc.cleaned = re.sub(r"www\S+", "", doc.cleaned)

        return doc


class RemoveEmail(Cleaner):
    """Remove Emails."""

    def __call__(self, text: Union[str, Document]) -> Document:
        """Remove text Emails.

        Args:
            text (Union[str, Document]): text to be cleaned.

        Returns: Document
        """
        if isinstance(text, str):
            doc = Document(text)
        else:
            doc = text

        if doc.cleaned is None:
            doc.cleaned = doc.text

        doc.cleaned = re.sub(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", "", doc.cleaned)

        return doc


class RemoveNumber(Cleaner):
    """Remove Numbers."""

    def __call__(self, text: Union[str, Document]) -> Document:
        """Remove text Numbers.

        Args:
            text (Union[str, Document]): text to be cleaned.

        Returns: Document
        """
        if isinstance(text, str):
            doc = Document(text)
        else:
            doc = text

        if doc.cleaned is None:
            doc.cleaned = doc.text

        doc.cleaned = re.sub(r'[0-9]+', '', doc.cleaned)
        return doc


class RemovePunctuation(Cleaner):
    """Remove Punctuation."""

    def __call__(self, text: Union[str, Document]) -> Document:
        """Remove Punctuation from text.

        Args:
            text (Union[str, Document]): text to be cleaned.

        Returns: Document

        """
        if isinstance(text, str):
            doc = Document(text)
        else:
            doc = text

        if doc.cleaned is None:
            doc.cleaned = doc.text

        doc.cleaned = doc.cleaned.translate(str.maketrans('', '', punctuation))
        return doc
