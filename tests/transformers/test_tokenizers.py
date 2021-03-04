import pytest

from nlpiper.transformers.tokenizers import BasicTokenizer


class TestRemovePunctuation:
    @pytest.mark.parametrize('inputs,results', [
        ('Test to this test', ['Test', 'to', 'this', 'test']),
        ('numbers 123 and symbols "#$%', ['numbers', '123', 'and', 'symbols', '"#$%']),
    ])
    def test_remove_punctuation(self, inputs, results):
        t = BasicTokenizer()
        assert t(inputs) == results
