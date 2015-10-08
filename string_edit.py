import numpy as np

def difference(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    forward_metrix = np.zeros(shape=(len1+1, len2+1))
    backward_metrix = np.zeros(shape=(len1+1, len2+1))

    test  = np.zeros(shape=(len1+1, len2+1))
    row = len1
    column = len2
    while row >= 0:
        while column >= 0:
            test[row, column] = None
            column -= 1
        row -= 1
        column = len2

    i = 0
    while i <= len1:
        forward_metrix[i, 0] = i
        i += 1
    i = 0
    while i <= len2:
        forward_metrix[0, i] = i
        i += 1


    i = 1
    j = 1
    while i <= len1:
        while j <= len2:
            if str1[i-1] == str2[j-1]:
                forward_metrix[i, j] = forward_metrix[i-1, j-1]

            else:
                forward_metrix[i, j] = min(forward_metrix[i-1, j-1] + 1, forward_metrix[i-1, j] + 1, forward_metrix[i, j-1] + 1)

            j += 1
        i += 1
        j = 1

    i = len1
    j = len2
    backward_metrix[i, j] = forward_metrix[i, j]
    test[i, j] = forward_metrix[i, j]

    while i >= 1 and j >= 1:
        if str1[i-1] == str2[j-1]:
            backward_metrix[i-1, j-1] = forward_metrix[i-1, j-1]
            test[i-1, j-1] = forward_metrix[i-1, j-1]
            i -= 1
            j -= 1

        else:
            if forward_metrix[i-1, j-1] == min(forward_metrix[i-1, j-1], forward_metrix[i-1, j], forward_metrix[i, j-1]):
                backward_metrix[i-1, j-1] = forward_metrix[i-1, j-1]
                test[i-1, j-1] = forward_metrix[i-1, j-1]
                i -= 1
                j -= 1

            if forward_metrix[i-1, j] == min(forward_metrix[i-1, j-1], forward_metrix[i-1, j], forward_metrix[i, j-1]) and \
                   forward_metrix[i-1, j-1] != min(forward_metrix[i-1, j-1], forward_metrix[i-1, j], forward_metrix[i, j-1]):

                backward_metrix[i-1, j] = forward_metrix[i-1, j]
                test[i-1, j] = forward_metrix[i-1, j]
                i -= 1
                j = j

            if forward_metrix[i, j-1] == min(forward_metrix[i-1, j-1], forward_metrix[i-1, j], forward_metrix[i, j-1]) and\
                    forward_metrix[i-1, j-1] != min(forward_metrix[i-1, j-1], forward_metrix[i-1, j], forward_metrix[i, j-1]) and\
                    forward_metrix[i-1, j] != min(forward_metrix[i-1, j-1], forward_metrix[i-1, j], forward_metrix[i, j-1]):

                backward_metrix[i, j-1] = forward_metrix[i, j-1]
                test[i, j-1] = forward_metrix[i, j-1]
                i = i
                j -= 1
    print("forward metrix")
    print(forward_metrix)
    print("backward_metrix")
    print(test)
    return forward_metrix[len1, len2]

print("difference between azced and abcdef")
print("minimum distance between azced and abcdef is = {}".format(difference("azced", "abcdef")))

print("difference between sam and samual")
print("minimum distance between sam and samual is = {}".format(difference("sam", "samual")))

print("difference between detroit and lansing")
print("minimum distance between detroit and lansing is = {}".format(difference("detroit", "lansing")))