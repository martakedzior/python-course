def get_prize(points):
    result = []
    if points <= 50:
        result.append("Rabbit!")
    elif points <= 150:
        result.append("Oh dear, no prize this time.")
    elif points <= 180:
        result.append("Ballons")
    else:
        result.append("Ping-pong table")

    return result

print(get_prize(176))


def html(items):
    html_str = "<ul>\n"

    for item in items:
        html_str += "<li>{}</li>\n".format(item)
    html_str += "</ul>"

    return html_str


html(10)