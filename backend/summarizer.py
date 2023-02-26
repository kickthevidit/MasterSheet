
def generate_prompt(text):
    return """
    Summarize the text below as a bullet point list of the most important points.
    Text:
    ###
    {} 
    ###
    \n
    """.format(text)