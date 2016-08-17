#!/usr/bin/env python2


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings where
    the string length is 2 or more and the first and last chars of the string
    are the same.
    """
    return len([w for w in words if len(w) >= 2 and w[0]==w[-1] ])


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted order,
    except group all the strings that begin with 'x' first.
    """
    with_x = sorted([w for w in words if w.startswith("x")])
    without_x = sorted([w for w in words if not w.startswith("x")])
    return with_x + without_x


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in increasing order
    by the last element in each tuple.
    """
    return sorted(tuples, lambda l,r : cmp(l[-1], r[-1]))


def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print
    print 'sort_last'
    test(sort_last([(2, 3), (1, 2, 3, 1), (10, 0, 0)]),
         [(10, 0, 0), (1, 2, 3, 1), (2, 3)])
    test(sort_last([(10,), (1, 2), (10, 0, 5)]),
         [(1, 2), (10, 0, 5), (10,)])

main()


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent == elements
    have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3].
    """
    result = []
    for num in nums:
        if len(result) > 0 and result[-1] == num:
            continue
        else:
            result.append(num)
    return result


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a merged list
    of all the elements in sorted order. You may modify the passed in lists. Ideally,
    the solution should work in "linear" time, making a single pass of both lists.
    """
    result = []
    len_result = len(list1) + len(list2)
    index_1, index_2 = 0, 0
    while len(result) < len_result:
        if index_1 >= len(list1):
            result.append(list2[index_2])
            index_2 += 1
        elif index_2 >= len(list2):
            result.append(list1[index_1])
            index_1 += 1
        elif list1[index_1] <= list2[index_2]:
            result.append(list1[index_1])
            index_1 += 1
        else:
            result.append(list2[index_2])
            index_2 += 1
    return result


def main():
    print
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()