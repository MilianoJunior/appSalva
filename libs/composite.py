from libs.processamento.entrada import Entrada
from libs.menus.menus import Menus

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.button import Button

class Composite():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __call__(self):
        try:
            box_central= MDFloatLayout()
            box_menu = MDBoxLayout(orientation='vertical',
                                   size_hint=(1,.1),
                                   pos_hint={'x':0,'y':.9})
            box_screens = MDBoxLayout(orientation='vertical',
                                      size_hint=(1,.9),
                                      pos_hint={'x':0,'y':0})
            # componentes
            sm = ScreenManager()
            menus = Menus()()
            # Screens
            c1 = Entrada(name='entrada')()

            # composicao screens
            sm.add_widget(c1)
            # composicao
            box_menu.add_widget(menus)
            box_screens.add_widget(sm)
            #-------
            box_central.add_widget(box_menu)
            box_central.add_widget(box_screens)

            return box_central
        except Exception as e:
            raise Exception ('Composite erro: ', e)