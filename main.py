#----------------------- By GalTech UNC 2022---------------
#Tableau des charges :
#Niveau 1: Fait en entier
#Niveau 2: Fait en entier
#Niveau 3: Fait en entier
#Niveau 4: Fait en entier
#Niveau 5: Fait en entier
#Niveau 6: Fait en entier

from msvcrt import getch
import os
from time import sleep
from tkinter.filedialog import askopenfilename, asksaveasfilename
from math import *

#----------------- Technical Function--------------------------
os.system("color")

def clear() -> None:
    """Supprime le contenu de la console

    Returns
    -------
    None
    """
    os.system("cls")

def colored(text: str, color: tuple[int,int,int]) -> str:
    """Retour le text entré de la couleur spécifié.

    Parameters
    ----------
    text : str
        le texte à colorer
    color : tuple[int,int,int]
        le code rgb

    Returns
    -------
    str :
        le texte colorer
    """
    return f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m{text}\x1b[0m"

def get_input(white_list: list | None = None, blacklist: list | None = None) -> str:
    """Renvoie la touche qui est appuyé parmie celle défini.

    Parameters
    ----------
    white_list : list | None
    black_list : list | None

    Return
    ------
    key : str
        La touche appuyé.
    """
    while True:
        base = getch()
        key = None
        if base == b'\x00' or base == b'\xe0':
            sub = getch()
            if sub == b'H':
                key = 'UP_KEY'

            elif sub == b'M':
                key = 'RIGHT_KEY'

            elif sub == b'P':
                key = 'DOWN_KEY'

            elif sub == b'K':
                key = 'LEFT_KEY'
            
            elif sub == b'Q':
                key = 'PAGEDOWN_KEY'

            elif sub == b'I':
                key = 'PAGEUP_KEY'
            elif sub == b'S':
                key = 'DEL_KEY'

        elif base == b'\r':
            key = 'RETURN_KEY'
        elif base == b'\x08':
            key = 'BACK_KEY'
        elif base == b'\x1b':
            key = 'ESC_KEY'
        elif base == b'\t':
            key = 'TAB_KEY'
        else:
            try:
                base = base.decode("utf-8")
                if base in "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn+-/*=1234567890. ":
                    key = f"{base}_KEY"
            except:
                pass

        if not white_list==None:
            if key in white_list:
                return key
        elif not blacklist==None:
            if not key in blacklist:
                return key
        elif not key==None:
            return key

def int_to_ch(nb: int) -> str:
    """La nb ème lettre de l'alphabet.

    Parameters
    ----------
    nb : int

    Return
    ------
    ch : str
    """
    ch = ALPHA[nb]
    return ch

def show_titre() -> None:
    """Affiche un titre

    Return
    ------
    None
    """
    print("         Pybleau by GalTech\n")

def centrage(text: str, longueur: int, remplacement: str = " ") -> str:
    """Centre le texte avec des espaces sur une longueur fixée en nombre de caractères.

    Si la longueur est inferieur a la longueur du text, renvoie les longueur premier caractère du texte.
    Si le nombre l'espace à gauche du texte est inférieur à celui de droite (nombre d'espaces impair), alors l'espace en trop est mis à gauche.

    Parameters
    ----------
    texte : str
        le texte à centrer
    longueur : int
        la longueur totale du texte à obtenir

    Returns
    -------
    str
        le texte centré
    """
    text=str(text)
    if len(text)>=longueur:
        return text[:longueur]
    else:
        if (longueur-len(text))%2 == 0:
            decal_left=(longueur-len(text))//2
        else:
            decal_left=(longueur-len(text))//2+1
        return (f"{remplacement*decal_left}{text}{remplacement*(longueur-len(text)-decal_left)}")

def print_horisontal(list_menu: list, index: int, inactive: list = []) -> None:
    """Affiche une liste de textes horizontalement en mettant le texte situé à un certain indice en évidence et ceux contenu dans la liste inactive en rouge.

    Parameters
    ----------
    list_menu : str
        la liste des textes à afficher
    index : int
        index du texte à mettre en évidence
    inactive : list


    Returns
    -------
    None
    """
    debut="" 
    for menu in list_menu[:index]:
        if menu in inactive:
            debut+="\x1b[0;31;40m "+menu+" \x1b[0m"
        else:
            debut+=f" {menu} "
    fin=""
    for menu in list_menu[index+1:]:
        if menu in inactive:
            fin+="\x1b[0;31;40m "+menu+" \x1b[0m"
        else:
            fin+=f" {menu} "

    ligne =  debut+"\x1b[0;30;47m "+list_menu[index]+" \x1b[0m"+ fin
    print(ligne)

def print_cell_action(postion: tuple[int,int], selected: bool) -> None:
    """Affiche une liste d'action selon la position et l'état de selected.

    Parameters
    ----------
    position : tuple
        position de la cellule
    selected : bool
        état de selection de la cellule

    Returns
    -------
    None
    """
    if postion==(-1,-1):
        if selected:
            print("Action : Suppr -> tout supprimer")
        else:
            print("Action : Entrer -> tout selectionner")
    elif postion[0]==-1:
        if selected:
            print("Action : Suppr -> supprimer la ligne")
        else:
            print("Action : Entrer -> selectionner la ligne")
    elif postion[1]==-1:
        if selected:
            print("Action : Suppr -> supprimer la colonne")
        else:
            print("Action : Entrer -> selectionner la colonne")
    else:
        print("Action : Entrer -> modifier la cellule")

def is_nb(text: str) -> bool:
    """Détecte sur un str est un nombre.

    Parameters
    ----------
    text : str
        text à tester

    Returns
    -------
    bool
    """
    try:
        text=float(text)
        return True
    except:
        return False

def is_ref(text: str) -> bool:
    """Détecte si un str est une reference.

    Parameters
    ----------
    text : str
        text à tester

    Returns
    -------
    bool
    """
    if text[0] in ALPHA:
        return is_nb(text[1:]) and text[1:]!=""
    else:
        return False

def ref_to_pos(ref: str) -> tuple[int, int]:
    """Convertie une reference en ça coordonné.

    Parameters
    ----------
    ref : str
        text à convertir

    Returns
    -------
    tuple[int, int]
    """
    return (int(ref[1:])-1,ALPHA.index(ref[0]))

def get_ref(expression: str) -> list[str]:
    """Détecte toute les reference d'un text.

    Parameters
    ----------
    expression : str
        text à traiter

    Returns
    -------
    list[str]
    """
    all_ref=[]
    for i,ch in enumerate(expression):
        if ch in ALPHA:
            nbs=""
            for nb in expression[i+1:]:
                if is_nb(nb):
                    nbs+=nb
                else:
                    break
            if nbs!="":
                all_ref.append(f"{ch}{nbs}")
    return all_ref
             
#---------------------------- Main ----------------------------
COLONNE=10
LIGNE=10
MIN_LIGNE=1
MAX_LIGNE=14
MIN_COLONNE=1
MAX_COLONNE=14

CELL_SIZE=6
MIN_CELL_SIZE=1
MAX_CELL_SIZE=20
DEFAULT_SIZE=CELL_SIZE

CSV_SEPARATOR=";"
ALPHA="ABCDEFGHIJKLMNOPQRSTUVYXYZ"

class Cell:
    def __init__(self) -> None:
        """Initialisation de la class.

        Parameters
        ----------
        self : Cell

        Returns
        -------
        None
        """
        self.content=""

    def get_value(self) -> float | str:
        """Retourn la valeur de la cellule.
            Calcule la valeur des cellules en reference puis lui même.
        Parameters
        ----------
        self : Cell

        Returns
        -------
        float | str
        """
        if self.content!="":
            if self.content[0]=="=":
                all_ref=get_ref(self.content[1:])
                for ref in all_ref:
                    try:
                        exec(f"{ref}=table.get_cell(ref_to_pos(ref)).get_value()")
                    except Exception as error:
                        if type(error)==RecursionError:
                            return "#RefErr"

                try:
                    result = str(eval(self.content[1:]))
                    if is_nb(result) and all([type(ref)==float for ref in all_ref]):
                        if float(result) == int(float(result)):
                            result = int(float(result))
                        else:
                            result = float(result)

                except Exception as error:
                    if type(error)==ZeroDivisionError:    
                        result="#DIV/0"
                    elif type(error)==TypeError:
                        result="#ValErr"
                    elif type(error)==NameError:
                        result=f"#Ref Not Found {self.content[1:]}"
                    else:  
                        result="#Err"
                        raise error
            else:
                result=self.content
        else:
            result=self.content
        return result

    def get_content(self) -> str:
        """Retour le contenu de la cellule.

        Parameters
        ----------
        self : Cell

        Returns
        -------
        str
        """
        return self.content

    def set_content(self, new_content: str) -> None:
        """Défini le contenu de la cellule.

        Parameters
        ----------
        self : Cell
        new_content : str
            le nouveau contenu

        Returns
        -------
        None
        """
        self.content=new_content

class Tableau:
    def __init__(self, cells: list[list[Cell]], colonne: int, ligne:int, colonne_size: int) -> None:
        """Initialisation de la class.

        Parameters
        ----------
        self : Tableau
        cells : list
        colonne : int
        ligne : int
        colonne_size : int

        Returns
        -------
        None
        """
        self.all_cell=cells
        self.colonne_size=[colonne_size for j in range(colonne)]
        self.colonne_lock=[False for j in range(colonne)]
        self.colonne=colonne
        self.ligne=ligne

    def show_table(self, evidance: list = []) -> None:
        """Affiche le tableau en mettant en evidance les cellule au coordonées qui sont dans la liste evidance.

        Parameters
        ----------
        self : Tableau
        evidance : list
            list de tuples (coordonées)

        Returns
        -------
        None
        """
        for i in range(-1,self.ligne):
            if i==-1:
                if (-1,-1) in evidance:
                    print(f"\x1b[0;30;47m{centrage(' ',2)}\x1b[0m|", end="")
                else:
                    print(f"{centrage(' ',2)}|", end="")
            else:
                if (i,-1) in evidance:
                    print(f"\x1b[0;30;47m{centrage(str(i+1),2)}\x1b[0m|", end="")
                else:
                    print(f"{centrage(str(i+1),2)}|", end="")
            for j in range(self.colonne):
                if i==-1:
                    if (i,j) in evidance:
                        print(f"\x1b[0;30;47m{centrage(int_to_ch(j),self.colonne_size[j],'_')}\x1b[0m|", end="")
                    else:
                        print(f"{centrage(int_to_ch(j),self.colonne_size[j],'_')}|", end="")
                else:
                    if (i,j) in evidance:
                        print(f"\x1b[0;30;47m{centrage(self.get_cell((i,j)).get_value(),self.colonne_size[j],'_')}\x1b[0m|", end="")
                    else:
                        print(f"{centrage(self.get_cell((i,j)).get_value(),self.colonne_size[j],'_')}|", end="")
            print("")

    def pos_is_valide(self, position: tuple[int, int]) -> bool:
        """Test si position est est dans les limites du tableau.
            
        Parameters
        ----------
        self : Tableau
        position : tuple

        Returns
        -------
        bool
        """
        return position[0]>=0 and position[1]>=0 and position[0]<self.ligne and position[1]<self.colonne

    def add_colonne(self, position:int) -> None:
        """Ajoute une colonne.
            Ajoute si la limite n'est pas dépassé.
        Parameters
        ----------
        self : Tableau
        position : int
        
        Returns
        -------
        None
        """
        if self.colonne<MAX_COLONNE:
            for i in range(self.ligne):
                for j in range(self.colonne):
                    cell_content=self.get_cell((i,j)).content
                    if len(cell_content)>0:
                        if cell_content[0]=="=":
                            all_ref=get_ref(cell_content[1:])
                            for ref in all_ref:
                                if ref[0]>=int_to_ch(position):
                                    self.all_cell[i][j].content=self.all_cell[i][j].content.replace(ref,f"{ALPHA[ALPHA.index(ref[0])+1]}{ref[1:]}")
                self.all_cell[i].insert(position,Cell())
            self.colonne_size.insert(position,cell_size)
            self.colonne_lock.insert(position,False)
            self.colonne+=1
    
    def add_ligne(self, position: int) -> None:
        """Ajoute une ligne.
            Ajoute si la limite n'est pas dépassé.
        Parameters
        ----------
        self : Tableau
        position : int
        
        Returns
        -------
        None
        """
        if self.ligne<MAX_LIGNE:
            if self.ligne>MIN_LIGNE:
                for i in range(self.ligne):
                    for j in range(self.colonne):
                        cell_content=self.get_cell((i,j)).content
                        if len(cell_content)>0:
                            if cell_content[0]=="=":
                                all_ref=get_ref(cell_content[1:])
                                for ref in all_ref:
                                    if float(ref[1:])>=float(position+1):
                                        self.all_cell[i][j].content=self.all_cell[i][j].content.replace(ref,f"{ref[0]}{int(float(ref[1:])+1)}")
            self.all_cell.insert(position,[Cell() for j in range(self.colonne)])
            self.ligne+=1

    def del_colonne(self, position: int) -> None:
        """Supprime une colonne.
            Supprime si la limite n'est pas dépassé.
        Parameters
        ----------
        self : Tableau
        position : int
        
        Returns
        -------
        None
        """
        if self.colonne>MIN_COLONNE:
            for i in range(self.ligne):
                for j in range(self.colonne):
                    cell_content=self.get_cell((i,j)).content
                    if len(cell_content)>0:
                        if cell_content[0]=="=":
                            all_ref=get_ref(cell_content[1:])
                            for ref in all_ref:
                                if ref[0]>int_to_ch(position):
                                    self.all_cell[i][j].content=self.all_cell[i][j].content.replace(ref,f"{ALPHA[ALPHA.index(ref[0])-1]}{ref[1:]}")
                self.all_cell[i].pop(position)
            self.colonne_size.pop(position)
            self.colonne_lock.pop(position)
            self.colonne-=1

    def del_ligne(self, position: int) -> None:
        """Supprime une ligne.
            Supprime si la limite n'est pas dépassé.
        Parameters
        ----------
        self : Tableau
        position : int
        
        Returns
        -------
        None
        """
        if self.ligne>MIN_LIGNE:
            for i in range(self.ligne):
                for j in range(self.colonne):
                    cell_content=self.get_cell((i,j)).content
                    if len(cell_content)>0:
                        if cell_content[0]=="=":
                            all_ref=get_ref(cell_content[1:])
                            for ref in all_ref:
                                if float(ref[1:])>float(position+1):
                                    self.all_cell[i][j].content=self.all_cell[i][j].content.replace(ref,f"{ref[0]}{int(float(ref[1:])-1)}")
            self.all_cell.pop(position)
            self.ligne-=1

    def add(self, position: tuple, decal: bool = False) -> None:
        """Loby d'ajout de ligne/colonne.

        Parameters
        ----------
        self : Tableau
        position : tuple
        decal : bool

        Returns
        -------
        None
        """
        if position[0]==-1:
            self.add_colonne(position[1]+ (1 if decal else 0))
        else:
            self.add_ligne(position[0]+ (1 if decal else 0))

    def suppr(self, position: tuple) -> None:
        """Loby de suppression de ligne/colonne.

        Parameters
        ----------
        self : Tableau
        position : tuple

        Returns
        -------
        None
        """
        if position[0]==-1:
            if self.colonne>1:
                self.del_colonne(position[1])
            else:
                return False
        else:
            if self.ligne>1:
                self.del_ligne(position[0])
            else:
                return False
        return True

    def get_cell(self, position: tuple) -> Cell:
        """Retourn la cellule à cette position.

        Parameters
        ----------
        self : Tableau
        position : tuple

        Returns
        -------
        Cell
        """
        return self.all_cell[position[0]][position[1]]

    def get_data(self) -> list:
        """Retourn la liste de donné qui seront utiliser pour sauvgarder.

        Parameters
        ----------
        self : Tableau

        Returns
        -------
        list
        """
        data=[]
        for i in range(self.ligne):
            ligne=""
            for j in range(self.colonne):
                ligne+=str(self.get_cell((i,j)).get_value())+CSV_SEPARATOR
            data.append(ligne[:-1]+"\n")
        return data

    def get_selected(self, selected: bool, position: tuple) -> list:
        """Retourn la liste des coordonées des cellules selon la position.

        Parameters
        ----------
        self : Tableau
        selected : bool
        position : tuple

        Returns
        -------
        list
        """
        selected_cell=[]
        if selected:
            if position==(-1,-1):
                for i in range(self.ligne):
                    for j in range(self.colonne):
                        selected_cell.append((i,j))
            else:
                if position[0]==-1:
                    for i in range(self.ligne):
                        for j in range(self.colonne):
                            if j==position[1]:
                                selected_cell.append((i,j))
                else:
                    for i in range(self.ligne):
                        for j in range(self.colonne):
                            if i==position[0]:
                                selected_cell.append((i,j))
        return selected_cell

    def edit(self) -> None:
        """Menu d'édition.

        Parameters
        ----------
        self : Tableau

        Returns
        -------
        None
        """
        position=(0,0)
        run=True
        selected=False
        while run:
            clear()
            show_titre()
            selected_cell=[]
            if position[0] >-1 and position[1] >-1:
                print(f"   {int_to_ch(position[1])}{position[0]+1} : {self.get_cell(position).get_content()}")
            else:
                selected_cell+=self.get_selected(selected,position)     
                print("")
            self.show_table([position]+selected_cell)
            print_cell_action(position,selected)
            key=get_input(white_list=["UP_KEY","DOWN_KEY","LEFT_KEY","RIGHT_KEY","RETURN_KEY","BACK_KEY","ESC_KEY","DEL_KEY","TAB_KEY"])
            if key=="DOWN_KEY" or key=="RETURN_KEY":
                if (key=="RETURN_KEY" and position[0] >-1 and position[1] >-1) or key=="DOWN_KEY":
                    if key=="RETURN_KEY":
                        new_data=input(f"{int_to_ch(position[1])}{position[0]+1} : ")
                        if CSV_SEPARATOR in new_data:
                            print(f"Vous ne pouvez pas utiliser ' {CSV_SEPARATOR} '.")
                            input("Entrer pour continuer ")
                        else:
                            table.get_cell(position).set_content(new_data)
                    position = position if position[0]==self.ligne-1 else (position[0]+1,position[1])
                    if selected:
                        selected=False
                else:
                    if position==(-1,-1):
                        ref=0
                    elif position[0]==-1:
                        ref=1
                    elif position[1]==-1:
                        ref=2
                    position = self.select_menu(ref,position)
            elif key=="UP_KEY":
                position = position if position[0]==-1 else (position[0]-1,position[1])
            elif key=="RIGHT_KEY" or key=="TAB_KEY":
                position = position if position[1]==self.colonne-1 else (position[0],position[1]+1)
            elif key=="LEFT_KEY":
                position = position if position[1]==-1 else (position[0],position[1]-1)
            elif key=="ESC_KEY":
                run=False
            elif key=="DEL_KEY":
                if position[0] >-1 and position[1] >-1:
                    self.get_cell(position).set_content("")
            elif key=="BACK_KEY":
                self.get_cell(position).set_content(self.get_cell(position).get_content()[:-1])
    
    def select_menu(self, type_selec:int, position: tuple) -> None:
        """Sous-menu d'édition.

        Parameters
        ----------
        self : Tableau
        type_selec : int
        position : tuple

        Returns
        -------
        None
        """
        index=0
        run=True
        list_menu=["VIDER","AFFICHAGE","RETOUR"]
        if type_selec==1:
            list_menu=["VIDER","INSERER","SUPPRIMER","AFFICHAGE","RETOUR"]
        elif type_selec==2:
            list_menu=["VIDER","INSERER","SUPPRIMER","RETOUR"]
        while run:
            clear()
            show_titre()
            print("")
            self.show_table([position]+self.get_selected(True,position))
            print_horisontal(list_menu=list_menu,index=index)
            key=get_input(white_list=["LEFT_KEY","RIGHT_KEY","RETURN_KEY","BACK_KEY","DEL_KEY","ESC_KEY"])
            if key=="RIGHT_KEY":
                index = 0 if index==len(list_menu)-1 else index+1
            elif key=="LEFT_KEY":
                index = len(list_menu)-1 if index==0 else index-1
            if key=="BACK_KEY" or (key=="RETURN_KEY" and list_menu[index]=="VIDER"):
                if position==(-1,-1):
                    for i in range(self.ligne):
                        for j in range(self.colonne):
                            self.get_cell((i,j)).set_content("")
                elif position[0]==-1:
                    for i in range(self.ligne):
                        self.get_cell((i,position[1])).set_content("")
                elif position[1]==-1:
                    for j in range(self.colonne):
                        self.get_cell((position[0],j)).set_content("")
                else:
                    self.get_cell(position).set_content("")
            if key=="DEL_KEY" or (key=="RETURN_KEY" and list_menu[index]=="SUPPRIMER"):
                pass

            if key=="RETURN_KEY":
                if list_menu[index]=="AFFICHAGE":
                    clear()
                    show_titre()
                    print("")
                    self.show_table([(-2,-2)]+self.get_selected(True,position))
                    print_horisontal(list_menu=list_menu,index=index)
                    if type_selec==0:
                        print_horisontal(list_menu=["REINITIALISER TAILLES"],index=0)
                        key=get_input(white_list=["RETURN_KEY","ESC_KEY"])
                        if key=="RETURN_KEY":
                            self.colonne_size=[cell_size for j in range(self.colonne)]
                    if type_selec==1:
                        run2=True
                        old=self.colonne_size[position[1]]
                        index2=0
                        while run2:
                            clear()
                            show_titre()
                            print("")
                            self.show_table([(-2,-2)]+self.get_selected(True,position))
                            print_horisontal(list_menu=list_menu,index=index)
                            print_horisontal(list_menu=["MODIFIER TAILLE","REINITIALISER TAILLE"],index=index2)
                            key=get_input(white_list=["LEFT_KEY","RIGHT_KEY","RETURN_KEY","ESC_KEY"])
                            if key=="RIGHT_KEY":
                                index2 = index2  if index2 == 1 else index2 +1
                            if key=="LEFT_KEY":
                                index2  = index2  if index2 == 0 else index2 -1
                            if key=="ESC_KEY":
                                run2=False
                            if key=="RETURN_KEY":
                                if index2==0:
                                    self.colonne_lock[position[1]]=True
                                    run3=True
                                    while run3:
                                        clear()
                                        show_titre()
                                        print("")
                                        self.show_table([(-2,-2)]+self.get_selected(True,position))
                                        print_horisontal(list_menu=list_menu,index=index)
                                        print_horisontal(list_menu=["MODIFIER TAILLE","REINITIALISER TAILLE"],index=index2)
                                        print(f"< {self.colonne_size[position[1]]} >")
                                        key=get_input(white_list=["LEFT_KEY","RIGHT_KEY","RETURN_KEY","ESC_KEY"])
                                        if key=="RIGHT_KEY":
                                            self.colonne_size[position[1]] = self.colonne_size[position[1]] if self.colonne_size[position[1]]==MAX_CELL_SIZE else self.colonne_size[position[1]]+1
                                        if key=="LEFT_KEY":
                                            self.colonne_size[position[1]] = self.colonne_size[position[1]] if self.colonne_size[position[1]]==MIN_CELL_SIZE else self.colonne_size[position[1]]-1
                                        if key=="ESC_KEY":
                                            self.colonne_size[position[1]]=old
                                            run3=False
                                        if key=="RETURN_KEY":
                                            run3=False
                                    key=""
                                else:
                                    self.colonne_lock[position[1]]=False
                                    self.colonne_size[position[1]]=cell_size
                        key=""
                if list_menu[index]=="INSERER":
                    run2=True
                    index2=0
                    list_menu2=["AVANT","APRES"]
                    while run2:
                        clear()
                        show_titre()
                        print("")
                        self.show_table([(-2,-2)]+self.get_selected(True,position))
                        print_horisontal(list_menu=list_menu,index=index)
                        print_horisontal(list_menu=list_menu2,index=index2)
                        key=get_input(white_list=["LEFT_KEY","RIGHT_KEY","RETURN_KEY","ESC_KEY"])
                        if key=="RIGHT_KEY":
                            index2 = 0 if index2==len(list_menu2)-1 else index2+1
                        if key=="LEFT_KEY":
                            index2 = len(list_menu2)-1 if index==0 else index2-1
                        if key=="ESC_KEY":
                            run2=False
                        if key=="RETURN_KEY":
                            table.add(position,False if index2==0 else True)
                            run2=False
                    key=""

                if list_menu[index]=="SUPPRIMER":
                    if table.suppr(position):
                        if position[0]==-1:
                            if position[1]==table.colonne:
                                position=(position[0],position[1]-1)
                        if position[1]==-1:
                            if position[0]==table.ligne:
                                position=(position[0]-1,position[1])

            if key=="ESC_KEY" or (key=="RETURN_KEY" and list_menu[index]=="RETOUR"):
                run=False
        return position

def load_table(data: list[list] | None = None) -> Tableau:
    """Retourn un tableau avec toute les données entrées.

        Parameters
        ----------
        data: list[list] list[[data A1,data B1],
                              [data A2,data B2],
                              [data A3,data B3]]

        Returns
        -------
        Tableau
        """
    if data==None or data==[]:
        new_table = Tableau([[Cell() for j in range(COLONNE)] for i in range(LIGNE)],COLONNE,LIGNE,cell_size)
    else:
        size_colonne=len(data)
        size_ligne=max([len(ligne) for ligne in data])
        new_table = Tableau([[Cell() for j in range(size_ligne)] for i in range(size_colonne)],size_ligne,size_colonne,cell_size)
        corupt=False
        for i in range(new_table.ligne):
            for j in range(new_table.colonne):
                try:
                    new_table.get_cell((i,j)).set_content(data[i][j].replace("\n",""))
                except:
                    if not corupt:
                        print(colored("Fichier corrompu: Il est possible que le tableau généré soit différent de celui attendu",(222,0,0)))
                        corupt=True
                        sleep(3)
                    pass
    return new_table

def save_table(data: list[str], path: str | None = None) -> None:
    """Sauvgarde.

        Parameters
        ----------
        data : list[str]
        path : str | None

        Returns
        -------
        None
        """
    if path==None:
        path=asksaveasfilename(filetypes=[("csv files", "*.csv")], title="Save as")
        if path=="":
            return

        if path[-4:]!=".csv":
            path+=".csv"
    try:
        file = open(path, "x", encoding="utf-8")
    except:
        file = open(path, "w", encoding="utf-8") 
    new_data=""
    for ligne in data:
        new_data+=ligne
    file.write(new_data)
    file.close()

def menu() -> None:
    """Main Menu.

        Parameters
        ----------

        Returns
        -------
        None
        """
    global cell_size
    global table
    cell_size=CELL_SIZE
    index=0
    list_menu=["NEW","OPEN","EDIT","SAVE","SAVE AS","OPTION","QUIT"]
    loaded=False
    run=True
    dir=None
    while run:
        clear()
        show_titre()
        if loaded:
            table.show_table([(-2,-2)])
            print_horisontal(list_menu, index)
        else:
            print_horisontal(list_menu, index, inactive=["EDIT","SAVE","SAVE AS"])
        key = get_input(white_list=["LEFT_KEY","RIGHT_KEY","RETURN_KEY"])
        if key=="RIGHT_KEY":
            index = 0 if index==len(list_menu)-1 else index+1
        if key=="LEFT_KEY":
            index = len(list_menu)-1 if index==0 else index-1
        if key=="RETURN_KEY":
            if list_menu[index]=="NEW":
                table=load_table()
                dir=None
                loaded=True
            
            if list_menu[index]=="OPEN":
                dir=askopenfilename(filetypes=[("csv files", "*.csv")], title="Open")
                if dir!="":
                    with open(dir,encoding="utf-8") as file:
                        data=file.readlines()
                    data=[ligne.split(CSV_SEPARATOR) for ligne in data]
                    loaded=True
                    table = load_table(data)
                    index+=1
            elif list_menu[index]=="EDIT":
                if loaded:
                    table.edit()

            elif list_menu[index]=="SAVE":
                if loaded:
                    save_table(table.get_data(),dir)

            elif list_menu[index]=="SAVE AS":
                if loaded:
                    save_table(table.get_data())

            elif list_menu[index]=="OPTION":
                run2=True
                old=cell_size
                while run2:
                    clear()
                    show_titre()
                    if loaded:
                        table.show_table([(-2,-2)])
                        print_horisontal(list_menu, index)
                    else:
                        print_horisontal(list_menu, index, inactive=["EDIT","SAVE","EXPORT"])
                    print(f"< {cell_size} >")
                    key=get_input(white_list=["LEFT_KEY","RIGHT_KEY","RETURN_KEY","ESC_KEY"])
                    if key=="RIGHT_KEY":
                        cell_size = cell_size if cell_size==MAX_CELL_SIZE else cell_size+1
                    if key=="LEFT_KEY":
                        cell_size = cell_size if cell_size==MIN_CELL_SIZE else cell_size-1
                    if key=="ESC_KEY":
                        cell_size=old
                        run2=False
                    if key=="RETURN_KEY":
                        run2=False
                    if loaded:
                        table.colonne_size=[cell_size if not table.colonne_lock[j] else table.colonne_size[j] for j in range(table.colonne) ]

            elif list_menu[index]=="QUIT":
                clear()
                run=False

menu()