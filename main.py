import re

import pyperclip


def convert(latexstring: str):
    matrixregex = re.compile(r"(\\begin\{pmatrix\}.*?\\end\{pmatrix\})")
    # clean input
    latexstring = latexstring.strip(".").strip(" ")
    results = []
    for expression in matrixregex.split(latexstring):
        result = expression
        if matrixregex.match(expression):
            result = result.replace("\\begin{pmatrix}", "{(")
            result = result.replace("\\end{pmatrix}", ")}")
            result = result.replace("&", ",")
            result = result.replace("\\\\", "),(")
        if not len(result) == 0:
            results.append(result)
    latexstring = '\n'.join(results)
    return latexstring


if __name__ == '__main__':
    print("Usage:\n"
          "\t- copy paste the latex code you want to wolfram-alpha-iphy in the input\n"
          "\t- the result will be copied into the clipboard.\n"
          "\t- Nested pmatrix tags(a \\begin{pmatrix} tag instide one) will cause parsing problems. Dont do that.\n"
          "\t- type q to quit")
    while True:
        inp = input("\ninput >")
        if inp == "q":
            print("Thank you for choosing Wolfram Conversion Services")
            break
        tmp = convert(inp)
        if len(tmp.replace("\n", "")) < 0:
            pyperclip.copy(tmp.replace("\n", ""))
        print(tmp)
