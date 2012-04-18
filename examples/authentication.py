
import cellophane

clients = []

class BigTalker(cellophane.Handler):

    def on_create(self):
        clients.append(self)
        self.write('Please enter a username: ', 'lightblue')
        self.name = None
        self.password = None

    def on_destroy(self):
        clients.remove(self)

    def on_receive(self, message):
        if not self.authenticated():
            self.authenticate(message)
            return
        message = cellophane.escape(message)
        self.writeline('You say, "%s"' % message, 'orange');
        for client in clients:
            if client is not self and client.authenticated:
                client.writeline('%s says, "%s"' % (self.name, message))

    def authenticated(self):
        return self.name is not None and self.password is not None

    def authenticate(self, message):
        if self.name is None:
            name = cellophane.escape(message)
            self.writeline(name)
            if name in [c.name for c in clients]:
                self.write('Sorry, that name is taken. Please enter a different username: ', 'red')
                return
            self.name = name
            self.writeline('Please enter a password:', 'lightblue')
            self.set_password_mode(True)
            return
        if self.password is None:
            self.password = message
            self.set_password_mode(False)
            self.writeline('Welcome %s!' % self.name, 'lightblue')
            return


cp = cellophane.Cellophane(BigTalker)
cp.go()

