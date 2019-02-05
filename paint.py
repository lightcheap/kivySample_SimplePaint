from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

### coding:UTF-8

class MyPaintWidget(Widget):

    def on_touch_down(self, touch): #押したとき
        color = (random(),random(),random())
        with self.canvas:
            Color(*color)#rgb指定
            d = 2. # 描画円の大きさ
            #2dの楕円を描画。座標は一番左上にあるのでポジションはそこを指定しないといけない。
            #サイズはｄのまま
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch): #押したまま動かす
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):

    def build(self):
        #描画エリアとボタンの親ウィジェット（中身はから）を作成
        parent = Widget()
        #MyPaintWidgetのインスタンすを作成
        self.painter = MyPaintWidget()
        #ボタンウィジェット作成
        clearbtn = Button(text='Clear')
        #bindでボタンを離したときにclear_canvas関数がなるようひもずける
        clearbtn.bind(on_release=self.clear_canvas)
        #親に各ウィジェットをひもずけ
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__=='__main__':
    MyPaintApp().run()