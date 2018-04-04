from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Rectangle

from datetime import datetime

def clearAllFields(instance):
    for child in instance.parent.children:
        if child.__class__.__name__ == "TextInput":
            child.text = ""

class RequestFields(GridLayout):
    def __init__(self, intManager, **kwargs):
        super(RequestFields, self).__init__(**kwargs)
        self.opFields = intManager

        self.cols = 2

        self.add_widget(Label(text='The following user wants to:'))

        self.add_widget(Label(text='edit file1.txt'))

        accBtn = Button(text='Accept', font_size=14)
        accBtn.bind(on_press=self.acceptReq)
        self.add_widget(accBtn)

        rejBtn = Button(text='Reject', font_size=14)
        rejBtn.bind(on_press=self.rejectReq)
        self.add_widget(rejBtn)

    def acceptReq(self, instance):
        print("You accepted a request !");

    def rejectReq(self, instance):
        print("You rejected a request !");

class OperationsFields(GridLayout):
    def __init__(self, intManager, **kwargs):
        super(OperationsFields, self).__init__(**kwargs)
        self.intManager = intManager

        self.cols = 2

        inputExamples = Button(text='Show accepted input formats', font_size=14)
        inputExamples.bind(on_press=self.showInputExamples)
        self.add_widget(inputExamples)

        clearBtn = Button(text='Clear all fields', font_size=14)
        clearBtn.bind(on_press=clearAllFields)
        self.add_widget(clearBtn)

        createFiles = Button(text='Create   ====>', font_size=14)
        createFiles.bind(on_press=self.doCreateFiles)
        self.add_widget(createFiles)

        self.toCreateFiles = TextInput(multiline=True)
        self.add_widget(self.toCreateFiles)

        editFiles = Button(text='Edit   ====>', font_size=14)
        editFiles.bind(on_press=self.doEditFiles)
        self.add_widget(editFiles)

        self.toEditFiles = TextInput(multiline=True)
        self.add_widget(self.toEditFiles)

        deleteFiles = Button(text='Delete   ====>', font_size=14)
        deleteFiles.bind(on_press=self.doDeleteFiles)
        self.add_widget(deleteFiles)

        self.toDeleteFiles = TextInput(multiline=True)
        self.add_widget(self.toDeleteFiles)

        giveViewPriv = Button(text='Give view privilege   ====>', font_size=14)
        giveViewPriv.bind(on_press=self.doGiveViewPriv)
        self.add_widget(giveViewPriv)

        self.toGiveViewPriv = TextInput(multiline=True)
        self.add_widget(self.toGiveViewPriv)

        giveEditPriv = Button(text='Give edit privilege   ====>', font_size=14)
        giveEditPriv.bind(on_press=self.doGiveEditPriv)
        self.add_widget(giveEditPriv)

        self.toGiveEditPriv = TextInput(multiline=True)
        self.add_widget(self.toGiveEditPriv)

        removeViewPriv = Button(text='Remove view privilege   ====>', font_size=14)
        removeViewPriv.bind(on_press=self.doRemoveViewPriv)
        self.add_widget(removeViewPriv)

        self.toRemoveViewPriv = TextInput(multiline=True)
        self.add_widget(self.toRemoveViewPriv)

        removeEditPriv = Button(text='Remove edit privilege   ====>', font_size=14)
        removeEditPriv.bind(on_press=self.doRemoveEditPriv)
        self.add_widget(removeEditPriv)

        self.toRemoveEditPriv = TextInput(multiline=True)
        self.add_widget(self.toRemoveEditPriv)

        editPrivileges = Button(text='Show edit privileges', font_size=14)
        editPrivileges.bind(on_press=self.showEditPrivileges)
        self.add_widget(editPrivileges)

        viewPrivileges = Button(text='Show view privileges', font_size=14)
        viewPrivileges.bind(on_press=self.showViewPrivileges)
        self.add_widget(viewPrivileges)

        viewAReq = Button(text='View a request', font_size=14)
        viewAReq.bind(on_press=self.showAReq)
        self.add_widget(viewAReq)

        logOut = Button(text='Log  out', font_size=14)
        logOut.bind(on_press=self.logOutFunc)
        self.add_widget(logOut)

    def doCreateFiles(self, instance):
        print("You chose to create the following files: " + instance.parent.\
            toCreateFiles.text)

    def doEditFiles(self, instance):
        print("You chose to edit the following files: " + instance.parent.\
            toEditFiles.text)

    def doDeleteFiles(self, instance):
        print("You chose to delete the following files: " + instance.parent.\
            toDeleteFiles.text)

    def doGiveViewPriv(self, instance):
        print("You chose to give view privilege according to: " + instance.\
            parent.toGiveViewPriv.text)

    def doGiveEditPriv(self, instance):
        print("You chose to give edit privilege according to: " + instance.\
            parent.toGiveEditPriv.text)

    def doRemoveViewPriv(self, instance):
        print("You chose to remove view privilege according to: " + instance.\
            parent.toRemoveViewPriv.text)

    def doRemoveEditPriv(self, instance):
        print("You chose to remove edit privilege according to: " + instance.\
            parent.toRemoveEditPriv.text)

    def showInputExamples(self, instance):
        popup = Popup(
            title='Input format',
            content=TextInput(text='If you want to apply an operation on multiple files/users,'
                    + ' then concatenate their names using "," as a separator as it will be shown '
                    + 'in the following examples. Write between """ if you wish to operate on a file'
                    + ' which has an unusual name.\n\n'
                    + 'Here are some example inputs for '
                    + 'create, edit, delete:\n'
                    + '-> <example.in> yelds: <example.in> ;\n'
                    + '-> <example1.in,    example  2.in > yelds: <example1.in> ,<example  2.in> ;\n'
                    + '-> <exampl,e.in, "exampl,e.in"> yelds: <exampl> ,<e.in>, <exampl,e.in> .\n\n'
                    + 'For the operations that require a relation between users and file use: \n'
                    + '(<list_of_users1>, <list_of_files1>), (<list_of_users2>, <list_of_files2>).\n'
                    + 'The above lists have the same format as if you would input a list of files.',
                    disabled=True),
            size_hint=(None, None),
            size=(700, 400)
        )
        popup.open()

    def showEditPrivileges(self, instance):
        popup = Popup(
            title='Edit privileges',
            content=TextInput(text='file1.txt => MYSELF    file2.txt => Alex'
                + '\tfile3.txt => Vlad',
                disabled=True),
            size_hint=(None, None),
            size=(700, 400)
        )
        popup.open()

    def showViewPrivileges(self, instance):
        popup = Popup(
            title='View privileges',
            content=TextInput(text='file1.txt => [MYSELF, Radu, Ioan]\n'
                + 'file2.txt => [MYSELF]\n'
                + 'file3.txt => [Vlad]\n',
                disabled=True),
            size_hint=(None, None),
            size=(700, 400)
        )
        popup.open()

    def showAReq(self, instance):
        popup = Popup(
            title='Request',
            content=RequestFields(instance.parent),
            size_hint=(None, None),
            size=(700, 400)
        )
        popup.open()

    def logOutFunc(self, instance):
        clearAllFields(instance)
        instance.parent.intManager.clear_widgets()
        instance.parent.intManager.add_widget(instance.parent.intManager.\
            logInScreen)

