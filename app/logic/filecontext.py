class FileContext:
    def __init__(self):
        self.filepath = ''
        self._contextRenderer = None
        self._menuBars = []
        self._tools = []

    def getMenuBars(self):
        return self._menuBars

    def getContextRenderer(self):
        return self._contextRenderer

    def getTools(self):
        return self._tools
