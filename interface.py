
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

from assets import logicaCriptografia
class Application:

    ScreenStartStatus = 'closed'
    ScreenEncryptDecryptStatus = 'closed'
    ScreenHelpStatus = 'closed'
    ScreenCreditsStatus = 'closed'
    RefuseDataEntryStatus = True

    def __init__(self, master=None):
        self.startScreen()

    def startScreen(self, master=None):
        self.ScreenStartStatus = "open"
        self.screenStart = Frame(master)
        self.screenStart.pack(fill="both", expand=1)

        self.titleContainer = Frame(self.screenStart, bg="#02242e")
        self.titleContainer.pack(fill="both", expand=1, side=TOP)

        self.buttonContainer = Frame(self.screenStart, pady=120, bg="#02242e")
        self.buttonContainer.pack(fill="both", expand=1, side=TOP)

        Label(self.titleContainer, fg="#fff", bg="#02242e", text="OceanCript", font=("System", "32", "bold")).pack(
            side=BOTTOM)

        Button(self.buttonContainer, cursor="hand2", bg="#5ecadb", bd=0, text="Iniciar", width=10, height=1, font=("System", "25"), fg="#18383d", highlightthickness=3, highlightbackground="#81ecfd", command=self.openStartMenuScreen).pack(side=TOP)

    def openStartMenuScreen(self):
        if self.ScreenStartStatus == "open":
            self.screenStart.destroy()

        self.screenMenu = Frame(master=None, bg="#02242e")
        self.screenMenu.pack(fill="both", expand=1)

        self.optionsContainer = Frame(self.screenMenu)
        self.optionsContainer.pack(expand=1)

        Button(self.optionsContainer, cursor="hand2", bg="#0097a7", bd=0, text="Criptografar / Descriptografar", width=25,
            font=("System", "18"), fg="#ffffff", highlightthickness=1, highlightbackground="#011116", command=self.open_Encrypt_Decrypt_Screen).pack()

        Button(self.optionsContainer, cursor="hand2", bg="#32828a", bd=0, text="Ajuda", width=25,
            font=("System", "18"), fg="#ffffff", highlightthickness=1, highlightbackground="#011116", command= self.openHelpScreen).pack()

        Button(self.optionsContainer, cursor="hand2", bg="#32828a", bd=0, text="Créditos", width=25,
            font=("System", "18"), fg="#ffffff", highlightthickness=1, highlightbackground="#011116", command=self.openCreditsScreen).pack()

        Button(self.optionsContainer, cursor="hand2", bg="#8a3d39", bd=0, text="Sair", width=25,
            font=("System", "18"), fg="#ffffff", highlightthickness=1, highlightbackground="#011116", command=root.destroy).pack()

    def open_Encrypt_Decrypt_Screen(self):
        self.screenMenu.destroy()
        self.ScreenEncryptDecryptStatus = "open"
        self.screen_Encrypt_Decrypt = Frame(master=None, bg="#020e06")
        self.screen_Encrypt_Decrypt.pack(fill="both", expand=1)

        # Top
        self.topContainer = Frame(self.screen_Encrypt_Decrypt, bg="#02242e")
        self.topContainer.pack(side=TOP, fill="both", expand=1)

        self.supportMenuContainer = Frame(self.topContainer,pady=8, bg="#02242e")
        self.supportMenuContainer.pack(side=TOP, fill="x")
        Button(self.supportMenuContainer, cursor="hand2", text="Voltar", height=1, width=7, highlightthickness=2, highlightbackground="#105e8a", bd=0, bg="#318abd", fg="#ffffff",font=("System", "16"),command=self.backToMenu).pack(side=LEFT, padx=16)

        Label(self.topContainer, fg="#fff", bg="#02242e", text="Digite seu texto: ", font=("System", "20")).pack(fill="x", padx=8, pady=10)
        self.inputText = Text(self.topContainer,bg="#9ccfd4", fg="#000", bd=0, font=("Arial", "16"), height=5, highlightthickness=3, highlightbackground="#075058")
        self.inputText.pack(fill="x", padx=16)

        # Middle
        self.optionsContainer = Frame(self.topContainer, bg="#02242e")
        self.optionsContainer.pack(side=LEFT)


        # Main container to key
        self.keyContainer = Frame(self.topContainer, bg="#02242e")
        self.keyContainer.pack(side=RIGHT, padx=16)

        # Key container
        self.supportKeyContainer = Frame(self.keyContainer, bg="#02242e")
        self.supportKeyContainer.pack(side=TOP)
        Label(self.supportKeyContainer, font=("System", "18"), fg="#5296a1", bg="#02242e", bd=0,
              text="Chave: ").pack(side=LEFT)
        self.inputKey = Entry(self.supportKeyContainer, validate="key", highlightthickness=2, width=25,
                                    validatecommand=(root.register(self.actionValidate_entry), "%P"), bg="#d5683e", bd=0,
                                    fg="#fff", font=("System", "16"))
        self.inputKey.pack(side=TOP, ipady=2, pady=5)
        self.inputKey.configure(highlightbackground="#a24930", highlightcolor="#a24930")

        self.statusKey = Label(self.keyContainer, font=("System", "16"), fg="#fff", bg="#02242e", bd=0,text="Aguardando seleção de método... ")
        self.statusKey.pack(side=TOP)



        # Button Encrypt
        self.encryptActionButton = Button(self.optionsContainer, cursor="hand2", text="Criptografar", width=10, bg="#8edb95", bd=0, fg="#163b19", highlightthickness=3, highlightbackground="#639d68", state='normal', font=("System", "18"), command= self.openWindowReceiveKey)
        self.encryptActionButton.pack(side=LEFT, padx=16, ipady=2, pady=8)

        # Button Decrypt
        self.decryptActionButton = Button(self.optionsContainer,  command= self.openWindowInsertKey, cursor="hand2", text="Descriptografar", width=12, bg="#ce8a8a", bd=0, fg="#3b1616", highlightthickness=3, highlightbackground="#986464", font=("System", "18"))

        self.decryptActionButton.pack(side=LEFT, padx=16, ipady=2, pady=8)

        # Bottom
        self.bottomContainer = Frame(self.screen_Encrypt_Decrypt, bg="#02242e")
        self.bottomContainer.pack(side=TOP, fill="both", expand=1)

        Label(self.bottomContainer, fg="#fff", text="Resultado: ", font=("System", "20"), bg="#02242e").pack(fill="x", padx=8, pady=10)
        self.resultText = Text(self.bottomContainer,bg="#699398", fg="#fff", bd=0, font=("Arial", "16"), height=5, highlightthickness=3, highlightbackground="#075058")
        self.resultText.config(state=DISABLED)
        self.resultText.pack(fill="x", padx=16)

        self.supportBottomContainer = Frame(self.bottomContainer, pady=8, bg="#020e06")
        self.supportBottomContainer.pack(side=BOTTOM, fill="x")

        self.convertActionButton= Button(self.bottomContainer, cursor="hand2", text="Converter", width=15, bd=0, fg="#473500", highlightthickness=3, highlightbackground="#a5872e", bg="#ddba4e", font=("System", "20"), command=self.actionConvertData)
        self.convertActionButton.pack(side=TOP, padx=16, ipady=3, pady=25)

    def openWindowInsertKey(self):


        self.RefuseDataEntryStatus = False

        self.encryptActionButton["bg"] = 'azure4'
        self.encryptActionButton["state"] = 'normal'
        self.decryptActionButton["bg"] = 'firebrick'
        self.decryptActionButton["state"] = DISABLED

        self.statusKey.config(text="Insira sua chave acima.")


    def openWindowReceiveKey(self):

        self.inputKey.delete(0, 'end')
        self.RefuseDataEntryStatus = True

        self.encryptActionButton["bg"] = 'aquamarine4'
        self.encryptActionButton["state"] = DISABLED
        self.decryptActionButton["bg"] = 'azure4'
        self.decryptActionButton["state"] = 'normal'

        self.statusKey.config(text = "Aguardando conversão para gerar chave...")

    def openHelpScreen(self):
        self.screenMenu.destroy()
        self.ScreenHelpStatus = "open"
        self.helpScreen = Frame(master=None, bg="#02242e")
        self.helpScreen.pack(fill="both", expand=1, side=TOP)

        self.topContainer = Frame(self.helpScreen, bg="#02242e")
        self.topContainer.pack(fill="x", pady=5)
        Button(self.topContainer, height=1, width=7, cursor="hand2", text="Voltar", font=("System", "16"),
               highlightthickness=2, highlightbackground="#105e8a", bd=0, bg="#318abd", fg="#ffffff",
               command=self.backToMenu).pack(side=LEFT, padx=16)
        Label(self.helpScreen, fg="#fff", bg="#02242e", text="Ajuda", font=("System", "32", "bold")).pack(
            side=TOP,pady=10)

        self.middleContainer = Frame(self.helpScreen, bg="#02242e")
        self.middleContainer.pack(fill="x")
        Label(self.middleContainer, fg="#fff", bg="#02242e", text="Criptografia:",font=("System", "22")).pack(side=TOP, pady=20)
        Label(self.middleContainer, wraplength=800, fg="#fff", bg="#02242e", font=("System", "16"),
            text="Para criptografar insira o texto e selecione a opção de criptografia, após isto basta converter o texto e logo será retornado o seu texto criptografado junto a sua chave para uma futura descriptografia.").pack(fill="x")

        self.bottomContainer = Frame(self.helpScreen, bg="#02242e")
        self.bottomContainer.pack(fill="x",pady=40)
        Label(self.bottomContainer, fg="#fff", bg="#02242e", text="Descriptografia:",font=("System", "22")).pack(side=TOP)
        Label(self.bottomContainer, wraplength=800, fg="#fff", bg="#02242e", font=("System", "16"),
            text="Para descriptografar um texto selecione a opção de descriptografia e informe os valores de sua chave e também do seu texto criptografado na primeira área de texto, após isto basta converter o texto e logo será retornado o texto descriptografado.").pack()

    def openCreditsScreen(self):
        self.screenMenu.destroy()
        self.creditsScreen = Frame(master=None, bg="#02242e")
        self.creditsScreen.pack(fill="both", expand=1, side=TOP)
        self.ScreenCreditsStatus = "open"

        self.topContainer = Frame(self.creditsScreen, bg="#02242e")
        self.topContainer.pack(fill="x", pady=5)
        Button(self.topContainer, height=1, width=7, cursor="hand2", text="Voltar",font=("System", "16"), highlightthickness=2, highlightbackground="#105e8a", bd=0, bg="#318abd", fg="#ffffff", command=self.backToMenu).pack(side=LEFT, padx=16)
        Label(self.creditsScreen, fg="#fff", bg="#02242e", text="Créditos", font=("System", "32", "bold")).pack(side=TOP)

        self.middleContainer = Frame(self.creditsScreen, bg="#fff")
        self.middleContainer.pack(pady=15)

        #Guilherme Dias
        self.containerGuiD = Frame(self.middleContainer, bg="#02242e")
        self.containerGuiD.pack(side=LEFT)
        self.imageGuiD = PhotoImage(file="images/imageGuilhermeDias.png")
        Label(self.containerGuiD, image=self.imageGuiD, width=180, height=180).pack(side=TOP,padx=62)
        Label(self.containerGuiD, fg="#fff", bg="#02242e", text="Guilherme Dias", font=("System", "20")).pack(side=BOTTOM)


        #Guilherme Leandro
        self.containerGuiL = Frame(self.middleContainer, bg="#02242e")
        self.containerGuiL.pack(side=LEFT)
        self.imageGuiL = PhotoImage(file="images/imageGuilhermeLeandro.png")
        Label(self.containerGuiL, image=self.imageGuiL, width=180, height=180).pack(side=TOP)
        Label(self.containerGuiL, fg="#fff", bg="#02242e", text="Guilherme Leandro", font=("System", "20")).pack(side=TOP)

        #Helen Silva
        self.containerHelen = Frame(self.middleContainer, bg="#02242e")
        self.containerHelen.pack(side=LEFT)
        self.imageHelen = PhotoImage(file="images/imageHelen.png")
        Label(self.containerHelen, image=self.imageHelen, width=180, height=180).pack(side=TOP,padx=62)
        Label(self.containerHelen, fg="#fff", bg="#02242e", text="Helen Silva", font=("System", "20")).pack(side=TOP)

        self.bottomContainer = Frame(self.creditsScreen, bg="#020e06")
        self.bottomContainer.pack(pady=10)


        # Luiz Filipe
        self.containerLuiz = Frame(self.bottomContainer, bg="#02242e")
        self.containerLuiz.pack(side=LEFT)
        self.imageLuiz = PhotoImage(file="images/imageLuiz.png")
        Label(self.containerLuiz, image=self.imageLuiz, width=180, height=180).pack(side=TOP, padx=62)
        Label(self.containerLuiz, fg="#fff", bg="#02242e", text="Luiz Filipe", font=("System", "20")).pack(side=BOTTOM)


        # Vitor Oliveira
        self.containerVitor = Frame(self.bottomContainer, bg="#02242e")
        self.containerVitor.pack(side=LEFT)
        self.imageVitor = PhotoImage(file="images/imageVitor.png")
        Label(self.containerVitor, image=self.imageVitor, width=180, height=180).pack(side=TOP, padx=62)
        Label(self.containerVitor, fg="#fff", bg="#02242e", text="Vitor Oliveira", font=("System", "20")).pack(side=BOTTOM)

    def backToMenu(self):
        if self.ScreenEncryptDecryptStatus == "open":
            self.ScreenEncryptDecryptStatus = "closed"
            self.screen_Encrypt_Decrypt.destroy()
        if self.ScreenHelpStatus == "open":
            self.ScreenHelpStatus = "closed"
            self.helpScreen.destroy()
        if self.ScreenCreditsStatus == "open":
            self.ScreenCreditsStatus = "closed"
            self.creditsScreen.destroy()

        self.openStartMenuScreen()

    def backToStartScreen(self):
        self.screenMenu.destroy()
        self.startScreen()

    def actionEncryptText(self):
        textoParaCriptografar = self.inputText.get("1.0",'end-1c')
        rsaCriptografado = logicaCriptografia.interfaceCriptografar(textoParaCriptografar)
        formatKey = str(rsaCriptografado.d) + "-" + str(rsaCriptografado.n)

        self.inputText.delete("1.0", "end")
        self.resultText.config(state="normal")
        self.resultText.delete("1.0", "end")
        self.resultText.insert("end", rsaCriptografado.textoCriptografado)
        self.resultText.config(state=DISABLED)

        self.RefuseDataEntryStatus = False
        self.inputKey.insert(0, formatKey)
        self.RefuseDataEntryStatus = True

    def actionDecryptText(self):
        textToDecrypt = self.inputText.get("1.0", 'end-1c').strip()
        keys = self.inputKey.get()

        validateText = True
        arrayText = textToDecrypt.split(" ")
        arrayText[-1] = arrayText[-1].strip()
        for i in arrayText:
            if not i.isdigit():
                validateText = False
                break

        validateKey = True
        def keyIsFormated():
            if keys.__contains__("-"):
                fields = keys.split("-")
                if fields[0] == "" or fields[0] == None or fields[1] == "" or fields[1] == None:
                    return False
                else:
                    return True
            return False

        if keys == None or keys == "" or not keyIsFormated():
            validateKey = False

        if validateText and validateKey:
            self.inputText.delete("1.0", "end")
            arrayTextoDescriptografado = logicaCriptografia.interfaceDescriptografar(keys, arrayText)
            self.resultText.config(state="normal")
            self.resultText.delete("1.0", "end")
            self.resultText.insert("end", arrayTextoDescriptografado)
            self.resultText.config(state=DISABLED)
        elif not validateText:
            messagebox.showinfo("Alerta", "Para descriptografar a caixa de texto deve apenas conter números!")
        elif not validateKey:
            messagebox.showinfo("Alerta", "Para descriptografar a chave deve estar no formato correto!")

    def actionValidate_entry(self, text):
        if not self.RefuseDataEntryStatus:
            validadeOne = text.count("-") == 1
            textFormat = text
            if validadeOne:
                textFormat = text.replace("-", '')

            if str.isdigit(textFormat) or text == "":
                return True
            else:
                return False
        else:
            return False


    def actionConvertData(self):
        if self.encryptActionButton['state'] == 'disabled':
            if self.inputText.get("1.0", 'end-1c') != '':
                self.actionEncryptText()
            else:
                messagebox.showinfo("Alerta", "Insira o texto para a criptografia.")
        elif self.decryptActionButton['state'] == 'disabled':
            if self.inputText.get("1.0", 'end-1c') != '' and self.inputKey.get() != '':
                self.actionDecryptText()
            elif self.inputText.get("1.0", 'end-1c') == '':
                messagebox.showinfo("Alerta", "Insira o texto criptografado.")
            else:
                messagebox.showinfo("Alerta", "Insira sua chave privada.")
        else:
            messagebox.showinfo("Alerta", "Selecione primeiro o método desejado e insira o seu texto")


root = Tk()
root.geometry("1024x600")
root.title('OceanCript')
Application(root)
root.mainloop()
