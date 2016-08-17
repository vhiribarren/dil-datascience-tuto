#!/usr/bin/env python2


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the form 'Number of donuts: ',
    where is the number passed in. However, if the count is 10 or more, then use the word 'many'
    instead of the actual count.
    So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
    """
    return "Number of donuts: {}".format("many" if count >= 10 else count)


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last 2 chars of the original
    string, so 'spring' yields 'spng'. However, if the string length is less than 2, return
    instead the empty string.
    """
    if len(s) <= 2:
        return ""
    return s[0:2] + s[-2:]


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its first char have been changed
    to '*', except do not change the first char itself.
    e.g. 'babble' yields 'ba**le'
    Assume that the string is length 1 or more. Hint: s.replace(stra, strb) returns a version
    of string s where all instances of stra have been replaced by strb.
    """
    if len(s) < 2:
        return s
    return s[0] + s[1:].replace(s[0], "*")


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b separated by a space '<a> <b>',
    except swap the first 2 chars of each string.
    e.g.
    'mix', pod' -> 'pox mid'
    'dog', 'dinner' -> 'dig donner'

    Assume a and b are length 2 or more.
    """
    return b[0:2]+a[2:]+" "+a[0:2]+b[2:]


def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


main()


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end. Unless it
    already ends in 'ing', in which case add 'ly' instead. If the string length is
    less than 3, leave it unchanged. Return the resulting string.
    """
    if len(s) < 3:
        return s
    return s + ("ly" if s[-3:] == "ing" else "ing")


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not' and 'bad'. If
    the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
    Return the resulting string.
    So 'This dinner is not that bad!' yields: This dinner is good!
    """
    index_bad = s.find("bad")
    index_not = s.find("not")
    if index_bad > index_not:
        return s[:index_not] + "good" + s[index_bad+3:]
    else:
        return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even, the front and
    back halves are the same length. If the length is odd, we'll say that the extra
    char goes in the front half.
    e.g. 'abcde', the front half is 'abc', the back half 'de'.
    Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back
    """
    a_split = len(a) // 2 + (len(a) % 2)
    b_split = len(b) // 2 + (len(b) % 2)
    a_front, a_back = a[:a_split], a[a_split:]
    b_front, b_back = b[:b_split], b[b_split:]
    return  a_front + b_front + a_back + b_back


def main():
    print
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


main()