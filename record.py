from pynput import mouse, keyboard
import os

class MyException(Exception): pass


class record :
    global str
    def __init__(self, parent):
        self.parent = parent
        self.fo = open("/result.txt", "w")
        with keyboard.Listener(
                on_press=self.on_press) as k:
            with mouse.Listener(
                    on_click=self.on_click
            ) as m:
                try:
                    self.k = k
                    self.m = m

                    self.k.join()
                    self.m.join()
                except MyException as e:
                    print('{0} was clicked'.format(e.args[0]))

    def on_click(self, x, y, button, pressed):
        if pressed :
            if format(button).find('left'):
                self.update_string(x, y, 'ML')
            else :
                self.update_string(x, y, 'MR')

    def update_string(self, x, y, button):
        self.fo.write(button+":"+str(x)+ ":"+str(y))
        self.fo.write("\n")

    def start(self):
        self.k.start()
        self.m.start()



    def on_press(self,key):
        try:
            print(format(key.char))
        except AttributeError:
            print(format(key))
            if format(key) == 'Key.f4' :
                self.fo.close()
                self.k.stop()
                self.m.stop()
                fi = open("/result.txt", "r")
                with fi:
                    data = fi.read()
                fi.close()
                os.remove("/result.txt")
                self.parent.data = data
            # print('special key {0} pressed'.format(
            #     key))


