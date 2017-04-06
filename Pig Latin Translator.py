#Pig Latin Translator

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0:
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    original = new_word[1:len(new_word)]
    print original
else:
    print 'empty'