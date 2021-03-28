import pywhatkit
import pyautogui as py
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Schedule_Messenger(App):
        def build(self):
                Layout = FloatLayout()

                #LABELS
                Window.clearcolor = (1,0,0,0)

                label1 = Label(text = 'Recipient Phone Number',size_hint=(0.3, 0.05), pos_hint={'center_x':0.2, 'center_y':0.9})
                label2 = Label(text = 'Message', size_hint=(0.3, 0.05), pos_hint={'center_x':0.2, 'center_y':0.8})
                label3 = Label(text = 'Number of times \n to be repeated:', size_hint=(0.3, 0.05), pos_hint={'center_x':0.2, 'center_y':0.7})
                label4 = Label(text = 'Time: ', size_hint=(0.3, 0.05), pos_hint={'center_x':0.2, 'center_y':0.6})
                label5 = Label(text = 'Hour ', size_hint=(0.3, 0.05), pos_hint={'center_x':0.4, 'center_y':0.6})
                label6 = Label(text = 'Minutes ', size_hint=(0.3, 0.05), pos_hint={'center_x':0.7, 'center_y':0.6})

                #INPUT BOX

                self.input1 = TextInput(text = '', size_hint=(0.5, 0.05), pos_hint={'center_x':0.6, 'center_y':0.9})
                self.input2 = TextInput(text = '', size_hint=(0.5, 0.09), pos_hint={'center_x':0.6, 'center_y':0.8})
                self.input3 = TextInput(text = '', size_hint=(0.1, 0.05), pos_hint={'center_x':0.4, 'center_y':0.7})
                self.input4 = TextInput(text = '', size_hint=(0.1, 0.05), pos_hint={'center_x':0.5, 'center_y':0.6})
                self.input5 = TextInput(text = '', size_hint=(0.1, 0.05), pos_hint={'center_x':0.8, 'center_y':0.6})

                #QUIT & SUBMIT BUTTON
                quit = Button(text= 'QUIT', on_press=self.quitpress, size_hint=(0.07, 0.07), pos_hint={'center_x':0.2, 'center_y':0.4})
                button = Button(text= 'SUBMIT', on_press = self.buttonPress , size_hint=(0.07, 0.07), pos_hint={'center_x':0.8, 'center_y':0.4})
                
                #Executing Widgets

                Layout.add_widget(label1)
                Layout.add_widget(self.input1)

                Layout.add_widget(label2)
                Layout.add_widget(self.input2)

                Layout.add_widget(label3)
                Layout.add_widget(self.input3)

                Layout.add_widget(label4)

                Layout.add_widget(label5)
                Layout.add_widget(self.input4)

                Layout.add_widget(label6)
                Layout.add_widget(self.input5)

                Layout.add_widget(button)
                Layout.add_widget(quit)

                return Layout

        def quitpress(self,obj):
                self.get_running_app().stop()

        def buttonPress(self,obj):
                userphone = self.input1.text
                usermessage = self.input2.text
                userloop = self.input3.text
                userhr = self.input4.text
                usermin = self.input5.text
                

        #Function of Button

                phone2 = str(userphone)
                phone_no = "91+" + phone2
                usermessage1 = str(usermessage)
                a1 = eval(userloop)
                a = a1 - 1
                h = int(userhr)
                m = int(usermin)

                pywhatkit.sendwhatmsg(phone_no, usermessage1, h, m)

                for i in range(a):
                        py.typewrite(usermessage1)
                        py.press("enter")

if __name__ == '__main__':
        Schedule_Messenger().run()