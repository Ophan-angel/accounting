import subprocess
import os
import sys

from scripts.logger import * 
from scripts.fileops import * 
from scripts.dataops import *

class Book():
    def __init__(self):
        self.__logger = Logger() 
        self.__fileops = FileOps() 
        self.__dataops = DataOps() 

        self.__logger._writeData("\n\n<< [+] Starting of main application on {}".format(self.__dataops._getDate()))
        
        self._startApplication()

    def _greeting(self):

        method_name  = "_greeting()"
        self.__logger._writeData(method_name, "starting")
        user = os.getlogin() 
        date = self.__dataops._getDate(type="Long") 
            
        # greeting the user 
        print("="*85)
        print("<< [+] Hallo, {}!".format(user))
        print("="*85)
        print("<< [Info] Aktuelles Datum : {}".format(date))
        print("<< [Info] Aktueller Stand : {} Euro\n".format(self.__dataops._showStatus()))
        self.__logger._writeData(method_name, "ending")
        return True
        
    def _clearScreen(self):
        method_name = "_clearScreen()"
        try:
            self.__logger._writeData(method_name, "starting")
            subprocess.run("cls", shell=True)
            self.__logger._writeData(method_name, "ending")
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to clear the screen :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return False

    def _startApplication(self):
        method_name = "_startApplication()"
        try:
            self.__logger._writeData(method_name, "starting")

            self._greeting()
            
            bol = True
            while bol: 
                # get the user-inputs
                user_input = self.__dataops._getUserInput() 
                if user_input == "stop" or user_input == "stop " or user_input == "ende":
                    self.__logger._writeData("  [*] User requested shutdown ... ")
                    bol = False
                elif user_input == None:
                    pass
                elif user_input == "clearLog":
                    self.__dataops._clearLog() 
                elif user_input == "leereMonat":
                    self.__dataops._deleteMonth()
                elif user_input == "zeigeMonat":
                    self.__dataops._printMonth()
                elif user_input == "aktuell":
                    self._clearScreen() 
                    self._greeting()
                else:
                    bol = self.__dataops._searchData(user_input)
            
            self.__logger._writeData(method_name, "ending")
            return True 
        except Exception as e:
            self.__logger._writeData("Exception while trying to start the application :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return False
        except KeyboardInterrupt:
            self.__logger._writeData("<< [Info] User requested shutdown ... ")
            self.__logger._writeData(method_name, "ending")
            return False 

def main():
    obj = Book() 

main() 

