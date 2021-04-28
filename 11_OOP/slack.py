class DiscordConnector:
    def wrzuc_na_kanal(self, kanal):
        kanal.send('message na kanal')


# w innym pliku


class PythonChannel():
    pass


#-----

class SQLChannel():
    pass


pykanal = PythonChannel()


d = DiscordConnector
d.wrzuc_na_kanal(pykanal)