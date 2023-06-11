from io_utils import read_possible_base_60, read_60_to_decimal_conversions
import numpy as np


def base_sixty_to_base_ten(base_sixty_num, conversion_dict):
    """Converts base-sixty number to a regular decimal
    number.
    """
    total = 0
    for i in range(1, len(base_sixty_num) + 1):
        base_sixty_digit = base_sixty_num[-i]
        decimal_digit = conversion_dict[base_sixty_digit]
        val = decimal_digit * 60 ** (i - 1)
        total = total + val
    return total


def get_base_10_representation():
    """Returns the square of numbers
    on pages 49-50 of the Liber Primus
    as decimal numbers in a numpy array.
    Assumes the originals are base 60.
    """
    input_df = read_possible_base_60()
    (
        conversion_dict,
        base_10_representation_to_base_60_digits,
    ) = read_60_to_decimal_conversions()
    as_matrix = input_df.iloc[:, 0:8].values
    new_matrix = np.zeros(as_matrix.shape)
    for i, row in enumerate(as_matrix):
        for j, item in enumerate(row):
            converted = base_sixty_to_base_ten(item, conversion_dict)
            new_matrix[i, j] = converted
    return as_matrix, new_matrix
