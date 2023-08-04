
from tkinter import *
from translate import Translator


Screen = Tk()
Screen.title("Language Translator App")
Screen.config(bg="#FFECC4")
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()


LanguageChoices = {'Chinese', 'Russian', 'Hindi','English','French','German','Spanish', 'Korean', 'Japanese'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Spanish')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
InputLanguageChoiceMenu.config(bg="#b38ed3", fg="black")
Label(Screen,text="Select a Language", bg="#b38ed3", fg="black").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)


NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
NewLanguageChoiceMenu.config(bg="#b38ed3", fg="black")
Label(Screen,text="Translation", bg="#b38ed3", fg="black").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)

Label(Screen,text="Enter Text", bg="#b38ed3", fg="black").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar, bg="white", fg="black").grid(row=2,column = 1)

Label(Screen,text="Output Text", bg="#b38ed3", fg="black").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar, bg="white", fg="black").grid(row=2,column = 3)


Btn_translate = Button(Screen,text="Translate",command=Translate, relief = GROOVE, bg="#b38ed3", fg="black").grid(row=3,column=1,columnspan = 2)

mainloop()
