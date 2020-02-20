import fileinput
import os
import sys
import fileinput
from xml.dom import minidom
from bs4 import BeautifulSoup


def changereplaceintext(filename, tobereplaced, replace):
    with open(filename, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(tobereplaced, replace)
    with open(filename, 'w') as file:
        file.write(filedata)


def changereplaceinxmlcontent(filename, tag, tobereplaced, replaced):
    with open(filename, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'xml')
        find_tags = soup.find_all(tag)
        for i in find_tags:
            i.string = i.text.replace(tobereplaced, replaced)

        contents = soup.prettify()
    with open(filename, 'w') as file:
        file.write(contents)


def changereplaceinxmltag(filename, tag, newtag):
    with open(filename, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'xml')
        find_tags = soup.find_all(tag)
    for tags in find_tags:
        tags.replace_with(soup.new_tag(newtag))
    contents = soup.prettify()
    with open(filename, 'w') as file:
        file.write(contents)


def changereplaceinhtmlcontent(filename, tag, tobereplaced, replaced):
    with open(filename, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')
        find_tags = soup.find_all(tag)
        for i in find_tags:
            i.string = i.text.replace(tobereplaced, replaced)

        contents = soup.prettify()
    with open(filename, 'w') as file:
        file.write(contents)


def changereplaceinhtmltag(filename, tag, newtag):
    with open(filename, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')
        find_tags = soup.find_all(tag)
    for tags in find_tags:
        tags.replace_with(soup.new_tag(newtag))
    contents = soup.prettify()
    with open(filename, 'w') as file:
        file.write(contents)


def extractcontentxml(filename, tag):
    with open(filename, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'xml')
        target_tag = soup.find_all(tag)
        for i in (target_tag):
            print(i.contents);


def extractcontenthtml(filename, tag):
    with open(filename, 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')
        target_tag = soup.find_all(tag)
        for i in (target_tag):
            print(i.contents);


def main():
    filename = input("Enter your filename        ")
    print(filename)
    if ".txt" in filename:
        tobereplaced = input("Enter the word to be replaced       ")
        replace = input("Enter the word to replace          ")
        changereplaceintext(filename, tobereplaced, replace)
    elif ".xml" in filename:
        op = input("Do you want to replace 1.A tag 2.Content of tag? 3.Extract Content")
        opt = int(op)
        if (opt == 2):
            tag = input("Enter the tag      ")
            tobereplaced = input("Enter the word to be replaced       ")
            replace = input("Enter the word to replace          ")
            changereplaceinxmlcontent(filename, tag, tobereplaced, replace)
        elif (opt == 1):
            tag = input("Enter the tag              ")
            newtag = input("Enter the replacing tag   ")
            changereplaceinxmltag(filename, tag, newtag)
        else:
            tag = input("Enter The Tag  ")
            extractcontentxml(filename, tag)

    elif ".html" in filename:
        op = input("Do you want to replace 1.A tag 2.Content of tag? 3.Extract Content")
        opt = int(op)
    if (opt == 2):
        tag = input("Enter the tag      ")
        tobereplaced = input("Enter the word to be replaced       ")
        replace = input("Enter the word to replace          ")
        changereplaceinhtmlcontent(filename, tag, tobereplaced, replace)
    elif (opt == 1):
        taghtml = input("Enter the tag              ")
        newtaghtml = input("Enter the replacing tag   ")
        changereplaceinhtmltag(filename, taghtml, newtaghtml)
    else:
        tag = input("Enter The Tag  ")
        extractcontenthtml(filename, tag)


if __name__ == "__main__":
    main()
