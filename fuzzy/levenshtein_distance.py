# ref: https://www.datacamp.com/community/tutorials/fuzzy-string-python
import sys

import numpy as np
import logging

format = '%(asctime)s: %(message)s'
# logging.basicConfig(format=format, level=logging.INFO)

log = logging.getLogger('mylog')
log.setLevel(logging.INFO)

stream = logging.StreamHandler()
stream.setLevel(level=logging.INFO)
stream.setFormatter(logging.Formatter(format))
log.addHandler(stream)


def levenshtein_ratio_and_distance(s: str, t: str, ratio_cal: bool=False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s) + 1
    cols = len(t) + 1
    distance = np.zeros((rows, cols), dtype=int)  # Create 2D matrix fill up with zeros

    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i  # Label on columns
            distance[0][k] = k  # Label on rows

    # log.info(f'Distance:\n {distance}')

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                if ratio_cal:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row - 1][col] + 1,  # cost of deletions
                                     distance[row][col - 1] + 1,  # cost of insertions
                                     distance[row - 1][col - 1] + cost)  # cost of substituions

    log.info(f'Final Distance: \n{distance}')
    if ratio_cal:
        return (len(s) + len(t) - distance[row][col]) / (len(s) + len(t))

    return f"The String are {distance[row][col]} edit away"


if __name__ == '__main__':
    str1 = "Apple Inc."
    str2 = "apple Inc"
    log.info(f'str1: {str1}, str2: {str2}')
    Distance = levenshtein_ratio_and_distance(str1, str2)
    log.info(f'distance: {Distance}')
    Ratio = levenshtein_ratio_and_distance(str1, str2, ratio_cal=True)
    log.info(f'ratio: {Ratio}')
