import os
import re
from pathlib import Path


def delete_borders(logo):
    logo = re.sub("(\n*^\s+\n)|($\n)", "", logo)  # empty lines
    lines = logo.split("\n")
    while 1:
        no_char = False
        for l in lines:
            if l[0] != " ":
                no_char = True
                break
        if no_char:
            break
        else:
            lines = [l[1:] for l in lines]
    logo = "\n".join(lines)
    return logo


def generate_ascii(path, image):
    path_to_image = path + image if image[0] == "/" else image
    path_to_ascii = path + "../ascii_arts/custom.txt"
    os.system(f"python3 img2txt.py --input {path_to_image} --output {path_to_ascii} --mode simple --num_cols 40")
    with open(path_to_ascii) as f:
        logo = f.read()
    count = {}
    for ch in logo:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
    for key in count:
        if count[key] == max(list(count.values())):
            char_to_escape = "$@%8&#*/\|(){}[]?-_+~<>!;:,\"^`'."
            char = "\\" + key if key in char_to_escape else key
            logo = re.sub(char, " ", logo)
            logo = delete_borders(logo)
            print(logo)
            break
    with open(path_to_ascii, "w") as f:
        f.write(logo)

