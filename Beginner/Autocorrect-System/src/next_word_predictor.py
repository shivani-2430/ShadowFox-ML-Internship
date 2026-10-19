import re
from collections import Counter, defaultdict


class NextWordPredictor:
    def __init__(self, corpus=None):
        self.corpus = corpus or [
            "i love machine learning",
            "i love python programming",
            "i enjoy machine learning",
            "machine learning is useful",
            "machine learning helps people",
            "python programming is fun",
            "python is easy to learn",
            "deep learning uses neural networks",
            "learning python is useful",
            "i enjoy learning new things",
            "artificial intelligence is growing",
            "artificial intelligence helps people",
            "people use machine learning",
            "people learn python programming"
        ]
        self.unigrams = Counter()
        self.bigrams = defaultdict(Counter)
        self.trigrams = defaultdict(Counter)
        self._train()

    def _tokenize(self, text):
        return re.findall(r"[a-z]+", text.lower())

    def _train(self):
        for sentence in self.corpus:
            words = self._tokenize(sentence)

            for word in words:
                self.unigrams[word] += 1

            for index in range(len(words) - 1):
                self.bigrams[words[index]][words[index + 1]] += 1

            for index in range(len(words) - 2):
                context = (words[index], words[index + 1])
                self.trigrams[context][words[index + 2]] += 1

    def predict_next_word(self, text, limit=3):
        words = self._tokenize(text)

        if not words:
            return []

        if len(words) >= 2:
            context = (words[-2], words[-1])
            candidates = self.trigrams.get(context, Counter())

            if candidates:
                return [
                    word
                    for word, _ in candidates.most_common(limit)
                ]

        candidates = self.bigrams.get(words[-1], Counter())

        if candidates:
            return [
                word
                for word, _ in candidates.most_common(limit)
            ]

        return [
            word
            for word, _ in self.unigrams.most_common(limit)
        ]