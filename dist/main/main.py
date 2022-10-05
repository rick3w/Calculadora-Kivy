from kivy.config import Config
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 400)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calc(BoxLayout):

    def clicarBotao(self, botao):
        operadores = '/*-+'

        try:

            if self.output.text == '0' or self.result:
                assert botao not in operadores
                self.output.text = botao
                self.result = False

            else:

                if botao in operadores:

                    for x in operadores:
                        assert x not in self.output.text

                    self.output.text += botao

                else:
                    self.output.text += botao

        except:
            pass

    def apagar(self):

        if self.result == False:

            if len(self.output.text) == 1:
                self.output.text = '0'

            else:
                self.output.text = self.output.text[:-1]

    def resultado(self):

        try:
            result = float(eval(self.output.text))

            if result.is_integer():
                result = int(result)

            self.output.text = str(result)
            self.result = True

        except:
            pass

class MyApp(App):

    def build(self):
        self.title = 'Calculadora'
        self.icon = 'calc.png'
        return Calc()

if __name__ == '__main__':
    MyApp().run()
