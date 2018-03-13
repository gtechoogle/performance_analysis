class VerifyClass(object):
    source_data = []
    target_data = []
    pkgname=''
    def __init__(self, source, target):
        self.source_data = source;
        self.target_data = target;

    def checkverifyclass(self, pkg):
        self.pkgname = pkg
        
        