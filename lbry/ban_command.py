def checks(codeblock=None):
    if codeblock is not None:
        answer = "Correct"
    else:
        answer = "Missing Reason"
    return answer

def reason(codeblockin, reasonin = None):
    sentence = ' '.join(reasonin)
    final = str(codeblockin + " " + sentence)
    return final
