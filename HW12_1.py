import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text = ""
    inside_tag = False

    for ch in html:
        if ch == "<":
            inside_tag = True
        elif ch == ">":
            inside_tag = False
        elif not inside_tag:
            text += ch

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write("\n".join(lines))
