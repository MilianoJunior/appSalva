from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
#from kivymd.uix.navigationrail import (MDNavigationRail, MDNavigationRailItem)
#from kivymd.utils import get_color_from_hex

#class NavegationMenu(MDNavigationRail):
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.md_bg_color = get_color_from_hex("#344954")
#        self.color_normal = get_color_from_hex("#718089")
#        self.color_normal = get_color_from_hex("#718089")
#
#    def __call__(self):
#        self.add_item('Entrada','bio')
#        return self
#
#    def add_item(self, name, icon):
#        item = MDNavigationRailItem(text=name,
#                                    icon=icon)
#        self.add_widget(item)

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