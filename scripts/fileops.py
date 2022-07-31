from re import A
import sys
import os


from scripts.logger import *

class FileOps():
    def __init__(self):
        self.__main_link = os.getcwd()
        self.__directory = "Data"
        self.__logger = Logger()    

    def _writeToFile(self, file_name, data):
        method_name = "_writeToFile()"
        try:
            self.__logger._writeData(method_name, "starting")
            try:
                os.chdir(self.__directory)
            except Exception as e:
                self.__logger._writeData("<< [!] Exception in '{}'-method while trying to access '{}'-dir :: {}".format(method_name ,self.__directory, e), link=self.__main_link)
            with open(file_name, "a") as file:
                file.write(data) 
                file.write("\n")
            os.chdir(self.__main_link)
            self.__logger._writeData("      << [+] Successfully wrote the requested data to the log file... ")
            self.__logger._writeData(method_name, "ending")
        except Exception as e:
            os.chdir(self.__main_link)
            self.__logger._writeData("<< [!] Exception while trying to write the requested data '{}' to the requested file '{}' :: {}".format(data, file_name, e))


    def _readFile(self, file_name):
        method_name = "_readFile()"
        try:
            self.__logger._writeData(method_name,"starting") 
            try:
                os.chdir(self.__directory)
            except Exception as e:
                self.__logger._writeData("<< [!] Exception in '{}'-method while trying to access '{}'-dir :: {}".format(method_name, self.__directory, e))
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
            
            os.chdir(self.__main_link)
            self.__logger._writeData(method_name,"ending") 
            return end_list
        except Exception as e:
            os.chdir(self.__main_link)
            self.__logger._writeData("<< [!] Exception while trying to read the requested file '{}' :: {}".format(file_name, e))
            return None 