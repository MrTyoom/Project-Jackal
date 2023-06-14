from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

import spacy
import nltk
nltk.download("stopwords")
#--------#


#Create lemmatizer and stopwords list
mystem = Mystem()
russian_stopwords = stopwords.words("russian")


def test_model(model, text):
    doc = nlp(text)
    results = []
    entities = []
    for ent in doc.ents:
        entities.append((ent.start_char, ent.end_char, ent.label_))
    if len(entities) > 0:
        results = [text, {"entities": entities}]  # специальный формат для spaCy
        return (results)


# Preprocess function
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]

    text = " ".join(tokens)

    return text


def input_for_gui(test):
    arrow = ['стрелка', 'указатель']
    balloon = ['воздушный шар', 'шар']
    barrel = ['бочка']
    cannibal = ['людоед']
    castle = ['крепость']
    castle_girl = ["девушка", "абориген", "аборигенка"]
    croc = ['крокодил']
    gold = ['сундук', 'деньги', 'сокровища', "золотишко", "монета", "золото", "деньга", "монетка",
            "клад", "сундучок", "мелочь", "сокровище", "сокровищница"]
    horse = ['конь', 'лошадь']
    ice = ['лед', 'лёд']
    labyrinth = ['лабиринт', 'джунгли', 'пустыня', 'болото',
                 'горы', "тропик", "пустынь", "заросль", "гора", "скала", "лес",
                 "песок", "дюна", "тропический", "леса"]
    plane = ['самолет', "самолёт"]
    trap = ['капкан', 'ловушка']
    cannon = ['пушка']
    field = ['поляна', 'пустышка', "клетка",
             "клеточка", "холм"]

    #     test = 'первым пиратом пойду налево и попаду на шар'
    test = preprocess_text(test)
    nlp = spacy.load("jackal_ner_trained_model")  # сущности определяются посредством обучения модели
    doc = nlp(test)
    #     results = test_model(nlp, command)
    dict_ = {}
    for ent in doc.ents:
        dict_[ent.label_] = ent.text
    #         print (ent.text, ent.label_)
    print(dict_)

    if "NUM" in dict_.keys():
        if "пер" in dict_["NUM"]:
            number = 1
        elif "втор" in dict_["NUM"]:
            number = 2
        elif "тр" in dict_["NUM"]:
            number = 3
    else:
        number = 101

    if "DIR" in dict_.keys():
        if "лев" in dict_["DIR"]:
            direction = 0
        elif "прав" in dict_["DIR"]:
            direction = 1
        elif "прям" in dict_["DIR"]:
            direction = 2
        elif "наз" in dict_["DIR"]:
            direction = 3

        return number, direction
    #             break

    elif "DIR" not in dict_.keys() and "TILE" in dict_.keys():
        if dict_["TILE"] in arrow:
            tile = 1
        elif dict_["TILE"] in balloon:
            tile = 8
        elif dict_["TILE"] in barrel:
            tile = 9
        elif dict_["TILE"] in cannibal:
            tile = 10
        elif dict_["TILE"] in castle:
            tile = 11
        elif dict_["TILE"] in castle_girl:
            tile = 12
        elif dict_["TILE"] in croc:
            tile = 13
        elif dict_["TILE"] in gold:
            tile = 14
        elif dict_["TILE"] in horse:
            tile = 19
        elif dict_["TILE"] in ice:
            tile = 20
        elif dict_["TILE"] in labyrinth:
            tile = 21
        elif dict_["TILE"] in field:
            tile = 25
        elif dict_["TILE"] in plane:
            tile = 29
        elif dict_["TILE"] in trap:
            tile = 30
        elif dict_["TILE"] in cannon:
            tile = 31

        return number, tile

    # def test_model(model, text):
