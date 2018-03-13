class VerifyClasChecker(object):
    source_data = []
    target_data = []
    def __init__(self, source, sourcepkgname):
        print("VerifyClasChecker")
        self.source_data = self.getsourcedata(source, sourcepkgname);
        for data in self.source_data:
            data.print_data()

    def getsourcedata(self, data, pkgname):
        valuelist = []
        for value in data:
            if value.task == pkgname:
                valuelist.append(value)
        return valuelist
            

        
        