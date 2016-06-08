# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'eyes_mind'
    players_per_group = None

    example = {'answer': 1, 'options': [u'jealous', u'panicked', u'arrogant', u'hateful'], 'fname': u'eyes-example.jpg'}

    questions = [
        {'answer': 0, 'options': [u'playful',u'comforting',u'irritated',u'bored'], 'fname': u'eyes-001.jpg'},
        {'answer': 1, 'options': [u'terrified',u'upset',u'arrogant',u'annoyed'], 'fname': u'eyes-002.jpg'},
        {'answer': 2, 'options': [u'joking',u'flustered',u'desire',u'convinced'], 'fname': u'eyes-003.jpg'},
        {'answer': 1, 'options': [u'joking',u'insisting',u'amused',u'relaxed'], 'fname': u'eyes-004.jpg'},
        {'answer': 2, 'options': [u'irritated',u'sarcastic',u'worried',u'friendly'], 'fname': u'eyes-005.jpg'},
        {'answer': 1, 'options': [u'aghast',u'fantasizing',u'impatient',u'alarmed'], 'fname': u'eyes-006.jpg'},
        {'answer': 2, 'options': [u'apologetic',u'friendly',u'uneasy',u'dispirited'], 'fname': u'eyes-007.jpg'},
        {'answer': 0, 'options': [u'despondent',u'relieved',u'shy',u'excited'], 'fname': u'eyes-008.jpg'},
        {'answer': 3, 'options': [u'annoyed',u'hostile',u'horrified',u'preoccupied'], 'fname': u'eyes-009.jpg'},
        {'answer': 0, 'options': [u'cautious',u'insisting',u'bored',u'aghast'], 'fname': u'eyes-010.jpg'},
        {'answer': 2, 'options': [u'terrified',u'amused',u'regretful',u'flirtatious'], 'fname': u'eyes-011.jpg'},
        {'answer': 2, 'options': [u'indifferent',u'embarrassed',u'sceptical',u'dispirited'], 'fname': u'eyes-012.jpg'},
        {'answer': 1, 'options': [u'decisive',u'anticipating',u'threatening',u'shy'], 'fname': u'eyes-013.jpg'},
        {'answer': 3, 'options': [u'irritated',u'disappointed',u'depressed',u'accusing'], 'fname': u'eyes-014.jpg'},
        {'answer': 0, 'options': [u'contemplative',u' flustered ',u'encouraging',u' amused'], 'fname': u'eyes-015.jpg'},
        {'answer': 1, 'options': [u'irritated',u'thoughtful',u'encouraging',u'sympathetic'], 'fname': u'eyes-016.jpg'},
        {'answer': 0, 'options': [u'doubtful',u'affectionate',u'playful',u'aghast'], 'fname': u'eyes-017.jpg'},
        {'answer': 0, 'options': [u'decisive',u'amused',u'aghast',u'bored'], 'fname': u'eyes-018.jpg'},
        {'answer': 3, 'options': [u'arrogant',u'grateful',u'sarcastic',u'tentative'], 'fname': u'eyes-019.jpg'},
        {'answer': 1, 'options': [u'dominant',u'friendly',u'guilty',u'horrified'], 'fname': u'eyes-020.jpg'},
        {'answer': 1, 'options': [u'embarrassed',u'fantasizing',u'confused',u'panicked'], 'fname': u'eyes-021.jpg'},
        {'answer': 0, 'options': [u'preoccupied',u'grateful',u'insisting',u'imploring'], 'fname': u'eyes-022.jpg'},
        {'answer': 2, 'options': [u'contented',u'apologetic',u'defiant',u'curious'], 'fname': u'eyes-023.jpg'},
        {'answer': 0, 'options': [u'pensive',u'irritated',u'excited',u'hostile'], 'fname': u'eyes-024.jpg'},
        {'answer': 3, 'options': [u'panicked',u'incredulous',u'despondent',u'interested'], 'fname': u'eyes-025.jpg'},
        {'answer': 2, 'options': [u'alarmed',u'shy',u'hostile',u'anxious'], 'fname': u'eyes-026.jpg'},
        {'answer': 1, 'options': [u'joking',u'cautious',u'arrogant',u'reassuring'], 'fname': u'eyes-027.jpg'},
        {'answer': 0, 'options': [u'interested',u'joking',u'affectionate',u'contented'], 'fname': u'eyes-028.jpg'},
        {'answer': 3, 'options': [u'impatient',u'aghast',u'irritated',u'reflective'], 'fname': u'eyes-029.jpg'},
        {'answer': 1, 'options': [u'grateful',u'flirtatious',u'hostile',u'disappointed'], 'fname': u'eyes-030.jpg'},
        {'answer': 1, 'options': [u'ashamed',u'confident',u'joking',u'dispirited'], 'fname': u'eyes-031.jpg'},
        {'answer': 0, 'options': [u'serious',u'ashamed',u'bewildered',u'alarmed'], 'fname': u'eyes-032.jpg'},
        {'answer': 3, 'options': [u'embarrassed',u'guilty',u'fantasizing',u'concerned'], 'fname': u'eyes-033.jpg'},
        {'answer': 2, 'options': [u'aghast',u'baffled',u'distrustful',u'terrified'], 'fname': u'eyes-034.jpg'},
        {'answer': 1, 'options': [u'puzzled',u'nervous',u'insisting',u'contemplative'], 'fname': u'eyes-035.jpg'},
        {'answer': 2, 'options': [u'ashamed',u'nervous',u'suspicious',u'indecisive'], 'fname': u'eyes-036.jpg'}
    ]

    num_rounds = len(questions)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    response_example = models.CharField(max_length=255, choices=Constants.example["options"], widget=widgets.RadioSelectHorizontal())

    response_q1 = models.CharField(max_length=255, choices=Constants.questions[0]["options"], widget=widgets.RadioSelectHorizontal())
    response_q2 = models.CharField(max_length=255, choices=Constants.questions[1]["options"], widget=widgets.RadioSelectHorizontal())
    response_q3 = models.CharField(max_length=255, choices=Constants.questions[2]["options"], widget=widgets.RadioSelectHorizontal())
    response_q4 = models.CharField(max_length=255, choices=Constants.questions[3]["options"], widget=widgets.RadioSelectHorizontal())
    response_q5 = models.CharField(max_length=255, choices=Constants.questions[4]["options"], widget=widgets.RadioSelectHorizontal())
    response_q6 = models.CharField(max_length=255, choices=Constants.questions[5]["options"], widget=widgets.RadioSelectHorizontal())
    response_q7 = models.CharField(max_length=255, choices=Constants.questions[6]["options"], widget=widgets.RadioSelectHorizontal())
    response_q8 = models.CharField(max_length=255, choices=Constants.questions[7]["options"], widget=widgets.RadioSelectHorizontal())
    response_q9 = models.CharField(max_length=255, choices=Constants.questions[8]["options"], widget=widgets.RadioSelectHorizontal())
    response_q10 = models.CharField(max_length=255, choices=Constants.questions[9]["options"], widget=widgets.RadioSelectHorizontal())
    response_q11 = models.CharField(max_length=255, choices=Constants.questions[10]["options"], widget=widgets.RadioSelectHorizontal())
    response_q12 = models.CharField(max_length=255, choices=Constants.questions[11]["options"], widget=widgets.RadioSelectHorizontal())
    response_q13 = models.CharField(max_length=255, choices=Constants.questions[12]["options"], widget=widgets.RadioSelectHorizontal())
    response_q14 = models.CharField(max_length=255, choices=Constants.questions[13]["options"], widget=widgets.RadioSelectHorizontal())
    response_q15 = models.CharField(max_length=255, choices=Constants.questions[14]["options"], widget=widgets.RadioSelectHorizontal())
    response_q16 = models.CharField(max_length=255, choices=Constants.questions[15]["options"], widget=widgets.RadioSelectHorizontal())
    response_q17 = models.CharField(max_length=255, choices=Constants.questions[16]["options"], widget=widgets.RadioSelectHorizontal())
    response_q18 = models.CharField(max_length=255, choices=Constants.questions[17]["options"], widget=widgets.RadioSelectHorizontal())
    response_q19 = models.CharField(max_length=255, choices=Constants.questions[18]["options"], widget=widgets.RadioSelectHorizontal())
    response_q20 = models.CharField(max_length=255, choices=Constants.questions[19]["options"], widget=widgets.RadioSelectHorizontal())
    response_q21 = models.CharField(max_length=255, choices=Constants.questions[20]["options"], widget=widgets.RadioSelectHorizontal())
    response_q22 = models.CharField(max_length=255, choices=Constants.questions[21]["options"], widget=widgets.RadioSelectHorizontal())
    response_q23 = models.CharField(max_length=255, choices=Constants.questions[22]["options"], widget=widgets.RadioSelectHorizontal())
    response_q24 = models.CharField(max_length=255, choices=Constants.questions[23]["options"], widget=widgets.RadioSelectHorizontal())
    response_q25 = models.CharField(max_length=255, choices=Constants.questions[24]["options"], widget=widgets.RadioSelectHorizontal())
    response_q26 = models.CharField(max_length=255, choices=Constants.questions[25]["options"], widget=widgets.RadioSelectHorizontal())
    response_q27 = models.CharField(max_length=255, choices=Constants.questions[26]["options"], widget=widgets.RadioSelectHorizontal())
    response_q28 = models.CharField(max_length=255, choices=Constants.questions[27]["options"], widget=widgets.RadioSelectHorizontal())
    response_q29 = models.CharField(max_length=255, choices=Constants.questions[28]["options"], widget=widgets.RadioSelectHorizontal())
    response_q30 = models.CharField(max_length=255, choices=Constants.questions[29]["options"], widget=widgets.RadioSelectHorizontal())
    response_q31 = models.CharField(max_length=255, choices=Constants.questions[30]["options"], widget=widgets.RadioSelectHorizontal())
    response_q32 = models.CharField(max_length=255, choices=Constants.questions[31]["options"], widget=widgets.RadioSelectHorizontal())
    response_q33 = models.CharField(max_length=255, choices=Constants.questions[32]["options"], widget=widgets.RadioSelectHorizontal())
    response_q34 = models.CharField(max_length=255, choices=Constants.questions[33]["options"], widget=widgets.RadioSelectHorizontal())
    response_q35 = models.CharField(max_length=255, choices=Constants.questions[34]["options"], widget=widgets.RadioSelectHorizontal())
    response_q36 = models.CharField(max_length=255, choices=Constants.questions[35]["options"], widget=widgets.RadioSelectHorizontal())


