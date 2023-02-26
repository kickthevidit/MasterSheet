
def generate_prompt(text):
    return """
    Thoroughly explain the text below, going in depth on specific details.
    Text:
    ###
    {} 
    ###
    \n
    """.format(text)
