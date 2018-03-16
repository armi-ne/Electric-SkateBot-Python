# For Battery


def batterycheck(series=None, parallel=None, amphour=None, codeblock=None):
    # No values
    if series == parallel == amphour is None:
        answer = "NoValues"
    # For Input Type
    elif not ((series.isnumeric() or series.replace('.', '', 1).isnumeric()) and (parallel.isnumeric() or parallel.replace('.', '', 1).isnumeric()) and (amphour.isnumeric() or amphour.replace('.', '', 1).isnumeric())):
        answer = "TypeError"
    # Series and Parallel Whole Numbers
    elif (series.isnumeric() and parallel.isnumeric()) is False:
        answer = "NoDecimals"
    # For Correct Input
    elif all((series, parallel, amphour)) and ((float(series) < 100.0 and float(parallel) < 100.0 and float(amphour) <= 100.0) is True) and codeblock is None:
        answer = "Correct"
    # For too many Values
    elif codeblock is not None:
        answer = "TooMany"
    # Values too high
    elif ((float(series) < 100.0 and float(parallel) < 100.0 and float(amphour) <= 100.0) is False):
        answer = "ValuesTooHigh"
    return answer

# For Convert


def convertercheck(inputval=None, inputuni=None, to_text=None, desireduni=None, codeblock=None):
    if (inputval is None) or (inputuni is None) or (to_text is None) or (desireduni is None):
        answer = "NoInput"
    # For Input Type
    elif ((inputval.isnumeric() or inputval.replace('.', '', 1).isdigit()) is False) or ((inputuni.isnumeric() or inputuni.replace('.', '', 1).isdigit()) is not False) or ((to_text.isnumeric() or to_text.replace('.', '', 1).isdigit()) is not False) or ((desireduni.isnumeric() or desireduni.replace('.', '', 1).isdigit()) is not False):
        answer = "TypeError"
    # For Correct Input
    elif all((inputval, inputuni, to_text, desireduni)) and codeblock is None:
        answer = "Correct"
    # For too many Values
    elif codeblock is not None:
        answer = "TooMany"
    return answer
