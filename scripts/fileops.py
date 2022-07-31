import sys
import os


from scripts.logger import *

class FileOps():
    def __init__(self):
        self.__logger = Logger() 

    def _writeToFile(self, file_name, data):
        method_name = "_writeToFile()"
        try:
            self.__logger._writeData(method_name, "starting")
            with open(file_name, "a") as file:
                file.write(data) 
                file.write("\n")
            self.__logger._writeData("      << [+] Successfully wrote the requested data to the log file... ")
            self.__logger._writeData(method_name, "ending")
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to write the requested data '{}' to the requested file '{}' :: {}".format(data, file_name, e))


    def _readFile(self, file_name):
        method_name = "_readFile()"
        try:
            self.__logger._writeData(method_name, "starting") 
            with open(file_name, "r") as file:
                data = file.readlines() 


                end_list = [] 
                for element in data:
                    const_list = [] 
                    for character in element:
                        if character == "\n": 
                            pass
                        else: 
                            const_list.append(character)
                    string = "".join(const_list)
                    end_list.append(string)
            
            self.__logger._writeData(method_name, "ending") 
            return end_list
        except Exception as e:
            self.__logger._writeData("<< [!] Exception while trying to read the requested file '{}' :: {}".format(file_name, e))
