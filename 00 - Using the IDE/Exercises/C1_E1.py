'''En la carpeta Exercises crear un nuevo archivo llamado C1_E1_done.py, agregarlo al repositorio, copiar el contenido de este archivo
y trabajar en el'''



'''El siguiente pedazo de código contiene un error, resolverlo para poder ejecutar correctamente el script'''

variable1=100
if variable1:
print(variable1)
print(variable1)

'''Debugguear el siguiente codigo, durante el debugging modificar el contenido de la variable x desde la consola de debug
El valor que debe imprimir es
a) Primer corrida: 100
b) Segunda corrida: Hola
'''

x=1
print(x)

'''Debugguear el siguiente código solo deteniendonos cuando la variable value contenga el valor 200
'''

for value in range(400):
    print(value)


'''Renombrar todas las apariciones de la variable 'nombreDato' a 'nombreInstrumento' utilizando la funcionalidad refactor'''

tickers=["GGAL","YPFD","SUPV","PAMP"]
nombreDato = "GGAL"
if nombreDato in tickers:
    print(nombreDato)
nombreDato = tickers[2]


'''Resolver el siguiente error'''
print(nombreDato+otroDato)


'''Utilizar el evaluate expression para conocer el contenido de la siguiente variable mientras se debuguea'''
from math import pi

#ver el resultado de la siguiente expresion
pi*1000



'''Probar mover bloques de codigo dentro y fuera del if con CTRL+SHIFT+ flechas'''

tickers=["GGAL","YPFD","SUPV","PAMP"]
nombreDato = "GGAL"
if nombreDato in tickers:
    print(nombreDato)
nombreDato = tickers[2]

#transformar el siguiente texto en un string solo seleccionandolo y apretando "

'''comentar y descomentar bloques completos de código usando ctrl+/ '''
# print("mi nombre es")
# print("me gusta programar en python")
# print("espero aprender algo en este curso")




'''
Editing I
    ctrl+[SPACE]    Complete code
    shift+ctrl+↵    Complete Current Statement
    ctrl+I          Implement base interface/class methods in the current class
    ctrl+O          Override base class methods in the current class
    ctrl+P          Show parameters of the method call at caret
    alt+ctrl+T      Surround selected code fragment with if, while, try/catch or other construct

Editing II
    alt+ctrl+I      Indent current line or selected block according to the code style settings
    ctrl+C          Copy to clipboard
    ctrl+X          Cut to clipboard
    ctrl+V          Paste from clipboard
    shift+ctrl+V    Paste from recent clipboards
    shift+alt+ctrl+VPaste without formatting, autoimport, literal escaping etc.
    alt+ctrl+L      Reformat code
    alt+↵           Show Intention Actions
    shift+TAB       Unindent Selection

Editing III
    ctrl+Y          Delete Line
    ctrl+           DELDelete to Word End
    ctrl+BACKSPACE  Delete to Word Start
    ctrl+D          Duplicate Line or Block
    ctrl+=          Expand folding region at caret
    shift+ctrl+=    Expand all folding regions
    shift+ctrl+J    Join Lines
    ctrl+↵          Split Line
    shift+↵         Start New Line
    alt+ctrl+↵      Start New Line Before Current
    shift+ctrl+U    Toggle Case

Running / Debugging
    shift+F10       Run
    shift+F9        Debug
    alt+5           Activate Debug window
    shift+alt+F9    Choose and debug configuration
    alt+F8          Evaluate arbitrary expression
    F9              Resume program execution
    shift+ctrl+F10  Run context configuration
    alt+F9          Run to the line where the caret is
    shift+alt+F10   Choose and run configuration
    shift+F7        Step into the particular method
    F7              Step to the next line executed
    shift+F8        Step to the first line executed after returning from this method
    F8              Step to the next line in this file
    shift+ctrl+F8   View and manage all breakpoints and watchpoints

Navigation I
    ctrl+B          Navigate to the declaration of the symbol at caret
    ctrl+0          Go to Bookmark 0
    ctrl+1          Go to Bookmark 1
    ctrl+2          Go to Bookmark 2
    ctrl+3          Go to Bookmark 3
    ctrl+4          Go to Bookmark 4
    alt+ctrl+F4     Open image in external editor
    alt+HOME        Jump to Navigation Bar
    F4              Open editor for the selected item and give focus to it
    ctrl+E          Show list of recently viewed files
    shift+ctrl+E    Show list of recently changed files
    alt+ctrl+HOME   Navigate to one of the related or linked files
    alt+RIGHT       Activate next tab
    shift+alt+RIGHT Select Next Tab in multi-editor file
    alt+LEFT        Activate previous tab
    shift+alt+LEFT  Select Previous Tab in multi-editor file

Navigation II
    alt+ctrl+H      Browse call hierarchy for the selected method
    ctrl+5          Go to Bookmark 5
    ctrl+6          Go to Bookmark 6
    ctrl+7          Go to Bookmark 7
    ctrl+8          Go to Bookmark 8
    ctrl+9          Go to Bookmark 9
    alt+ctrl+B      Navigate to the implementation of class or method
    shift+ctrl+BACKSPACEMove through the most recent change points
    shift+ctrl+H    Browse method hierarchy for the selected method
    F2              Navigate to the next highlighted error in the active editor
    shift+F2        Navigate to the previous highlighted error in the active editor
    ctrl+U          Navigate to the declaration of the method that current method overrides or implements
    shift+ctrl+0    Toggle Bookmark 0
    shift+ctrl+1    Toggle Bookmark 1
    shift+ctrl+2    Toggle Bookmark 2
    shift+ctrl+3    Toggle Bookmark 3
    ctrl+F11        Toggle Bookmark With Mnemonic
    ctrl+H          Browse hierarchy for the selected class

Navigation III
    ctrl+]          Move Caret to Code Block End
    shift+ctrl+]    Move Caret to Code Block End with Selection
    ctrl+[          Move Caret to Code Block Start
    shift+ctrl+[    Move Caret to Code Block Start with Selection
    shift+END       Move Caret to Line End with Selection
    shift+HOME      Move Caret to Line Start with Selection
    shift+ctrl+RIGHT    Move Caret to Next Word with Selection
    ctrl+HOME       Move Caret to Text Start
    shift+alt+DOWN  Move selected lines one line down
    shift+alt+UP    Move selected lines one line up
    F7              Move to the Next Difference
    shift+F7        Move to the previous difference

Refactoring
    shift+F5        Create a copy of the selected class, file or directory in the same package/directory
    alt+ctrl+C      Replace selected expression with a constant
    shift+alt+ctrl+CCopy reference to selected class, method or function
    F5              Create a copy of the selected class
    alt+ctrl+N      Inline the selected method or variable
    alt+ctrl+M      Turn the selected code fragment into a method
    F6              Move the selected class, method, package or static member to another package or class and correct all references
    alt+ctrl+P      Turn the selected expression into method parameter
    shift+F6        Rename the selected symbol and correct all references
    alt+DEL         Delete the selected class, method or field, checking for usages
    alt+ctrl+J      Surrounds the selection with one of the template
    alt+ctrl+V      Put a result of the selected expression into a variable
'''
