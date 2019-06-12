

class Dispatcher:

    cmds = {}

    def reg(self, cmd, fn):
        cmds[cmd] = fn

    def run(self):
        while True:
            cmd = input("Please input your command").strip()
            if cmd == 'quit':
                return
            self.cmds.get(cmd, self.defaultfn)()

    def defaultfn(self):
        print('Unknow command.')