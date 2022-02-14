from make_word_dict import make_word_dict
from game_logic import game_logic
try:
    from dictionary_5 import words_5_dict
except:
    words_5_dict = {}

loaded_words = []
words = make_word_dict(loaded_words=loaded_words, dictionary=words_5_dict)
#words.add_to_dict(20000)
#words.remove_proper_nouns()
#words.save_dict()
sorted_dict = dict(sorted(words.dictionary.items(), key=lambda item: item[1], reverse=True))
game = game_logic(words.dictionary)
game.first_word('drive')




