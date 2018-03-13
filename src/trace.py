class Trace(object):
    task = ''
    pid = ''
    tgid = ''
    cpu_num = 0
    time_stamp = 0
    function_name = ''
    argument = ''
    def __init__(self, rowdata):
        rawdata = self.parserowdata(rowdata)
        # print rawdata
        self.task = self.gettask(rawdata)
        self.pid = self.getpid(rawdata)
        self.tgid = self.gettgid(rawdata)
        self.cpu_num = self.getcpunum(rawdata)
        self.time_stamp = self.gettime(rawdata)
        self.function_name = self.getfunctionname(rawdata)
        self.argument = self.getargument(rawdata)
    def parserowdata(self, data):
        temp = data.split(' ')
        value = []
        for x in temp:
            if(x != ''):
                value.append(x)
        if value[1] == '(':
            value.pop(1);
        return value
        
    def print_data(self):
        print ("task = " + self.task + " pid = " + self.pid +
        " tgid = " + self.tgid + " cpunum = %d"%self.cpu_num + " time = %f"%self.time_stamp + " function_name = " + self.function_name + " argument = " + self.argument)
    
    def gettask(self,data):
        str = date[0]
        task = str[0:str.find('-')]
        return task.strip(' ')
    def getpid(self,data):
        str = data[0]
        pid = str[str.find('-') + 1 :]
        return pid.strip(' ')
    def gettgid(self,data):
        tgid = ''
        if data[1].find('(')!= -1 or data[1].find(')')!= -1:
            tgid = data[1].strip('(').strip(')').strip(' ')
        return tgid
    def getcpunum(self,str):
        # print str
        cpunum = str[str.find('[') + 1:str.find(']')]
        # print str
        # print cpunum
        return int(cpunum.strip(' '))
    def gettime(self,str):
        print str
        return float(str.strip(':'))
    def getfunctionname(self,str):
        return str.strip(':')
    def getargument(self,str):
        temp = ''
        for x in str[6:len(str)]:
            temp = temp + x + ' '
        return temp
        