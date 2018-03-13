import os
import trace

log_file = os.getcwd() + '\\demo_file\\test.html'
trace_data=[]

def main():
    trace_data = gettracedata(log_file)
    for value in trace_data:
        value.print_data()

def gettracedata(file_path):
    temp_data=[]
    trace_begin = False
    for line in open(file_path,'rb'):
        log = line.decode()
        log = log.strip()
        if (istracebegin(log)):
            trace_begin = True
        elif (trace_begin == True):
            if isend(log):
                break
            elif(islog(log)):
                data = trace.Trace(log)
                temp_data.append(data)
                # print (log)
    return temp_data

def istracebegin(str):
    return str.find('<!-- BEGIN TRACE -->') != -1
def isend(str):
    return str.find('</script>') !=-1

def islog(str):
    islog = True
    if str.startswith('#'):
        islog = False
    elif len(str) == 0:
        islog = False
    elif str.find('<script class="trace-data" type="application/text">')!=-1:
        islog = False
    return islog

if __name__ == '__main__':
    main()