import os
import sys
from datetime import date

from scripts.logger import Logger
from scripts.fileops import FileOps

class DataOps():
    def __init__(self):
        self.__fileops = FileOps() 
        self.__logger  = Logger() 

    def _getDate(self, type=None):
        method_name = "_getDate()"
        try:
            self.__logger._writeData(method_name, "starting")
            
            if type == None:
                # get the requested date with the 'datetime'-module
                current_date = str(date.today())
                self.__logger._writeData("  [*] Current date :: {}".format(current_date))
                self.__logger._writeData(method_name, "ending")
            else:
                current_date = str(date.today().strftime("%b-%d-%Y"))

            # return the date
            return current_date 
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to get the date :: {} ".format(e))
            self.__logger._writeData(method_name, "ending")
            return False

    
    def _getUserInput(self):
        method_name = "_getUserInput()"
        try:
            # get the user input with 'input'-function... 
            self.__logger._writeData(method_name, "starting")
            user_input  = input("<\: ")

            # check the length of the input
            if len(user_input) != None:
                self.__logger._writeData(method_name, "ending")
                return user_input
            else:
                self.__logger._writeData(method_name, "ending")
                return None
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to get the user input :: {} ".format(e))
            self.__logger._writeData(method_name, "ending")
            return None 

    def _deleteMonth(self):
        method_name = "_deleteMonth()"
        try:
            temp_link = os.getcwd() 
            self.__logger._writeData(method_name, "starting")       
            link = "Data"
            try:
                os.chdir(link)
            except Exception as e:
                self.__logger._writeData("<< [!] Exception while trying to change the dir to delete the current month :: {}".format(e))

            file_name = self._createFileName() 
            with open(file_name, "w") as file:
                pass
            
            os.chdir(temp_link)

            self.__logger._writeData("  [*] Successfully deleted the current month... ")

            self.__logger._writeData(method_name, "ending")
            return True
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to delete the current month :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return False

    def _clearLog(self):
        method_name = "_clearLog()"
        try:
            self.__logger._writeData(method_name, "starting")

            file_name = "log.txt"
            with open(file_name, "w") as file:
                pass

            self.__logger._writeData("  [*] Successfully deleted the current log... ")

            self.__logger._writeData(method_name, "ending")
            return True
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to delete the current log :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return False


    def _setTargetValue(self, value):
        method_name = "_setTargetValue()"
        try:
            self.__logger._writeData(method_name, "starting") 

            temp_link = os.getcwd() 
            link = "Data"
            os.chdir(link)
            target_file = "target.sav"
            
            try:
                with open(target_file, "w") as file:
                    file.write(str(value))
            except Exception as e:
                self.__logger._writeData("<< [!] Exception while trying to write to the file '{}' :: {}".format(target_file, e))

            os.chdir(temp_link)
            return True
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to set the target value :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            os.chdir(temp_link)
            return False


    def _searchData(self, data):
        method_name = "_searchData()"
        try:
            self.__logger._writeData(method_name, "starting")

            #try to split string into pieces 
            list = data.split(" ")
            
            price  = ""
            reason = "" 
            mode   = "" 

            target = None 

            #iterate through the list and search for key-words 
            for i in range(len(list)):
                #search for the explicit key word 'eingabe'
                if list[i] == "eingabe":
                    # get price and reason attribute
                    for j in range(len(list)):
                        if list[j] == "-p": 
                            price = list[j+1]
                        elif list[j] == "-g":
                            reason = list[j+1]
                elif list[i] == "setzeZiel":
                    for j in range(len(list)):
                        if list[j] == "-z":
                            target = list[j+1] 
                        else:
                            pass
                else:
                    pass
            
            if target != None:
                self._setTargetValue(target)
            else:
                pass

            # check for a given mode and look if price and reason are given... 
            if mode != None:
                if price != None:
                    if reason != None:
                        file_name = self._createFileName()
                        self.__logger._writeData("  << [*] Writing user data into file : {}".format(file_name)) 
                        self.__fileops._writeToFile(file_name, "-M {} -D {} -P {} -G {}".format(mode, self._getDate(type="Long"), price, reason))
                else:
                    pass
            else:
                pass

            self.__logger._writeData(method_name, "ending")
            return True
        except Exception as e: 
            self.__logger._writeData("<< [!] Exception while trying to search the requested data :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return False

    def _breakDownData(self):
        method_name = "_breakDownData()"
        try:
            self.__logger._writeData(method_name, "starting")
            data = self.__fileops._readFile(self._createFileName())
            if data == None:
                return data
            else:
                pass

            dates = []
            prices = [] 
            reasons = [] 

            for line in data:
                temp_list = line.split(" ")
                for i in range(len(temp_list)):
                    if temp_list[i] == "-D": 
                        dates.append(temp_list[i+1])
                    elif temp_list[i] == "-P":
                        if temp_list[i+1] == '':
                            pass
                        else: 
                            prices.append(temp_list[i+1])
                    elif temp_list[i] == "-G":
                        reasons.append(temp_list[i+1])

            data_dict = {"date":dates, "price":prices, "reason":reasons}

            self.__logger._writeData(method_name, "ending")
            return data_dict
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to break down the data :: {}".format(e))
            self.__logger._writeData(method_name, "ending")

    def _showStatus(self):
        method_name = "_showStatus()"
        try:
            self.__logger._writeData(method_name, "starting")

            target_file = "target.sav"

            target_val = None
            #look for the target value
            data = self.__fileops._readFile(target_file)
            if data != None:
                target_val = float(data[0])
            else:
                #no target value was found
                pass
            
            data = self._breakDownData() 
            if data == None:
                return 0
            else:
                pass
            if target_val == None or target_val == 0.0:
                counter = 0
                for i in range(len(data["price"])):
                    counter += float(data["price"][i]) 
                self.__logger._writeData(method_name, "ending")
                return counter
            else:
                for i in range(len(data["price"])):
                    target_val -= float(data["price"][i]) 
                self.__logger._writeData(method_name, "ending")
                return target_val
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to show the current status :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return None

    def _printMonth(self, month=None):
        method_name = "_printMonth()"
        try:
            self.__logger._writeData(method_name, "starting")

            data_dict = self._breakDownData()

            print("="*75)
            print("     {}      -------     {}      -------     {}      ".format("Tag", "Wert", "Grund"))
            for i in range(len(data_dict["date"])):
                print('%*s   %*s    %*s ' % (7, data_dict["date"][i], 15, data_dict["price"][i], 20, data_dict["reason"][i]))
            self.__logger._writeData(method_name, "ending")
        except Exception as e: 
            self.__logger._writeData("<< [!] Exception while trying to print the values of the month :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return True

    def _createFileName(self):
        method_name = "_createFileName()"
        try:
            self.__logger._writeData(method_name, "starting")

            file_name = "" 
            current_date = self._getDate()

            extracted_month = "" 
            #search for the first '-' character 
            for i in range(len(current_date)):
                if current_date[i] == "-":
                    extracted_month += current_date[i+1]
                    extracted_month += current_date[i+2]
                    break

            # transfer the extracted month to a name
            file_name = "{}-data.sav".format(extracted_month)

            self.__logger._writeData("  [*] Extracted file name :: {}".format(file_name))
            self.__logger._writeData(method_name, "ending")
            return file_name 
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to create the requested filename :: {}".format(e))
            self.__logger._writeData(method_name, "ending")
            return None