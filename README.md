# **scrabble_cheater**

# General info

Scrabble cheater is a command-line program that enables you to find all possible words matching a requested pattern and its anagrams (optionally).


**The pattern** is an incomplete word in which the empty spaces are replaced by **'.'** or **'\*'**.

**'.'** in a pattern tells the program to search for all words with the same letters as the pattern and any letter in place of **'.'**. Examples:

* for **ve.icle** it would find: 'vehicle'
* for **judg.** it would find: 'judge' and 'judgy'

**'\*'** does the same, but instead of one letter the program looks for any number of matching letters. Examples:

* for **judg\*** it would find: 'judges', 'judgement', 'judgemental', 'judgements', 'judgy'
* for **ep.ste\*ic** it would find only 'epistemic'

The number of '.'s and '\*'s in a pattern is unlimited.

### Input:

* dictionary file - a txt file being a subset of https://sjp.pl/slownik/odmiany/
* patterns file - a txt file consisting of patterns for our search

### Output:

* .json file consisting of a Python dictionary with patterns as keys and pattern-matching words as its values.
* .json file consisting of a Python dictionary with patterns as keys and patterns' anagrams as its values (optional).



# Technology
Python (3.5 or newer) and Bash (or a different Unix shell) are required to run this program.

# Setup
In the program directory save also dictionary and patterns files.

In your command line type:

$ python3 cheater_final.py [-h] [-o] [-a] dictionary patterns

**positional arguments:**

  *dictionary* -          a txt file being a subset of https://sjp.pl/slownik/odmiany/

  *patterns* -            a txt file consisting of patterns to be found in a dictionary

**optional arguments:**

  -h, --help          -  show this help message and exit

  -o , --output_filename -
                        indicate a name of the output file

  -a , --anagrams_filename -
                        find anagrams of the patterns and name the output file
