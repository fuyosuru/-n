from PyQt5.QtWidgets import QCheckBox,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QCompleter, QListWidget, QDialog, QComboBox
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QStringListModel
import sys
import os
import json
import pickle

class TrieNode:      
    def __init__(self):
        self.children = {}  
        self.word = False
        self.Meaning = "Không tìm thấy nghĩa của từ này"

class Trie:          
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, Meaning):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True
        node.Meaning = Meaning
        return node.word

    def find_suggest(self, node, word):     
        if(len(goi_y_list) >= 30):
            return
        for char in alphabet:
            if char in node.children:
                self.find_suggest(node.children[char], word + char)
        if node.word:
            goi_y_list.append(word)

    def search(self, word):        
        goi_y_list.clear()
        node = self.root
        for char in word:
            if char not in node.children:
                return "Không tìm thấy nghĩa của từ này"
            node = node.children[char]
        self.find_suggest(node, word)
        return node.Meaning

def lay_data():                 
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\word_meaning_anh_viet.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key, meaning in data.items():
        SuggestTree_Anh_Viet.insert(key, meaning)
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\dictionary.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key, meaning in data.items():
        SuggestTree_Anh_Anh.insert(key, meaning) 
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\word_meaning_viet_anh.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key, meaning in data.items():
        SuggestTree_Viet_Anh.insert(key, meaning)

def save_data():
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Anh_Anh.pkl", 'wb') as f:
        pickle.dump(historylist_Anh_Anh[-1000:], f)
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Anh_Anh.pkl", 'wb') as f:
        pickle.dump(favorite_list_Anh_Anh[-1000:], f)
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Anh_Viet.pkl", 'wb') as f:
        pickle.dump(historylist_Anh_Viet[-1000:], f)
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Anh_Viet.pkl", 'wb') as f:
        pickle.dump(favorite_list_Anh_Viet[-1000:], f)
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Viet_Anh.pkl", 'wb') as f:
        pickle.dump(historylist_Viet_Anh[-1000:], f)
    with open(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Viet_Anh.pkl", 'wb') as f:
        pickle.dump(favorite_list_Viet_Anh[-1000:], f)

def load_data():
    global historylist_Anh_Viet,historylist_Anh_Anh,historylist_Viet_Anh,favorite_list_Anh_Anh,favorite_list_Anh_Viet,favorite_list_Viet_Anh
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Anh_Anh.pkl"):
        with open(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Anh_Anh.pkl", 'rb') as f:
            historylist_Anh_Anh = pickle.load(f)
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Anh_Anh.pkl"):
        with open(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Anh_Anh.pkl", 'rb') as f:
            favorite_list_Anh_Anh = pickle.load(f)
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Anh_Viet.pkl"):
        with open(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Anh_Viet.pkl", 'rb') as f:
            historylist_Anh_Viet = pickle.load(f)
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Anh_Viet.pkl"):
        with open(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Anh_Viet.pkl", 'rb') as f:
            favorite_list_Anh_Viet = pickle.load(f)
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Viet_Anh.pkl"):
        with open(os.path.dirname(os.path.realpath(__file__)) + r"\historylist_Viet_Anh.pkl", 'rb') as f:
            historylist_Viet_Anh = pickle.load(f)
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Viet_Anh.pkl"):
        with open(os.path.dirname(os.path.realpath(__file__)) + r"\favorite_list_Viet_Anh.pkl", 'rb') as f:
            favorite_list_Viet_Anh = pickle.load(f)

def splitPath(path):
    return []


def bigger_font(size):
    font = QFont()
    font.setPointSize(size)
    return font

def typing():     
    input_value = user_input.text()
    if input_value != '':
        CurrentTree.search(input_value)
        model = QStringListModel()
        model.setStringList(goi_y_list)
        goi_y.setModel(model)
        user_input.setReadOnly(False)
    else:
        goi_y_list.clear()


def them_favorite():
    input_value = user_input.text()
    if checkbox.isChecked():
        if input_value not in favorite_list:
            favorite_list.append(input_value)
    else:
        if input_value in favorite_list:
            favorite_list.remove(input_value)

def press_button():    
    global checkbox
    input_value = user_input.text()
    Meaning = CurrentTree.search(input_value)
    text_box.clear()
    text_box.append(Meaning)
    if Meaning != "Không tìm thấy nghĩa của từ này":
        if language_selection.currentText() == "Anh - Anh":
            if input_value in historylist_Anh_Anh:
                historylist_Anh_Anh.remove(input_value)
            historylist_Anh_Anh.insert(0,input_value)
        else:
            if language_selection.currentText() == "Anh - Việt":
              if input_value in historylist_Anh_Viet:
               historylist_Anh_Viet.remove(input_value)
              historylist_Anh_Viet.insert(0,input_value)
            else:
              if input_value in historylist_Viet_Anh:
                historylist_Viet_Anh.remove(input_value)
              historylist_Viet_Anh.insert(0,input_value)
        if input_value in historylist:
            historylist.remove(input_value)
        historylist.insert(0,input_value)
        checkbox.setChecked(input_value in favorite_list)
        checkbox.show()  
    else:
        checkbox.hide()  

def History_giaodien():    
    global history_dialog
    history_dialog = QDialog()
    history_dialog.setWindowTitle('History')
    history_dialog_layout = QVBoxLayout()
    history_dialog.setLayout(history_dialog_layout)
    backbutton = QPushButton('Go back', history_dialog)
    history_dialog_layout.addWidget(backbutton)
    listbox = QListWidget()
    listbox.addItems(historylist)
    history_dialog_layout.addWidget(listbox)
    listbox.itemClicked.connect(Out_history)
    backbutton.clicked.connect(history_dialog.close)
    history_dialog.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)) + r"\images2.png")))
    history_dialog.exec_()

