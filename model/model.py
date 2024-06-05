from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()
        self._set=[]



    def WorstCase(self, nerc, maxY, maxH):
        lista=DAO.getAllEvents(nerc)
        self._solBest = []
        self.ricorsione([],maxY,maxH,lista)
        return self._solBest

    def ricorsione(self, parziale, maxY, maxH, pos):
        somma = 0

        for i in range(len(parziale)):
            somma += (parziale[i]._date_event_finished - parziale[i]._date_event_began).total_seconds()/ 3600
        if somma > float(maxH):
            parziale.pop(-1)
            if len(parziale) > 0 and set not in self._set:
                self._solBest.append(parziale)
                print(parziale)
            return
        if len(pos)==0:
            if set not in self._set:
                self._solBest.append(parziale)
                print(parziale)
            return
        else:
            for item in range(len(pos)):
                nuovo_parziale=list(parziale)
                nuovo_parziale.append(pos[item])
                nuovo_pos=list(pos[item+1:len(pos)])
                if self.possibile(nuovo_parziale, maxY):
                    self.ricorsione(nuovo_parziale, maxY, maxH, nuovo_pos)

    def possibile(self, nuovo_parziale, maxY):
        for i in range(len(nuovo_parziale)-1):
            if abs(nuovo_parziale[-1]._date_event_began.year-nuovo_parziale[i]._date_event_began.year) > float(maxY):
                return False
        return True


    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc