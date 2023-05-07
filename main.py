import kivy,os
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
# from android.permissions import request_permissions, Permission

# request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

root_dir = os.getcwd()

class RootDirScreen(Screen):
    def set_root_dir(self):
        self.parent.parent.root_dir = self.ids.file_chooser.path
        self.parent.dismiss()


class PdfSearch(BoxLayout):
    def __init__(self, **kwargs):
        super(PdfSearch, self).__init__(**kwargs)
        self.input = self.ids.input
        self.results = []

    def select_root_dir(self, event):
        # Open a file browser to select the root directory
        dir_content = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        dir_content.add_widget(file_chooser)

        popup = Popup(title='Select Root Directory',
                      content=dir_content,
                      size_hint=(0.9, 0.9),
                      auto_dismiss=False)

        def set_root_dir(event):
            self.root_dir = file_chooser.path
            popup.dismiss()

        set_dir_button = Button(text='Set Root Directory',
                                size_hint_y=None,
                                height='50dp')
        set_dir_button.bind(on_press=set_root_dir)
        dir_content.add_widget(set_dir_button)

        popup.open()


    def search(self, event):
        self.found_list = []
        self.ids.result_box.clear_widgets()
        ext = self.ids.extension.text
        extension = '.' + self.ids.extension.text if ext else '.txt'
        key = self.input.text
        for dir, sub_dir, file_lst in os.walk(root_dir):
            for file in file_lst:
                if file.endswith(extension):
                    with open(file,'r+') as item:
                        data = item.read()
                        if key in data:
                            self.found_list.append(file)
        self.add_results()
  
    def add_results(self):
        for i in self.found_list:
            button_exists = False
            for child in self.ids.result_box.children:
                if isinstance(child, Button) and child.text == i:
                    button_exists = True
                    break
            if not button_exists:
                lbl = Button(text=i, background_color=(0.2, 0.2, 0.2))
                self.ids.result_box.add_widget(lbl)

class PdfSearchApp(App):
    def build(self):
        return PdfSearch()

if __name__ == '__main__':
    PdfSearchApp().run()
