from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField



class Entrada(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        box_central = MDBoxLayout(orientation='vertical')
        # elementos
        entrada = MDTextField(multiline=True,
                              hint_text='Texto')

        # composicao
        box_central.add_widget(Button(text='salva'))
        self.add_widget(box_central)
        return self