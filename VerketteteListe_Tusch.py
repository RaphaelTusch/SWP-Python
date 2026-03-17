import random

class ListElement:
    def __init__(self, wert):
        self.wert = wert
        self.nextElem = None

    def setNextElem(self, nextElem):
        self.nextElem = nextElem

    def getNextElem(self):
        return self.nextElem

    def getWert(self):
        return self.wert


class EinfachVerketteteListe:
    def __init__(self):
        self.startElem = ListElement("Kopf")

    def addLast(self, wert):
        newElem = ListElement(wert)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)
    
    def addFirst(self, wert):
        newElem = ListElement(wert)
        firstElem = self.startElem.getNextElem()
        self.startElem.setNextElem(newElem)
        newElem.setNextElem(firstElem)

    def getLastElem(self):
        le = self.startElem
        while le.getNextElem() is not None:
            le = le.getNextElem()
        return le

    def laenge(self):
        count = 0
        le = self.startElem.getNextElem()
        while le is not None:
            count += 1
            le = le.getNextElem()
        return count

    def writeList(self):
        le = self.startElem.getNextElem()
        while le is not None:
            print(le.getWert())
            le = le.getNextElem()

    def __iter__(self):
        self.current = self.startElem.getNextElem()
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        wert = self.current.getWert()
        self.current = self.current.getNextElem()
        return wert

def main():
    liste = EinfachVerketteteListe()

    liste.addFirst(999)

    for _ in range(5):
        liste.addLast(random.randint(1, 100))

    print("Alle Elemente:")
    liste.writeList()

    print("Länge:", liste.laenge())

    print("Iteration:")
    for wert in liste:
        print(wert)

if __name__ == "__main__":
    main()