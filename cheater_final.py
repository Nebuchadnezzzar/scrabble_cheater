import argparse
import json
import re

# a function that finds words from a dictionary which match a pattern


def matches_finder(pattern, dictionary):
    reg_pattern = pattern.replace('.', '[A-Źa-ź]').replace('*', '[A-Źa-ź]+')
    reg_pattern = "(^|\s)" + reg_pattern + "(\s|$)"
    matches = {}
    for line in dictionary:
        matchingwords = []
        listed_line = line.split(',')
        for word in listed_line:
            if re.match(reg_pattern, word) is not None:
                matchingwords.append(re.match(reg_pattern, word).group(0))
        if len(matchingwords) != 0:
            matches[listed_line[0]] = matchingwords
    return matches

# a function that find anagrams of patterns in a given dictionary


def anagrams_finder(pattern, dictionary):
    anagrams = []
    if "." and "*" not in pattern:
        listed_pattern = list(pattern)
        for line in dictionary:
            splitted_line = line.split(', ')
            for word in splitted_line:
                listed_word = list(word)
                if sorted(listed_pattern) == sorted(listed_word):
                    anagrams.append(word)
    if "*" in pattern:
        listed_pattern = list(pattern)
        num_stars = listed_pattern.count('*')
        listed_pattern_re = list(pattern.replace('.', '').replace('*', ''))
        for line in dictionary:
            splitted_line = line.split(', ')
            for word in splitted_line:
                if len(word) >= len(listed_pattern_re) + num_stars:
                    if all(element in word for element in listed_pattern_re):
                        anagrams.append(word)
    if "." in pattern:
        listed_pattern = list(pattern.replace('.', ''))
        for line in dictionary:
            splitted_line = line.split(', ')
            for word in splitted_line:
                if len(word) == len(pattern):
                    if all(element in word for element in listed_pattern):
                        anagrams.append(word)
    return sorted(anagrams)


# a parser enabling input of the required files
parser = argparse.ArgumentParser()
parser.add_argument(
    "dictionary",
    help="a subset of https://sjp.pl/slownik/odmiany/")
parser.add_argument(
    "patterns",
    help="a file consisting of patterns to be found in a dictionary")
parser.add_argument(
    "-o",
    "--output_filename",
    help="indicate a name of the output file",
    metavar="",
    default='output.json')
parser.add_argument(
    "-a",
    "--anagrams_filename",
    help="find anagrams of the patterns and name the output file",
    metavar="")

args = parser.parse_args()

# opening the parsed files and converting them to the necessary form
dictionary = open(args.dictionary, 'r')
dictionary = dictionary.readlines()

patterns = open(args.patterns, 'r')
patterns = list(patterns)

# getting rid of "\n" at the end of every pattern
corrected_patterns = []

for pattern in patterns:
    corrected_patterns.append(pattern.strip())

patterns = corrected_patterns

# producing the output
result = {}
for pattern in patterns:
    result[pattern] = matches_finder(pattern, dictionary)

# saving the output as a .json file
if ".json" not in args.output_filename:
    args.output_filename = args.output_filename + ".json"

with open(args.output_filename, 'w') as f_obj:
    json.dump(result, f_obj, ensure_ascii=False)


# optional anagrams
if args.anagrams_filename:
    anagrams = {}
    for pattern in patterns:
        anagrams[pattern] = anagrams_finder(pattern, dictionary)

    with open(args.anagrams_filename, 'w') as f_obj:
        json.dump(anagrams, f_obj, ensure_ascii=False)
