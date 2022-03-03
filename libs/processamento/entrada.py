from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel



class Entrada(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        box_central = MDBoxLayout(orientation='vertical')
        # elementos de entrada reativo
        entrada = MDTextField(multiline=True,
                              hint_text='Como você está se sentindo?',
                              size_hint=(.9,.5),
                              pos_hint={'center_x':.5,'center_y':.5})
        entrada.bind(text=self.reescrever)
        resposta = MDLabel(text='Olá, talvez eu possa lhe ajudar',
                           halign= "center",
                           size_hint=(.9,.5),
                           pos_hint={'center_x':.5,'center_y':.5})

        # composicao
        box_central.add_widget(entrada)
        box_central.add_widget(resposta)
        self.add_widget(box_central)
        return self

    def reescrever(self, *args):
        print(args)