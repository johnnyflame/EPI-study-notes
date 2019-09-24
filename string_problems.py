import functools,string


"""
Code of selected string problems from Elements of Programming Interviews.
For the purpose of learning and improving understanding.


1,2,4,5,6
"""


def is_palindromic(s):
    """
    Boot camp question--palindromic string
    :param s: a string to be assessed
    :return: boolean, true if the string is a palindrome
    """
    # Note that s[~i] for i in [0,len(s)-1] is s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s)//2))


def int_to_string(x):
    """
    6.1 A: int_to_string
    :param x:
    :return:
    """

    is_negative = False
    # If the input is negative, we take a note of it, and flip the sign
    if x < 0:
        x,is_negative = -x, True

    s = []
    while True:
        # why ord('0')?
        s.append(chr(ord('0') + x%10))
        x //=10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))

# def string_to_int(s):


def string_to_int_pythonic(s):
    """
    6.1B
    :param s:
    :return:
    """
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
                            s[s[0] == '-':],0) * (-1 if s[0] == '-' else 1)



def convert_base(num_as_string,b1,b2):
    """
    6.1b
    :param num_as_string:
    :param b1:
    :param b2:
    :return:
    """
    def construct_from_base(num_as_int,base):
        return ('' if num_as_int == 0 else construct_from_base(num_as_int//base, base)
                + string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'

    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
    num_as_string[is_negative:], 0)

    return ('-' if is_negative else '') + ('0' if num_as_int == 0
                                           else construct_from_base(num_as_int,b2))



def my_ss_decode_col_id(col):
    """
    A "non-pythonic" version of ss decode for my own understanding of how lambda and
    reduce works in python
    :param col:
    :return:
    """
    sumval = 0
    for e in col:
        sumval = sumval * 26 + ord(e) - ord("A") + 1
    return sumval
    # return functools.reduce(
    #     lambda result,c: result * 26 + ord(c) - ord("A") + 1, col, 0
    # )


def replace_and_remove(size,s):
    """
    6.4
    :param size:
    :param s:
    :return:
    """
    write_idx, a_count = 0,0

    # Forward pass
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx +=1
        if s[i] == 'a':
            a_count +=1


    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1

    # backwards pass
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -=2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1

    return final_size


def is_palindrome_sentence(s):
    """
    6.5

    A classic case of two pointer (start and end) manipulation
    :param s:
    :return:
    """
    i, j = 0, len(s)-1

    while i < j:
        while not s[i].isalnum() and i < j:
            i +=1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i+=1
        j-=1

    return True


def reverse_words(s):

    s.reverse()

    def reverse_range(s,start,end):
        while start < end:
            s[start],s[end] = s[end],s[start]
            start,end = start+1, end-1

    start = 0

    while True:
        end = s.find(b' ', start)
        if end < 0:
            break

        reverse_range(s,start,end-1)
        start = end+1

    reverse_range(s,start,len(s)-1)



# test cases, move these to a test file later
# int_to_string(-56089)
# int_to_string("-56789")


a = my_ss_decode_col_id("AB")
my_ss_decode_col_id("ZY")

print(a)

