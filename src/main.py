#!/bin/python3

import configparser
from pathlib import Path

from terminal import get_args
from generate_ascii import generate_ascii


path = str(Path(__file__).parent) + "/"
config = configparser.ConfigParser()
config.read(path + "/config.ini")
config_dict = {section: {key: config[section][key] for key in config[section]} for section in config}


def create_md(text):
    style = config_dict["base"]["style"]
    md_text = f"```{style}\n$ ghfetch\n{text}\n```"
    with open("README.md", "w+") as f:
        f.write(md_text)


def format_text(ascii_art):
    lines = ascii_art.split("\n")
    index = 0
    for section in config_dict:
        if section == "DEFAULT" or section == "base":
            continue
        if section == "infos":
            first_line = config_dict["base"]["hostname"] + "@" + config_dict["base"]["country"]
            lines[index] += first_line
            lines[index + 1] += "-" * len(first_line)
        else:
            lines[index] += section.title()
            lines[index + 1] += "-" * len(section)
        index += 2
        for key in config_dict[section]:
            if key == "age":
                lines[index] += "Uptime: \"" + config_dict[section][key] + " years\""
            elif key == "os":
                lines[index] += key + ": \"" + config_dict[section][key] + "\""
            else:
                lines[index] += key.title() + ": \"" + config_dict[section][key] + "\""
            index += 1
        index += 1
    return "\n".join(lines)


def add_spacing(ascii_art):
    lines = ascii_art.split("\n")
    longest_line = len(max(lines))
    for i in range(len(lines)):
        lines[i] += " " * (longest_line - len(lines[i]))
        lines[i] += "  "
    return "\n".join(lines)


def main(opt):
    ascii_art_path = path + "../ascii_arts/" + opt.logo + ".txt"
    with open(ascii_art_path) as f:
        ascii_art = f.read()
    ascii_art = add_spacing(ascii_art)
    text = format_text(ascii_art)
    create_md(text)
    print(text)


if __name__ == "__main__":
    opt = get_args()
    if opt.generate_ascii:
        generate_ascii(path, opt.generate_ascii)
    else:
        main(opt)
