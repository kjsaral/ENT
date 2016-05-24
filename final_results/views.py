# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


class Results_task1(Page):

    def vars_for_template(self):
        option, option_desc, decision = self.player.get_decision()
        return {"option": option, "option_desc": option_desc, "decision": decision}

class Results_task2(Page):

    def vars_for_template(self):
        sp, choice, loteries, wrange, initial_payoff = self.player.get_selected_puzzle()
        return {
            "selected_puzzle": sp, "choice": choice,
            "graphs": {k: graph.render_unknow("?", *map(c, v)) for k, v in loteries.items()},
            "lotery": loteries[choice],
            "wrange": wrange, "initial_payoff": initial_payoff}

class Results_task3(Page):

    def vars_for_template(self):
        squares = graph.render_squares(Constants.pie_conf["colors"])
        snum, soption, choices = self.player.selected_skew()
        return {
            "snum": snum, "soption": soption,
            "landed": squares[self.player.winning_choice],
            "choices": list(zip(squares, choices))}

class final_payoff(Page):
    pass



page_sequence = [Results_task1, Results_task2, Results_task3, final_payoff]
