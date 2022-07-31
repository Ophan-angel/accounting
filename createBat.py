import os

class Create():
    def __init__(self):
        self.__file_name = "accouting.bat"
        self._createBat() 

    def _createBat(self):
        try:
            current_link = os.getcwd()
            print("<< [*] The used link is :: {}".format(current_link))

            current_work = current_link + "\\accounting.py"
            with open(self.__file_name, "w") as file: 
                file.write("@Echo off\n")
                file.write("title Accounting\n")
                file.write("color 0a\n")
                file.write("python {}\n".format(current_work))
                file.write("pause")
        
        except Exception as e:
            print("<< [!] Exception while trying to create the requested batch file :: {}".format(e))

def main():
    obj = Create() 

main() 