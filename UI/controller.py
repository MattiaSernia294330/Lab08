import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()
        self._nerc_id=None
        self._maxH=None
        self._maxY=None

    def handleWorstCase(self, e):
        if self._nerc_id is None or self._maxH is None or self._maxY is None:
            self._view.create_alert("non hai alcuni dati")
            return
        else :
            lista=[]
            result=self._model.WorstCase(self._nerc_id, self._maxY, self._maxH)
            for i in range(len(result)):
                somma=0
                for element in result[i]:
                    somma+=element._customers_affected
                lista.append(somma)
            risultato=result[lista.index(max(lista))]
            somma_ore=0
            for element in risultato:
                somma_ore+=(element._date_event_finished - element._date_event_began).total_seconds()/ 3600
            self._view._txtOut.controls.append(ft.Text(f"la somma delle ore di disservizio è : {somma_ore}"))
            self._view._txtOut.controls.append(ft.Text(f"gli utenti colpiti sono : {max(lista)}"))
            for element in risultato:
                self._view._txtOut.controls.append(ft.Text(f"{element}"))
            self._view.update_page()


    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(text=n,key=n._id,  on_click=self.read_nerc))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
    def read_nerc(self,e):
        self._nerc_id = e.control.key
    def read_maxH(self,e):
        self._maxH = e.control.value
    def read_maxY(self,e):
        self._maxY = e.control.value