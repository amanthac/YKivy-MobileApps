# UPDATES: Add color palette to choose from. Have save button to save drawing

from kivy.graphics import Color, Line
from kivy.properties import ListProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

Window.size = (345, 545)

paint_design = """
ScreenManager:
    Paint_Home:
    Palette:

<TooltipMDIconButton@MDIconButton+MDTooltip>

<Paint_Home>:
    name: "paint_home"

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos 

    # MENU OPTIONS
    TooltipMDIconButton:
        icon: "pencil"
        tooltip_text: "Pencil"
        pos_hint: {"center_y": 0.95, "center_x": 0.05}
        on_press: root.set_pen_width(self.icon)
    TooltipMDIconButton:
        icon: "pen"
        tooltip_text: "Pen"
        pos_hint: {"center_y": 0.87, "center_x": 0.05}
        on_press: root.set_pen_width(self.icon)
    TooltipMDIconButton:
        icon: "marker"
        tooltip_text: "Marker"
        pos_hint: {"center_y": 0.79, "center_x": 0.05}
        on_press: root.set_pen_width(self.icon)
    TooltipMDIconButton:
        icon: "eraser"
        #user_font_size: 30
        tooltip_text: "Eraser"
        pos_hint: {"center_y": 0.71, "center_x": 0.05}
        md_bg_color: (1, 1, 1, 1)
        on_press: root.set_pen_color(self.md_bg_color)
        on_press: root.set_eraser_width()
    TooltipMDIconButton:
        icon: "palette"
        tooltip_text: "Choose Palette"
        pos_hint: {"center_y": 0.63, "center_x": 0.05}
        on_press: root.manager.current = "palette"

    # MAIN COLOR OPTIONS
    MDRaisedButton:
        md_bg_color: 0, 0, 0, 1
        size_hint: (0.045, 0.05)
        pos_hint: {"center_y": 0.55, "center_x": 0.05}
        on_press: root.set_pen_color(self.md_bg_color)
    MDRaisedButton:
        md_bg_color: 219/255, 219/255, 219/255, 1
        size_hint: (0.045, 0.05)
        pos_hint: {"center_y": 0.47, "center_x": 0.05}
        on_press: root.set_pen_color(self.md_bg_color)
    MDRaisedButton:
        md_bg_color: 1, 0, 0, 1
        size_hint: (0.045, 0.05)
        pos_hint: {"center_y": 0.39, "center_x": 0.05}
        on_press: root.set_pen_color(self.md_bg_color)
    MDRaisedButton:
        md_bg_color: 41/255, 163/255, 74/255, 1
        size_hint: (0.045, 0.05)
        pos_hint: {"center_y": 0.31, "center_x": 0.05}
        on_press: root.set_pen_color(self.md_bg_color)
    MDRaisedButton:
        md_bg_color: 41/255, 120/255, 163/255, 1
        size_hint: (0.045, 0.05)
        pos_hint: {"center_y": 0.23, "center_x": 0.05}
        on_press: root.set_pen_color(self.md_bg_color)
    MDRaisedButton:
        md_bg_color: 1, 1, 0, 1
        size_hint: (0.045, 0.05)
        pos_hint: {"center_y": 0.15, "center_x": 0.05}
        on_press: root.set_pen_color(self.md_bg_color)
    MDRaisedButton:
        md_bg_color: 157/255, 52/255, 179/255, 1
        size_hint: (0.045, 0.05)
        pos_hint: {"center_y": 0.07, "center_x": 0.05}
        on_press: root.set_pen_color(self.md_bg_color)

    MDSeparator:
        height: "3dp"
        pos_hint: {"center_y": 0.82, "center_x": 0.1}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 90
                origin: self.center
        canvas.after:
            PopMatrix
    MDSeparator:
        height: "3dp"
        pos_hint: {"center_y": 0.18, "center_x": 0.1}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 90
                origin: self.center
        canvas.after:
            PopMatrix

<Palette>:
    name: "palette"

    MDSlider:
        id: eraser_thickness_slider
        min: 0
        max: 10
        value: 7
        size_hint_x: 0.5
        size_hint_y: 0.1
        pos_hint: {"center_y": 0.1, "center_x": 0.33}

    MDTextButton:
        text: "Eraser thickness: " + str(int(eraser_thickness_slider.value))
        pos_hint: {"center_y": 0.05, "center_x": 0.33}

    MDRaisedButton:
        text: "DONE"
        pos_hint: {"center_y": 0.05, "center_x": 0.77}
        on_press: root.done_command()

"""


class Paint_Home(Screen):
    pencolor = ListProperty([0, 0, 0, 1])
    pen_width = 2

    def __init__(self, **kwargs):
        super(Paint_Home, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        return True

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return
        with self.canvas:
            Color(rgba=self.pencolor)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.pen_width)

    def on_touch_move(self, touch):
        if Widget.on_touch_move(self, touch):
            return
        try:
            touch.ud['line'].points += [touch.x, touch.y]
        except:
            pass

    def set_pen_color(self, new_color):
        self.pencolor = new_color

    def set_pen_width(self, line_width):
        self.pen_width = {"pencil": 1, "pen": 2, "marker": 4}[line_width]

    def set_eraser_width(self):
        with open("color_palette.txt") as c:
            thickness_number = c.read()
        self.pen_width = int(thickness_number)


class Palette(Screen):
    def done_command(self):
        with open("color_palette.txt", "w") as c:
            c.write(str(int(self.ids.eraser_thickness_slider.value)))
        self.manager.current = "paint_home"


sm = ScreenManager()
sm.add_widget(Paint_Home(name="paint_home"))
sm.add_widget(Palette(name="palette"))


class Paint_App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        paint_design_string = Builder.load_string(paint_design)
        return paint_design_string

    def on_start(self):
        with open("color_palette.txt", "w") as c:
            c.write("7")


Paint_App().run()
