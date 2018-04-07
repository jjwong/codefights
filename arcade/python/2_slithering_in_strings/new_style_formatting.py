def newStyleFormatting(s):
    # The first thing you need to do is to clear duplicates, so we
    # assign a temporary variable to %%
    first_pass = re.sub('%%', '{%}', s)

    # Then we convert %character to {}
    second_pass = re.sub('%\w', '{}', first_pass)

    # Finally we clean up our temporary variables by replacing it back with %
    return re.sub('{%}', '%', second_pass)

    # If you are struggling with test 3, its because we need a temporary
    # variable as denoted in the first_pass