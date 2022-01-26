from __future__ import annotations
from cgitb import text
from dataclasses import dataclass
from math import fabs
import random

@dataclass
class Rank:
    keyword:str
    val:int
    valForCompare: int
@dataclass
class Suit:
    keyword:str
    valForCompare:int
@dataclass
class Card:
    suit: Suit
    rank: Rank
    def __gt__(self, other:Card):
        if self.suit.valForCompare>other.suit.valForCompare:
            return True
        else:
            if self.suit.valForCompare == other.suit.valForCompare:
                return self.rank.valForCompare> other.rank.valForCompare
            else:
                return False
    def get_scrore(self):
        return self.rank.val
    def show_card(self):
        return self.rank.keyword+self.suit.keyword

        

@dataclass
class Set3Card:
    list: list[Card]
    def get_scrore(self):
        sumScore = 0
        for x in self.list:
            sumScore+=x.rank.val
        score = sumScore%10
        if score==0:
            return 10
        else:
            return score
    def check_AAA(self):
        temp = self.list[0].rank
        for x in self.list:
            if x.rank!=temp:
                return 
        print("SAPPPPPPPPPPPPPPPPP")
        return True
    def get_max_card(self):
        tempMax = self.list[0]
        for x in self.list:
            if x>tempMax:
                tempMax = x
        return tempMax
    def __gt__(self, other:Set3Card):
        if self.check_AAA():
            if other.check_AAA():
                scoreA= self.get_scrore()
                scoreB= other.get_scrore()
                if scoreA== scoreB:
                    return self.get_max_card()> other.get_max_card()
                else:
                    return scoreA>scoreB
            else:
                return True
        else:
            if other.check_AAA():
                return False
            else:
                scoreA= self.get_scrore()
                scoreB= other.get_scrore()
                if scoreA== scoreB:
                    return self.get_max_card()> other.get_max_card()
                else:
                    return scoreA>scoreB
    def show_card(self):
        listShowCard=[]
        for x in self.list:
            listShowCard.append(x.show_card()) 
        score = self.get_scrore()
        maxcard = self.get_max_card()
        print(" ".join(listShowCard))
        print(score," điểm")
        print("quân bài lớn nhất ", maxcard.show_card())
        print("-----------------")
@dataclass
class Member:
    id:int
    name:str
    set_card:Set3Card
    def show_card(self):
        print(self.name)
        self.set_card.show_card()


    
@dataclass
class Deck:
    list: list[Card]
    def __init__(self) -> None:
        listSuit=[Suit("♠",1),Suit("♣",2),Suit("♥",3), Suit("♦",4)]
        listRank= [Rank("2",2,2),Rank("3",3,3),Rank("4",4,4),Rank("5",5,5),Rank("6",6,6),Rank("7",7,7),Rank("8",8,8),Rank("9",9,9),Rank("A",1,10)]
        result=[]
        for x in listSuit:
            for y in listRank:
                carditem=Card(x,y)
                result.append(carditem)
        self.list= result
        pass
    def shuffle(self):
        random.shuffle(self.list)
    def pop(self):
        result = self.list[:3]
        for x in result:
            self.list.remove(x)
        return result



deck = Deck()
deck.shuffle()
print(deck)
