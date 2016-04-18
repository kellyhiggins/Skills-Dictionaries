# For every one of these problems,
# Python dictionaries (or sets) are part of the solution
# (even if what is returned in the end is not a dictionary or a set).

# Hints

# keys()
# setdefault and get
# iteritems
# sorted and this guide to sorting in python



"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
# make an empty set
    unique_words = set()

# iterate over the list given, and append each item (word) to the set
# this will take out the duplicates
    for word in words:
        unique_words.add(word)

# convert back to list
    return list(unique_words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

# turn lists into sets
    items1 = set(items1)
    items2 = set(items2)
# make a new set from '&', which finds set intersections
    common_items = items1 & items2
# turn that set into a list
    return list(common_items)


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

# make an empty set
    word_count = {}
# split the phrase, entered as a string, into list of words
    words = phrase.split()
# iterate over list of words
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    # the .get(key, [default]) method returns the value associated with the given key
    # therefore, this assigns the value of 1 for the key in the list,
    # by setting the default to 0 and then adding 1 for each instance it appears

    # the longer way to write that would have been:
    # for word in words:
    #   if word in word_count:
    #       word_count[word] += 1
    #   else:
    #       word_count[word] = 1

    return word_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

# create a dictionary that uses the standard English word as the key,
# and the pirate translation as value
    pirate_speak = {
                    "sir": "matey",
                    "hotel": "fleabag inn",
                    "student": "swabbie",
                    "man": "matey",
                    "professor": "foul blaggart",
                    "restaurant": "galley",
                    "your": "yer",
                    "excuse": "arr",
                    "students": "swabbies",
                    "are": "be",
                    "restroom": "head",
                    "my": "me",
                    "is": "be"
    }

# split the input phrase, which will be a string, into its words
    words = phrase.split()
# create an empty list to append the phrase as it's being translated
    translated_pirate_phrase = []

# iterate over list of words (input phrase)
    for word in words:
# if the english word is a key, it has a pirate translation as value
        if word in pirate_speak:
# subsitute the value of the key for the key itself in the translation
            translated_pirate_phrase.append(pirate_speak[word])
# otherwise, the word won't have a pirate translation, and should be added as-is
        else:
            translated_pirate_phrase.append(word)

# join the list with spaces to return a phrase translated to pirate
    return (' ').join(translated_pirate_phrase)

def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """

# create an empty dictionary - {length: [list of words of that length]}
    words_and_length = {}

# iterate over list of words
    for word in words:
# if the length is already a key in the dictionary,
        if len(word) in words_and_length:
# the word will append to a list of those words
            words_and_length[len(word)].append(word)
        else:
# otherwise, it will create a list of the values, and put that word in a list
            words_and_length[len(word)] = [word]

# dictionary.items() returns a list of tuples of keys and their values
    print words_and_length.items()
# returns (length, [list of words of that length])


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

# I could not get this to work. My brain feels scrambled with it. 
# make an empty list in which to store pairs that will sum to zero
    sum_zero_pairs = []

# omit duplicates by converting numbers to a set
    input_nums = set(numbers)
    input_nums = list(input_nums)

# As per the instructions, if zero is in the input list of numbers,
# it should be returned in the results
    if 0 in input_nums:
        sum_zero_pairs.append([0,0])
# make an empty dictionary to store sums
    sums = {}

    for i in range(len(input_nums)):
        for e in range(len(input_nums)):
            sums[(input_nums[i], input_nums[e])] = input_nums[i] + input_nums[e]

    for key in sums:
        if sums[key] == 0:
            sum_zero_pairs.append(sums.values())

    return sum_zero_pairs

# # I think iter is key here, but i'm a little unclear about how to use it.
# # i found this, but it doesn't make enough sense to me to feel comfortable
# # submitting it as my answer. I want to better understand itertools.
#     import itertools
#     for n in itertools.combinations(input_list, 2):
#         if n[0] + n[1] == 0:
#             sum_zero_pairs.append(list(n))


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

# I could not get this to work either, I had a few drafts of how to solve it,
# but time is running out.

# create an empty list in which to put the results
    return_list = []
# start with first name in input list 'names'
    first_name = names[0]

# make an empty dictionary in which to store words based upon their first letter
    first_letter = {}
# cycle through list of names and make a dictionary based upon first letter
    for name in names:
        if name[0] in first_letter:
            first_letter[name[0]].append(name)
        else:
            first_letter[name[0]] = [name]

# assign variable of last letter of first name
    last_letter = first_name[-1]

# create a while loop that breaks when a first letter has no corresponding value
    if last_letter in first_letter:
        new_word = first_letter[last_letter][0]
        return_list.append(new_word)
        del first_letter[first_name[0]][0]
        first_name = new_word
        last_letter = first_name[-1]
    else:
        return

    return return_list

# this was a first draft where I made two separate dictionaries,
# one dictionary was meant to be organized by first letter, the other by last
# i abandoned this notion because it seemed more complicated than what was possible

# # create an empty list in which to put the results
#     return_list = []
# # start with first name in input list 'names'
#     first_name = names[0]
# # this name will be the first in the list that we return
#     return_list.append(first_name)

# # convert first_name string to list, take last letter
#     first_name = first_name.split()
#     first_name_last_letter = first_name[-1]

# # make an empty dictionary in which to store words based upon their first letter
#     first_letter = {}
# # make an empty dictionary in which to store words based upon their last letter
#     last_letter = {}
# # split the list of names into dictionaries based upon their first & last letter
#     for name in names:
#         split_name = name.split()
#         first_letter[split_name[0]] = name
#         last_letter[split_name[-1]] = name

#     print first_letter
#     print last_letter

#     print return_list


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