def Out_favorite(item):  
    user_input.setText(item.text())
    press_button()
    favorite_dialog.close()

def favorite_giaodien():   
    global favorite_dialog
    favorite_dialog = QDialog()
    favorite_dialog.setWindowTitle('Favorite')
    favorite_dialog_layout = QVBoxLayout()
    favorite_dialog.setLayout(favorite_dialog_layout)
    backbutton = QPushButton('Go back', favorite_dialog)
    favorite_dialog.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)) + r"\images2.png")))
    favorite_dialog_layout.addWidget(backbutton)
    listbox = QListWidget()
    listbox.addItems(favorite_list)
    favorite_dialog_layout.addWidget(listbox)
    listbox.itemClicked.connect(Out_favorite)
    backbutton.clicked.connect(favorite_dialog.close)
    favorite_dialog.exec_()

def Out_history(item): 
    user_input.setText(item.text())
    press_button()
    history_dialog.close()

def chuyen_mode(index):
    global CurrentTree,historylist,favorite_list
    if language_selection.currentText() == "Anh - Anh":
        CurrentTree = SuggestTree_Anh_Anh
        historylist=historylist_Anh_Anh
        favorite_list=favorite_list_Anh_Anh
    else:
        if language_selection.currentText() == "Anh - Việt":
            CurrentTree = SuggestTree_Anh_Viet
            historylist=historylist_Anh_Viet
            favorite_list=favorite_list_Anh_Viet
        else:
            CurrentTree = SuggestTree_Viet_Anh
            historylist=historylist_Viet_Anh
            favorite_list=favorite_list_Viet_Anh
    text_box.clear()
    user_input.clear()
    checkbox.hide()

alphabet = "aàảãáạăằẳẵắặâầẩẫấậbcdđeèẻẽéẹêềểễếệghiìỉĩíịjklmnoòỏõóọôồổỗốộơờởỡớợpqrstuùủũúụưừửữứựvwxyỳỷỹýỵz " 