class LoginScreen(GridLayout):
    def __init__(self, intManager,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.intManager = intManager

        self.cols = 2

        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        btn1 = Button(text='Log  in', font_size=14)
        btn1.bind(on_press=self.logInFunc)
        self.add_widget(btn1)

        clearBtn = Button(text='Clear all fields', font_size=14)
        clearBtn.bind(on_press=clearAllFields)
        self.add_widget(clearBtn)

    def logInFunc(self, instance):
        print("A log in request with u=<" + instance.parent.username.text +\
            "> and p=<" + instance.parent.password.text +">")

        # Comunicate with server and check if credentials are valid. Set
        # "loginInfoIsOk" to True if it is so, False otherwise.
        loginInfoIsOk = True

        if loginInfoIsOk == 1:
            clearAllFields(instance)
            instance.parent.intManager.clear_widgets()
            instance.parent.intManager.add_widget(instance.parent.intManager.\
                opScreen)
        else:
            popup = Popup(
                title='Error !',
                content=Label(text='Wrong username or password !'),
                size_hint=(None, None),
                size=(400, 400)
            )
            popup.open()

class InterfaceManager(BoxLayout):
    def __init__(self, **kwargs):
        super(InterfaceManager, self).__init__(**kwargs)
        self.col = 1
        self.logInScreen = LoginScreen(self)
        self.add_widget(self.logInScreen)

        self.opScreen = OperationsFields(self)

class MyApp(App):

    def build(self):
        return InterfaceManager(orientation='vertical')

if __name__ == '__main__':

    MyApp().run()
