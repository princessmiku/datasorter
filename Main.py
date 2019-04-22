"""
Zum Sotieren der Daten in einem Bestimmten verzeichnis
"""

import os
import sys
import shutil
from os import path


# s.rpartition(".")

class Sorter:
    SortPath = ""
    EndPath = ""
    DirPath = ""
    DirPathTrue = False
    PicSame = False
    PicEnd = ["png", "jpg", "gif"]

    def Start(self):
        if self.SortPath == "":
            print("Bitte gebe ein Verzeichnis an")
            PathInput = input()
            self.SortPath = PathInput
        if not path.isdir(self.SortPath):
            print("Dieses Verzeichnis ist existiert nicht")
            sys.exit()

        EndingList = []
        FolderFiles = os.listdir(self.SortPath)
        for f in FolderFiles:
            if not "." in f:
                None
            else:
                Ending = f.rpartition(".")[2]
                if not Ending in EndingList:
                    EndingList.append(Ending)
        if not EndingList:
            print("Es sind keine Dateien Vorhanden")
            sys.exit()

        print("Folgende Dateiendungen sind vorhanden")
        for s in EndingList:
            print(s)

        self.WaitPicAnswer()

        if self.PicSame:
            for x in self.PicEnd:
                if x in EndingList:
                    EndingList.remove(x)
        self.OtherPath()

        if not self.WaitAnswerSoting():
            self.WaitAnswerSoting()

        if self.DirPathTrue:
            if self.DirPath == "":
                print("Kein Pfad zum ablegen der Daten angegeben")
                sys.exit()
            self.EndPath = self.DirPath
        else:
            self.EndPath = self.SortPath

        if not path.isdir(self.EndPath + "/Sorter"):
            os.mkdir(self.EndPath + "/Sorter")
        if not path.isdir(self.EndPath + "/Sorter/Pictures") and self.PicSame:
            os.mkdir(self.EndPath + "/Sorter/Pictures")
        for FName in EndingList:
            if not path.isdir(self.EndPath + "/Sorter/{}".format(FName)):
                os.mkdir(self.EndPath + "/Sorter/{}".format(FName))
        for File in FolderFiles:
            if "." in File:
                print("{} wird nun verschoben".format(File))
                Ending = File.rpartition(".")[2]
                if Ending in self.PicEnd and self.PicSame:
                    if not path.isfile(self.EndPath + "/Sorter/Pictures/" + File):
                        shutil.move(self.SortPath + "/{}".format(File), self.EndPath + "/Sorter/Pictures")
                else:
                    if not path.isfile(self.EndPath + "/Sorter/{}/".format(Ending) + File):
                        shutil.move(self.SortPath + "/{}".format(File), self.EndPath + "/Sorter/{}".format(Ending))
                print("{} erfolgreich verschoben".format(File))
        print("Finish")

    def OtherPath(self):
        print(
            '\nSoll der Ordner in einem Bestimmten Verzeichnis erstellt werden?\n'
            'Das Verzeichnis muss vorher im Code eingegeben werden\ny / n')
        answer = input()
        if answer == "n":
            return
        elif answer == "y":
            self.DirPathTrue = True
            return
        print("Ungültige Eingabe")

    def WaitAnswerSoting(self):
        print("\nMöchten sie fortfahren?\ny / n")
        answer = input()
        if answer == "n":
            sys.exit()
        if answer == "y":
            return True
        print("Ungültige Eingabe")
        return False

    def WaitPicAnswer(self):
        print("\nMöchten sie Alle Bilder in einem Ordner haben?\ny / n")
        answer = input()
        if answer == "n":
            return
        elif answer == "y":
            self.PicSame = True
            return
        print("Ungültige Eingabe")


Sorter = Sorter()
Sorter.Start()