#     doc = nlp(text)
#     results = []
#     entities = []
#     for ent in doc.ents:
#         entities.append((ent.start_char, ent.end_char, ent.label_))
#     if len(entities) > 0:
#         results = [text, {"entities": entities}] # специальный формат для spaCy
#         return (results)
#
#
# # Preprocess function
# def preprocess_text(text):
#     tokens = mystem.lemmatize(text.lower())
#     tokens = [token for token in tokens if token not in russian_stopwords \
#               and token != " " \
#               and token.strip() not in punctuation]
#
#     text = " ".join(tokens)
#
#     return text
#
#
# def input_for_gui(test):
#     arrow = ['стрелка', 'указатель']
#     balloon = ['воздушный шар', 'шар']
#     barrel = ['бочка']
#     cannibal = ['людоед']
#     castle = ['крепость']
#     castle_girl = ["девушка", "абориген", "аборигенка"]
#     croc = ['крокодил']
#     gold = ['сундук', 'деньги', 'сокровища', "золотишко", "монета", "золото", "деньга", "монетка",
#             "клад", "сундучок", "мелочь", "сокровище", "сокровищница"]
#     horse = ['конь', 'лошадь']
#     ice = ['лед', 'лёд']
#     labyrinth = ['лабиринт', 'джунгли', 'пустыня', 'болото',
#                  'горы', "тропик", "пустынь", "заросль", "гора", "скала", "лес",
#                  "песок", "дюна", "тропический", "леса"]
#     plane = ['самолет', "самолёт"]
#     trap = ['капкан', 'ловушка']
#     cannon = ['пушка']
#     field = ['поляна', 'пустышка', "клетка",
#              "клеточка", "холм"]
#
#     #     test = 'первым пиратом пойду налево и попаду на шар'
#     test = preprocess_text(test)
#     nlp = spacy.load("jackal_ner_all_entities")  # сущности определяются посредством обучения модели
#
#     doc = nlp(test)
#     dict_ = {}
#     for ent in doc.ents:
#         dict_[ent.label_] = ent.text
#     # print(dict_)
#
#     number = 0
#     if "NUM" in dict_.keys():
#         if "пер" in dict_["NUM"]:
#             number = 0
#         elif "втор" in dict_["NUM"]:
#             number = 1
#         elif "тр" in dict_["NUM"]:
#             number = 2
#     else:
#         number = 101
#     print(number)
#     if "DIR" in dict_.keys() and number != 101:
#
#         if "лев" in dict_["DIR"]:
#             direction = 0
#         elif "прав" in dict_["DIR"]:
#             direction = 1
#         elif "прям" in dict_["DIR"]:
#             direction = 2
#             print(1)
#         elif "наз" in dict_["DIR"]:
#             direction = 3
#         return (number, direction)
#
#     elif "DIR" in dict_.keys() and number == 101:
#         if "лев" in dict_["DIR"]:
#             direction = 0
#         elif "прав" in dict_["DIR"]:
#             direction = 1
#         return (number, direction)
#
#     elif "DIR" not in dict_.keys() and "TILE" in dict_.keys():
#         if dict_["TILE"] in arrow:
#             tile = 1
#         elif dict_["TILE"] in balloon:
#             tile = 8
#         elif dict_["TILE"] in barrel:
#             tile = 9
#         elif dict_["TILE"] in cannibal:
#             tile = 10
#         elif dict_["TILE"] in castle:
#             tile = 11
#         elif dict_["TILE"] in castle_girl:
#             tile = 12
#         elif dict_["TILE"] in croc:
#             tile = 13
#         elif dict_["TILE"] in gold:
#             tile = 14
#         elif dict_["TILE"] in horse:
#             tile = 19
#         elif dict_["TILE"] in ice:
#             tile = 20
#         elif dict_["TILE"] in labyrinth:
#             tile = 21
#         elif dict_["TILE"] in field:
#             tile = 25
#         elif dict_["TILE"] in plane:
#             tile = 29
#         elif dict_["TILE"] in trap:
#             tile = 30
#         elif dict_["TILE"] in cannon:
#             tile = 31
#
#         return (number, tile, -1)
