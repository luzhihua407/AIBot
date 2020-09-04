from programy.parser.pattern.nodes.base import PatternNode
from programy.utils.logging.ylogger import YLogger


class MyPatternNode(PatternNode):

    def is_word(self):
        return super().is_word()

    @property
    def template(self):
        return super().template()

    def equivalent(self, other):
        return super().equivalent(other)

    def equals(self, client_context, words, word_no):
        return super().equals(client_context, words, word_no)

    def equals_ignore_case(self, word1, word2):
        return super().equals_ignore_case(word1, word2)

    def add_child(self, new_node, replace_existing=False):
        return super().add_child(new_node, replace_existing)

    def to_string(self, verbose=True):
        return super().to_string(verbose)

    def dump(self, tabs, output_func=YLogger.debug, eol="", verbose=True):
        super().dump(tabs, output_func, eol, verbose)

    def consume(self, client_context, context, words, word_no, match_type, depth, parent=False):
        return super().consume(client_context, context, words, word_no, match_type, depth, parent)
