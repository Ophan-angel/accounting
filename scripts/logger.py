
import os

class Logger():
    def __init__(self):
        link ="C:\\Users\\{}\\Documents\\Book\\".format(os.getlogin())
        os.chdir(link)
        self.__log_file = "log.txt"
        
    def _writeData(self, data,type=None, link=None):
        try:
            if type == None:
                if link != None:
                    os.chdir(link)
                else:
                    pass
                with open(self.__log_file, "a") as file:
                    file.write(str(data))
                    file.write("\n")
            elif type == "starting":
                msg = "<< [+] Starting '{}'-method ".format(str(data))
                with open(self.__log_file, "a") as file:
                    file.write(msg)
                    file.write("\n")
            elif type == "ending":
                msg = "<< [!] Ending '{}'-method ".format(str(data)) 
                with open(self.__log_file, "a") as file:
                    file.write(msg)
                    file.write("\n")
            True
        except Exception as e:
            print("<< [!] Exception while trying to write the requested data to the log file :: {}".format(e))
    
    def _clearLog(self, link=None):
        try:
            if link != None:
                os.chdir(link)
            else:
                pass
            with open(self.__log_file, "w") as file:
                pass
            return True
        except Exception as e:
            print("<< [!] Exception while trying to clear the log-file :: {}".format(e))
            return False