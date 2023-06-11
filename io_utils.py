import pandas as pd


def read_possible_base_60():
    """Reads the square of symbols on pages 49-51
    of the Liber Primus. Returns a dataframe with
    the symbols stored as strings and a final column
    indicated whether they appear on the first, second,
    or third page.
    """
    input_df = pd.read_csv("input.csv", header=None)
    return input_df


def read_60_to_decimal_conversions():
    """Reads in a file containing base 60 symbols and
    corresponding decimal values. Outputs a dictionary
    with symbols as keys and decimal values as values.
    Also outputs an array with decimals values as indices and
    array elements as symbols."""
    conversions = pd.read_csv("sixty_to_decimal.tsv", sep="\t")
    base_60_digits_to_base_10_representation = dict(
        zip(conversions["base_60"], conversions["decimal"])
    )
    # return as array
    base_10_representation_to_base_60_digits = conversions["base_60"].values
    return (
        base_60_digits_to_base_10_representation,
        base_10_representation_to_base_60_digits,
    )
