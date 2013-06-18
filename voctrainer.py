#!/usr/bin/python

import codecs
import signal
import sys
import random


class VocTrainer(object):
    def __init__(self):
        self.words = []
        self.score = 0
        self.running = False

    def load_file(self, filename):
        self.words = []
        f = codecs.open(filename, 'r', encoding='utf-8')
        for line in f:
            parts = line.split(',')
            if len(parts) > 1:
                self.words.append([trans.strip() for trans in parts])

    def ask_word(self, original, translations):
        print('What is the translation for "%s"?' % (original))
        answer = input()
        if answer.lower() in translations:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong! Correct answer(s) would have been: %s" % (", ".join(translations)))

    def start_training(self):
        self.running = True
        signal.signal(signal.SIGINT, self.stop_training)
        if len(self.words) > 0:
            while self.running:
                word = random.choice(self.words)
                self.ask_word(word[0], word[1:])

    def stop_training(self, *args):
        self.running = False
        print()
        print("Your score: %i" % (self.score))
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please add a filename as parameter to start VocTrainer")
        sys.exit(1)

    voctrainer = VocTrainer()
    voctrainer.load_file(sys.argv[1])
    voctrainer.start_training()

