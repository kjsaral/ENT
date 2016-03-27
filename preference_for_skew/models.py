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
    name_in_url = 'preference_for_skew'
    players_per_group = None
    num_rounds = 1
    pie_data = [10, 40, 50]
    pie_conf = {
        "data": pie_data,
        "labels": ["{}%".format(d) for d in pie_data],
        "title": "Please Choose your most preferred gamble",
        "colors": ['#EE9095', '#90EE90', '#AB90EE']
    }
    skew_choices = ["A", "B", "C", "D", "E", "F"]

    skewchoices1 = {
        'A': [1.0, 1.0, 1.0],
        'B': [0.6, 1.8, 1.8],
        'C': [0.2, 2.6, 2.6],
        'D': [-0.2, 3.4, 3.4],
        'E': [-0.6, 4.2, 4.2],
        'F': [-1.2, 4.8, 4.8]
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    skewchoice1 = models.CharField(max_length=50, choices=sorted(Constants.skewchoices1), widget=widgets.RadioSelectHorizontal())
    skewchoice2 = models.CharField(max_length=50, choices=Constants.skew_choices, widget=widgets.RadioSelectHorizontal())
    skewchoice3 = models.CharField(max_length=50, choices=Constants.skew_choices, widget=widgets.RadioSelectHorizontal())