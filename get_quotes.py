#!/usr/bin/env python
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup

import requests
import re


hh_page = requests.get("https://www.goodreads.com/author/quotes/1113469.Hermann_Hesse")

hh_soup = BeautifulSoup(hh_page.text, 'html.parser')

hh_quotes = hh_soup.find_all("div", class_="quoteText")

new_hh_quotes = []
for i, quote in enumerate(hh_quotes):
    new_hh_quotes.append(hh_quotes[i].find_all(re.compile('(.*) Hermann')))

# Fuck it, web scraping imdb etc. would take for fucking ever.
pw_quotes = [
    "The stars at night are big and bright",
    "I don't have to see it, Dottie. I lived it.",
    "There are a lot of things about me you don't know anything about. Things you wouldn't understand, you couldn't understand. Things you shouldn't understand.",
    "You don't wanna get mixed up with a guy like me. I'm a loner, Dottie. A rebel.",
    "It's like you're trying to unravel a giant cable-knit sweater and someone keeps knitting and knitting and knitting and knitting and knitting and knitting and knitting and knitting and knitting.",
    "Shhhh... I'm listening to reason.",
    "That's my name, don't wear it out.",
    "I brought you guys....FRENCH FRIES!",
    "I meant to do that.",
    "I'm rolling a big doughnut and a snake wearing a vest",
    "Boy, I always thought that was the dumbest law.",
    "Good for you and your father",
    "Because I don't make monkeys, I just train them.",
    "I know you are but what am I?",
    "I wouldn't sell my bike for all the money in the world. Not for a hundred million, billion, trillion dollars!",
]

print new_hh_quotes
