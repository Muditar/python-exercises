from sys import exit
from random import randint
from textwrap import dedent
class Scene(objext):

    def enter(self):
        print("this scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
