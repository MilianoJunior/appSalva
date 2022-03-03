#token = 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

import os
import sys
import multiprocessing
from pathlib import Path
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.clock import mainthread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from memory_profiler import memory_usage

from libs.composite import Composite


Clock.max_iteration = 20

registrar_componentes = ['main.py','composite.py','entrada.py']


def abrir():
    os.system("clear")
    os.system("python3 main.py")


class KvHandler(FileSystemEventHandler):
    def __init__(self, callback, target, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.callback = callback
        self.target = target

    def on_modified(self, event):
        for s in registrar_componentes:
            if os.path.basename(event.src_path) == s:
                self.callback(os.path.basename(event.src_path))

environ_root = 'SALVA_ROOT'
environ_assets = 'SALVA_ASSETS'

os.environ["SALVA_LANG"] = "1"

if getattr(sys, "frozen", False):
    os.environ[environ_root] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__))
    os.environ[environ_root] = str(Path(__file__).parent)
os.environ[environ_assets] = os.path.join(os.environ[environ_root],
          f"assets{os.sep}")


class Salva(MDApp):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Window.system_size = [300, 600]
        Window.top = 40
        Window.left = 10

    def build(self):
        TARGET = [files for files in os.listdir(f"{os.environ[environ_root]}")]
        PATH = os.environ[environ_root]
        o = Observer()
        o.schedule(KvHandler(self.update, TARGET), PATH, recursive=True)
        o.start()
        root = Composite()
        print(root())
        return root()

    def minimizar(self, *largs, **kwargs):
        print(os.getpid())
        mem_usage = memory_usage(os.getpid(), interval=.2, timeout=1, max_usage=True)
        print(mem_usage)
        print('main')
#        Window.minimize()--
    def on_stop(self, *args):
#        self.stop()
        Window.close()

    @mainthread
    def update(self, target, *args):
        print('executando update')
        self.stop()
        pc2 = multiprocessing.Process(target=abrir)
        pc2.start()
        pc2.join()
        self.stop()
        print('executando update')


if __name__ == "__main__":
    app = Salva()
    app.run()
