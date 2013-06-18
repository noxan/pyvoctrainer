#!/usr/bin/python

import sys
import codecs


class VocTrainer(object):
    def load_file(self, filename):
        f = codecs.open(filename, 'r', encoding='utf-8')
        for line in f:
            parts = line.split(',')
            if len(parts) > 1:
                orig = parts[0].strip()
                translations = [trans.strip() for trans in parts[1:]]

                print(orig, translations)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please add a filename as parameter to start VocTrainer")
        sys.exit(1)

    voctrainer = VocTrainer()
    voctrainer.load_file(sys.argv[1])
