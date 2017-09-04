from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.popup import Popup
import pymysql
import CSVtoSQL_logic
import tkinter as tk
from tkinter.filedialog import askopenfilename

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '460')


class CustomPopup1(Popup):
    pass


class CustomPopup2(Popup):
    pass


class CSVtoSQL(BoxLayout):
    file_name_text = ObjectProperty()
    file_delimiter_text = ObjectProperty()
    server_host_text = ObjectProperty()
    server_port_text = ObjectProperty()
    server_user_text = ObjectProperty()
    server_pass_text = ObjectProperty()
    server_db_text = ObjectProperty()
    server_table_name = ObjectProperty()
    server_connection_status_text = ObjectProperty()
    student_list = ObjectProperty()
    file_name = ''

    def test_connection(self):
        try:
            h_name = self.server_host_text.text
            p_name = int(self.server_port_text.text)
            user_name = self.server_user_text.text
            pass_name = self.server_pass_text.text
            db_name = self.server_db_text.text
            conn = pymysql.connect(host=h_name, port=p_name, user=user_name, passwd=pass_name, db=db_name)
            conn.close()
            self.server_connection_status_text.text = 'CONNECTION SUCCESSFUL'
        except:
            self.server_connection_status_text.text = 'CONNECTION FAILED'

    def open_file(self):
        try:
            root = tk.Tk()
            root.withdraw()
            name = askopenfilename(initialdir="C:/Users/Kamil/Desktop/",
                                   filetypes=(("Text File", "*.csv"), ("All Files", "*.*")),
                                   title="Choose a file."
                                   )
            print(name)
            self.file_name_text.text = name
            CSVtoSQL.file_name = name
        except:
            print("Something got wrong.")

    def submit_file(self):
        try:
            h_name = self.server_host_text.text
            p_name = int(self.server_port_text.text)
            user_name = self.server_user_text.text
            pass_name = self.server_pass_text.text
            db_name = self.server_db_text.text
            table_name = self.server_table_name.text
            file_delimiter = self.file_delimiter_text.text

            CSVtoSQL_logic.insertCSVtoSQL(h_name, p_name, user_name, pass_name, db_name, table_name, CSVtoSQL.file_name,
                                          file_delimiter)
            the_popup = CustomPopup1()
            the_popup.open()
        except:
            print('Something failed')
            the_popup = CustomPopup2()
            the_popup.open()


class CSVtoSQLApp(App):
    def build(self):
        return CSVtoSQL()


dbApp = CSVtoSQLApp()
dbApp.run()
