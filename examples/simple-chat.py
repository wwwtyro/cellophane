
import cellophane
import time
clients = []


class BigTalker(cellophane.Handler):

    def on_create(self):
        clients.append(self)
        self.last_time = 0
        self.warnings = 0

    def on_destroy(self):
        clients.remove(self)

    def on_receive(self, message):
        if len(message) > 140:
            self.writeline('Too long (>140 characters)', 'red')
            return
        if time.time() - self.last_time < 1.0:
            self.warnings += 1
            self.writeline('Too fast (>1 line per half second), %d warnings out of 10.' % self.warnings, 'red')
            if self.warnings >= 10:
                self.destroy()
            return
        self.last_time = time.time()
        message = cellophane.escape(message)
        self.writeline('You say, "%s"' % message, 'orange');
        for client in clients:
            if client is not self:
                client.writeline('Someone says, "%s"' % message)

cp = cellophane.Cellophane(BigTalker)
cp.go()

