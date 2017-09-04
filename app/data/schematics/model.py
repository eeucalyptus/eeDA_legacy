import yaml, binascii

class Model:
    def __init__(self):
        self.polygons = []
        self.pins = []
        self.description = ''
        self.name = ''
        self.referenceprefix = '?'
        self.path = ''
        self.hash = ''
        self.fields = {}
        
    def load(self, modelpath):
        self.path = modelpath
        with open(modelpath) as stream:
            try:
                modelfile = yaml.load(stream)
                self.polygons = _loadpolygons(modelfile['polygons'])
                self.pins = _loadpins(modelfile['pins'])
                self.description = modelfile['description']
                self.referenceprefix = modelfile['referenceprefix']
                self.name = modelfile['name']
                self.fields = modelfile['fields']
            except yaml.YAMLError as exc:
                print(exc)
                
        self.hash = _crc(modelpath)


def _loadpins(sourcedict):
    return sourcedict


def _loadpolygons(sourcedict):
    return sourcedict


def _crc(filepath):
    last = 0
    for line in open(filepath,"rb"):
        last = binascii.crc32(line, last)
    return "%X"%(last & 0xFFFFFFFF)

