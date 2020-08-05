import re

import pyperclip


def convert(latexstring: str):
    matrix_regex = re.compile(r"(\\begin{pmatrix}.*?\\end{pmatrix})")
    # clean input
    latexstring = latexstring.strip(".").strip(" ")
    latexstring = re.sub(r"(\\+ *\\+end{pmatrix})", r"\\end{pmatrix}", latexstring)  # remove useless \\ \end{ptable}
    results = []
    for expression in matrix_regex.split(latexstring):
        result = expression
        if matrix_regex.match(expression):
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
        if len(tmp.replace("\n", "")) > 0:
            pyperclip.copy(tmp.replace("\n", ""))
        print(tmp)
