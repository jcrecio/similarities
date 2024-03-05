import re
import spacy

nlp = spacy.load("es_core_news_lg")


def get_phrase_from_method(method_name):
    words = re.findall("[a-z]+|[A-Z][a-z]*", method_name)
    s = " ".join(word.lower() for word in words)
    return s[0].capitalize() + s[1:]


def compute_method_similarity(method_name1, method_name2):
    phrase1 = get_phrase_from_method(method_name1)
    phrase2 = get_phrase_from_method(method_name2)
    doc1 = nlp(phrase1)
    doc2 = nlp(phrase2)

    return doc1.similarity(doc2)
