class PseudoOutputDevice:

    def __init__(self, pinNr):
        self.value = True

    def on(self):
        self.value = True

    def off(self):
        self.value = False

    def toggle(self):
        self.value = not self.value
