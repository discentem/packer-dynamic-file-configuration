import os
import sys
import yaml
import difflib
from colorama import Fore, Back, Style, init
from jinja2 import FileSystemLoader, Environment

def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

def color_diff(diff):
    diff_string = []
    for line in diff:
        if line.startswith('+'):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith('-'):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith('^'):
            yield Fore.BLUE + line + Fore.RESET
        else:
            yield line

        diff_string += line

    return diff


def diff_autounattend(autounattendFile, newAutounattendString):
    autounattendFile = autounattendFile.read().splitlines()
    newAutounattendString = newAutounattendString.splitlines()

    diff = difflib.unified_diff(autounattendFile, newAutounattendString)
    diff = color_diff(diff)
    diff = '\n'.join(diff)

    return diff

def main():

    templateFile = sys.argv[1]

    with open('Autounattend.yml', 'r') as au:
        data = yaml.load(au)
    newAutounattendString = render_from_template(os.path.dirname(templateFile),
                                               'Autounattend.xml.j2',
                                               **data)

    autounattendFile = open(templateFile.strip('.j2'), 'r')
    diff = diff_autounattend(autounattendFile, newAutounattendString)

    autounattendFile = open(templateFile.strip('.j2'), 'w+')
    autounattendFile.write(newAutounattendString)
    autounattendFile.close()

    print(diff)


main()