SuggestTree_Anh_Anh = Trie()
SuggestTree_Anh_Viet = Trie()
SuggestTree_Viet_Anh = Trie()
CurrentTree = Trie()
goi_y_list = []
historylist = []
favorite_list = []
historylist_Anh_Anh = []
historylist_Viet_Anh = []
historylist_Anh_Viet = []
favorite_list_Anh_Viet = []
favorite_list_Viet_Anh = []
favorite_list_Anh_Anh = []


fuyonary = QApplication(sys.argv)
giaodien = QWidget()
layout = QVBoxLayout()
giaodien.setLayout(layout)
giaodien.setGeometry(100, 100, 800, 600)
user_input = QLineEdit(giaodien)    
user_input.setFont(bigger_font(10))
language_selection = QComboBox(giaodien)
language_selection.addItems(["Anh - Anh", "Anh - Việt","Việt - Anh"]) 
language_selection.setFont(bigger_font(10))   
layout.addWidget(language_selection)
goi_y = QCompleter()  
goi_y.splitPath = splitPath
user_input.setCompleter(goi_y)
user_input.setPlaceholderText('Nhập từ cần tra')
layout.addWidget(user_input)
search_button = QPushButton('Search', giaodien)     # nút Search
search_button.setFont(bigger_font(10)) 
layout.addWidget(search_button)
text_box = QTextEdit(giaodien)  
text_box.setReadOnly(True)
text_box.setFont(bigger_font(10))
layout.addWidget(text_box)
checkbox = QCheckBox('Thêm từ vào favorite', giaodien)
checkbox.setFont(bigger_font(10))
layout.addWidget(checkbox)
checkbox.stateChanged.connect(them_favorite)
checkbox.hide() 
button_layout = QHBoxLayout()
history_button = QPushButton('History', giaodien)   
history_button.setFont(bigger_font(10))
favorite_button = QPushButton('Favorite', giaodien)
favorite_button.setFont(bigger_font(10)) 
button_layout.addWidget(history_button)
button_layout.addWidget(favorite_button)
layout.addLayout(button_layout)
user_input.textChanged.connect(typing)
search_button.clicked.connect(press_button)
history_button.clicked.connect(History_giaodien)
favorite_button.clicked.connect(favorite_giaodien)
giaodien.setWindowTitle('fuyonary')
giaodien.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.realpath(__file__)) + r"\images2.png")))
giaodien.show()
language_selection.currentIndexChanged.connect(chuyen_mode)
lay_data()
load_data()
chuyen_mode("Anh - Anh")
fuyonary.aboutToQuit.connect(save_data)
CurrentTree=SuggestTree_Anh_Anh
fuyonary.setStyleSheet("""
QPushButton {
    border: 2px solid #000080; 
    border-radius: 15px; 
    padding: 5px;
    background-color: #FFFFFF; 
}
    QLineEdit {
    border: 2px solid #000080; 
    border-radius: 15px;
    padding: 5px;
    background-color: #FFFFFF; 
}
    QComboBox {
    border: 2px solid #000080; 
    border-radius: 10px; 
    padding: 5px;
    background-color: #add8e6; 
}
    QComboBox::drop-down {
    width: 30px;
    border-left: 1px solid #000080;
}
    QTextEdit {
    border: 2px solid #add8e6; 
    border-radius: 10px; 
    padding: 5px;
    background-color: #FFFFFF; 
    color: #000000; 
    font-family: Arial, sans-serif;
}
    QListWidget {
    border: 2px solid #add8e6; 
    border-radius: 10px; 
    padding: 5px;
    background-color: #FFFFFF; 
    color: #000000; 
    font-family: Arial, sans-serif;
}

QListWidget::item {
    padding: 5px;
    margin: 2px;
}

QListWidget::item:selected {
    background-color: #add8e6; 
    color: #FFFFFF; 
}

""")
sys.exit(fuyonary.exec_())
