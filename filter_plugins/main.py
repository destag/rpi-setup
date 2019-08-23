def figlet(string, font="banner"):
    import figfont

    font = figfont.banner
    rows = [""] * font["size"]

    for c in string.lower():
        letter = font.get(c)
        for i, row in enumerate(letter):
            rows[i] += row

    return "\n".join(rows)


class FilterModule:
    def filters(self):
        return {
            "figlet": figlet,
        }
