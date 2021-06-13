# scrabble_cheater

Scrabble cheater is a command-line program that enables you to find all possible words from a given dictionary matching a requested pattern. 
 
The pattern is an incomplete word (string) in which the empty spaces are replaced by '.' or '*'.  '.' tells the program to search for all words with the same letters as the pattern and any letter in place of '.' . '*' doesn the same, but it makes the program to look for any number of letters. The number of '.' and '*' in a pattern is unlimited.

Examples of patterns: 've.icle', 'judg*', 'ep.ste*ic'.  
Outputs: {'ve.icle',['vehicle']}, {'judg*', ['judge', 'judges', 'judgement', 'judgemental', 'judgements', 'judgy']}, {'ep.ste*ic', ['epistemic']}
