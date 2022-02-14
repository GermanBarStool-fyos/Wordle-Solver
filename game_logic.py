class game_logic():
    def __init__(self,dictionary):
        self.known_places = {1: None,
                             2: None,
                             3: None,
                             4: None,
                             5: None,
                             }
        self.known_letters = []
        self.known_places_false = {1: [],
                                   2: [],
                                   3: [],
                                   4: [],
                                   5: [],
                                   }
        self.known_letters_false = []
        self.guessed_words = []
        self.dictionary = dictionary

    def provide_known_place(self,letter,index):
        if not letter.isalpha():
            print(f"{letter} is not a letter")
            return
        self.known_places[index] = letter
        #self.provide_known_letter(letter)

    def provide_known_letter(self,letter):
        if not letter.isalpha():
            print(f"{letter} is not a letter")
            return
        self.known_letters += letter

    def check_known_places(self,word):
        for i in range(len(word) - 1):
            #if not self.known_places[i+1] is None:
            if self.known_places[i+1]:
                if word[i] != self.known_places[i+1]: #This will always be called because the known_places will be none.
                    return False #Must also return false if all are None
        return True

    def check_known_places_false(self,word):
        for i in range(len(word) - 1):
            for j in self.known_places_false[i+1]:
                if word[i] == j:
                    return False
        return True

    def check_known_letter_false(self,word):
        for i in word:
            if i in self.known_letters_false:
                return False
        return True

    def remove_false_letters(self):
        for position in self.known_places.keys():
            if self.known_places[position]:
                if self.known_places[position] in self.known_letters_false:
                    self.known_letters_false.remove(self.known_places[position])

    def check_known_letters(self,word):
        for i in self.known_letters:
            if i not in word:
                return False
        return True

    def populate_false(self):
        if self.guessed_words:
            for i in range(len(self.guessed_words[-1])-1):
                if self.guessed_words[-1][i] != self.known_places[i+1]:
                    self.known_places_false[i+1] = self.guessed_words[-1][i]
                if self.guessed_words[-1][i] not in self.known_letters:
                    self.known_letters_false.append(self.guessed_words[-1][i])
        self.remove_false_letters()

    def guess_word(self):
        self.populate_false()
        for word in self.dictionary.keys():
            if self.check_known_places(word):
                if self.check_known_letters(word):
                    if self.check_known_letter_false(word):
                        if self.check_known_places_false(word):
                            self.guessed_words.append(word)
                            return word
        return "No word in dictionary"

    def first_word(self,word):
        self.guessed_words.append(word)

