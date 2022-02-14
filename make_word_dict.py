import requests
from bs4 import BeautifulSoup


class make_word_dict():
    def __init__(self, loaded_words=False, dictionary=False):
        self.get_random_url = 'https://en.wikipedia.org/wiki/Special:Random'
        if loaded_words:
            self.words_5 = loaded_words
        else:
            self.words_5 = []
        if dictionary:
            self.dictionary = dictionary
        else:
            self.dictionary = {}
        self.get_current_number()

    def get_page_data(self):
        random_response = requests.get(self.get_random_url, auth=False)
        url = random_response.url
        print(random_response.url)
        page = requests.get(url, auth=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        ###
        paragraphs = len(soup.find_all('p'))
        page_string = ""
        for p in range(paragraphs):
            page_string = page_string + soup.find_all('p')[p].get_text()
        words = page_string.split(" ")
        return words

    def get_words_5(self, words):
        for word in range(len(words)-1,-1,-1):
            if len(words[word])<5:
                words.remove(words[word])
        for word in range(len(words) - 1,-1,-1):
            if not words[word].isalpha():
                words[word] = ''.join(filter(str.isalpha, words[word]))
            if (len(words[word]) != 5) or (not words[word].isascii()):
                words.remove(words[word])
        self.words_5 = self.words_5 + words

    def add_to_dict(self,number):
        temp = len(self.words_5)
        while len(self.words_5) < number + temp:
            self.get_words_5(self.get_page_data())
            print(f'number of additional 5 letter words: {len(self.words_5)}')
        for word in self.words_5:
            if word not in self.dictionary:
                self.dictionary[word] = 1
            else:
                self.dictionary[word] = self.dictionary[word] + 1
        self.get_current_number()
        print(f'total number of words: {self.current_number}')
        self.words_5 = []

    def get_current_number(self):
        self.current_number = 0
        for key in list(self.dictionary.keys()):
            self.current_number += self.dictionary[key]

    def remove_proper_nouns(self):
        for key in list(self.dictionary.keys()):
            if key[0].isupper():
                del self.dictionary[key]

    def save_dict(self):
        f = open("dictionary_5.py", "w")
        f.write(f'words_5_dict={str(self.dictionary)}')
        f.close()
