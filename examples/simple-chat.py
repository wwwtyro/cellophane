
import cellophane
clients = []


class BigTalker(cellophane.Handler):

    def on_create(self):
        clients.append(self)

    def on_destroy(self):
        clients.remove(self)

    def on_receive(self, message):
        message = cellophane.escape(message)
        self.writeline('You say, "%s"' % message, 'orange');
        for client in clients:
            if client is not self:
                client.writeline('Someone says, "%s"' % message)


cp = cellophane.Cellophane(BigTalker)
cp.go()

