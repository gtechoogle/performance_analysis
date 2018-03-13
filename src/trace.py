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
        self.task = self.gettask(rawdata[0])
        self.pid = self.getpid(rawdata[0])
        self.tgid = self.gettgid(rawdata[1])
        self.cpu_num = self.getcpunum(rawdata[2])
        self.time_stamp = self.gettime(rawdata[4])
        self.function_name = self.getfunctionname(rawdata[5])
        self.argument = self.getargument(rawdata)
    def parserowdata(self, data):
        temp = data.split(' ')
        if (temp[0].find('-') == -1):
            index = -1;
            str1 = ''
            for value in temp:
                index = index + 1
                if value.find('-') !=-1:
                    str1 = str1 + value
                    break
                else:
                    str1 = str1 + value +'_'
            for x in range(0,index+1):
                temp.pop(0)
            temp.insert(0,str1)
        value = []
        for x in temp:
            if(x != ''):
                value.append(x)
        if value[1] == '(':
            value.pop(1);
        includeTgid = False
        for tempvalue in value:
            if (tempvalue.find(')') != -1):
                includeTgid = True
                break
        if (includeTgid == False):
            value.insert(1,"()");
        return value
        
    def print_data(self):
        print ("task = " + self.task + " pid = " + self.pid +
        " tgid = " + self.tgid + " cpunum = %d"%self.cpu_num + " time = %f"%self.time_stamp + " function_name = " + self.function_name + " argument = " + self.argument)
    
    def gettask(self,str):
        task = str[0:str.find('-')]
        return task.strip(' ')
    def getpid(self,str):
        pid = str[str.find('-') + 1 :]
        return pid.strip(' ')
    def gettgid(self,str):
        tgid = ''
        if str.find('(')!= -1 or str.find(')')!= -1:
            tgid = str.strip('(').strip(')').strip(' ')
        return tgid
    def getcpunum(self,str):
        # print str
        cpunum = str[str.find('[') + 1 : str.find(']')]
        # print str
        # print cpunum
        return int(cpunum.strip(' '))
    def gettime(self,str):
        return float(str.strip(':'))
    def getfunctionname(self,str):
        return str.strip(':')
    def getargument(self,str):
        temp = ''
        for x in str[6:len(str)]:
            temp = temp + x + ' '
        return temp
        