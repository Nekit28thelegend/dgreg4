class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        words = []
        str_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as opener:
                for line in opener:
                    line = line.lower()
                    for p in str_punctuation:
                        if p in line:
                            line = line.replace(p, '')
                    split_line = line.split()
                    words.append(split_line)
        sorted_list = [x for y in words for x in y]
        all_words[self.file_name] = sorted_list
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        word_place = {}
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w:
                    index = words.index(w)
                    word_place[name] = index +1
        return word_place
    def count(self, word):
        dict_ = self.get_all_words()
        word_counts = {}
        count = 0
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w:
                    count += 1
        word_counts[name] = count
        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего






