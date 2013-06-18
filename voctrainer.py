#!/usr/bin/python

import codecs
import sys
import random


class VocTrainer(object):
    def load_file(self, filename):
        self.words = []
        f = codecs.open(filename, 'r', encoding='utf-8')
        for line in f:
            parts = line.split(',')
            if len(parts) > 1:
                self.words.append([trans.strip() for trans in parts])

    def start_training(self):
        if len(self.words) > 0:
            word = random.choice(self.words)
            print(word)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please add a filename as parameter to start VocTrainer")
        sys.exit(1)

    voctrainer = VocTrainer()
    voctrainer.load_file(sys.argv[1])
    voctrainer.start_training()

