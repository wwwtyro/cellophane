import cellophane

class Echoer(cellophane.Handler):
    def on_receive(self, message):
        self.writeline(message)

cp = cellophane.Cellophane(Echoer)
cp.go()

    
