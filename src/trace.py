class Trace(object):
    task = ''
    pid = ''
    tgid = ''
    cpu_num = 0
    time_stamp = 0
    function_name = ''
    def __init__(self, rawdata):
        self.task = self.gettask(rawdata)
        self.pid = self.getpid(rawdata)
        self.tgid = self.gettgid(rawdata)
        self.cpu_num = self.getcpunum(rawdata)
        self.time_stamp = self.gettime(rawdata)
        self.function_name = self.getfunctionname(rawdata)
    def print_data(self):
        print ("task = " + self.task + " pid = " + self.pid +
        " tgid = " + self.tgid + " cpunum = %d"%self.cpu_num + " time = " + self.time_stamp)
    
    def gettask(self,str):
        task = str[0:str.find('-')]
        return task.strip(' ')
    def getpid(self,str):
        pid = str[str.find('-') + 1 : str.find(' ')]
        return pid.strip(' ')
    def gettgid(self,str):
        tgid = str[str.find('(') + 1:str.find(')')]
        return tgid.strip(' ')
    def getcpunum(self,str):
        cpunum = str[str.find('[') + 1:str.find(']')]
        return int(cpunum.strip(' '))
    def gettime(self,str):
        index1 = str.find(':')
        index2 = str.rfind(' ',index1)
        return str[index2:index1]
    def getfunctionname(self,str):
        return ''
        