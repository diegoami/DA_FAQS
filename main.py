import requests
from bs4 import BeautifulSoup
import re
import os
ROOT_PAGE='https://en.chessbase.com'
ROOT_POST_PAGE=ROOT_PAGE+'/post/'
import traceback

import argparse

def get_qas(pageLink, qsel, anssel):
    pgnstrings =[]
    print(pageLink)
    r = requests.get(pageLink)
    soup = BeautifulSoup(r.content)
    if not soup:
        return None

    questions = soup.select(qsel)

    answers = soup.select(anssel)

    return questions, answers

def process_page(page_link, qsel, anssel):

  #  page_link = page_link if ROOT_POST_PAGE in page_link else ROOT_POST_PAGE + page_link
    questions, answers = get_qas(page_link, qsel, anssel)
    queans = zip(questions, answers)
    for quean in queans:
        print(quean)

def retrieve_faqs(fileLink):
    with open(fileLink, "r") as handle:
        lines = handle.readlines()
        for line in lines:
            if (line.startswith('#')):
                continue
            print("Processing %s" % line)
            try:
                file, qsel, anssel = line.strip(",")
                process_page(file, qsel, anssel)
            except:
                print("Could not process page %s " % line.strip())

                traceback.print_exc()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--fileLink')
    parser.add_argument('--debug')
    args = parser.parse_args()

    retrieve_faqs(args.fileLink)