from seleniumbase import BaseCase

#Testes feitos na página de demonstração do SeleniumBase.

class Casos(BaseCase):


    #Caso Input - Confere se a textbox está recebendo texto corretamente.
    def test_caso_input(self):
        self.open("https://seleniumbase.io/demo_page")
        self.type("#myTextarea", "Caso Input")
        self.assert_no_js_errors



    #Caso Barra Html - Confere se a barra está em 25%, então seleciona a opção de mudar para 100% e então confere se ela foi atualizada para 100%.

    def test_caso_htmlbar(self):
        self.open("https://seleniumbase.io/demo_page")
        self.assert_element('meter[value="0.25"]')
        self.select_option_by_text("#mySelect", "Set to 100%")
        self.assert_element('meter[value="1"]')


    #Caso Slider - Confere se o valor do slider está em 50, então após isso move o slider duas vezes, e então compara se o valor atual é de 70%.
    def test_caso_slider(self):
     self.open("https://seleniumbase.io/demo_page")
     self.assert_element('progress[value="50"]')
     self.press_right_arrow("#myslider", times=2)
     self.assert_element('progress[value="70"]')


    #Caso(ERRO) - Confere o texto que aparece ao clicar no botão. Retorna um erro, pois o texto correto seria "This Text is Purple", não "This Text is Blue".
    def test_caso_erro(self):
        self.open("https://seleniumbase.io/demo_page")
        self.assert_text("This Text is Green", "#pText")
        self.click("#myButton")
        self.assert_text("This Text is Blue", "#pText")



    #Caso Checkbox&DragDrop - Clica no checkbox, verifica se ele está verdadeiro, então confere a presença da imagem que apareceu, então arrasta ela e depois confere sua nova posição.
    def test_dragdrop_checkbox(self):

        self.open("https://seleniumbase.io/demo_page")
        self.click("#checkBox1")
        self.assert_true(self.is_selected("#checkBox1"))
        self.assert_element("img#logo")
        self.assert_element_not_visible("div#drop2 img#logo")
        self.drag_and_drop("img#logo", "div#drop2")
        self.assert_element("div#drop2 img#logo")


    # Caso Button - Confere se, ao clicar no botão, o texto muda para "This Text is Purple".
    def test_caso_button(self):
        self.open("https://seleniumbase.io/demo_page")
        self.assert_text("This Text is Green", "#pText")
        self.click("#myButton")
        self.assert_text("This Text is Purple", "#pText")

