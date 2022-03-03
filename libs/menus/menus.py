from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar

class Menus():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        box_central = MDBoxLayout(orientation='vertical')
        # criar componentes
        toolbar = MDToolbar(title='App Salva')
#        navigation = NavegationMenu()()

        #add componentes
        box_central.add_widget(toolbar)
#        box_central.add_widget(navigation)


        return box_central