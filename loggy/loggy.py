from datetime import datetime as dt
from time import strftime


default_name="loggy.log"


def init(f):
    fl = str(__file__).split("\\")
	global default_name
    default_name = fl[len(fl)-1]

conf_file={'info':default_name,'error':default_name,'critical':default_name}
fmt={'d':"%d-%m-%Y @ %H:%M",'s':'->','ls':"||",'rs':"||"}


def now():
    """
    Default value of date parameter:
    Coverts `datetime` object to: "dd-mm-yyyy @ hh:mn"
    using `time.strftime()`
    """
    d=dt.now()
    return d.strftime(fmt['d'])
        
def set_file(error_type,filename):
    """
    Set a file to log specific type of events,
    If not specified, all the logs would be redirected to loggy.log file.
    Usage:
    `loggy.set_file("CRITICAL","critical_file.log")`
    Default events are:
    `CRITICAL, ERROR, INFO`
    Use `loggy.add_custom()` to add custom events!!
    """
    conf_file[error_type.lower()]=filename
    try:
        f=open(filename,"r")
        f.close()
        return
    except:pass
    with open(conf_file[error_type.lower()],"w") as f:
        f.write("{0} logs for {1}\n----------------------".format(error_type.upper(),get_name()))
    return True



def del_all_logs(f):
    import os
    fl = f.split("\\")
    ls=fl[len(fl)-1]
    fstr=f[:-(len(ls)+1)]
    fls=[]
    for _f in os.listdir(fstr):
        if _f.endswith(".log"):
            fls.append(_f)
            os.remove(_f)
    with open(fstr+"\\loggy.log","w") as f:
        f.write("ALL LOGS DELETED AT "+now())
    return (True,fls)


def set_datefmt(strftime):
    """
    Set the format of the date and time for logging
    Should be of type `time.strftime()`
    `loggy.set_datefmt("%H:%M") # hh:mn`
    """
    fmt['d']=strftime
    return fmt

def side_seperator(lsep,rsep):
    """
    To have a custom side lined formatter.
    A side-lined formatter is:
    `[DATE] SEP "L_SEP" EVENT "R_SEP" LOG`
    `loggy.side_seperator(lsep="||",rsep="||") # Default vals`
    """
    fmt['ls']=lsep
    fmt['rs']=rsep
    return fmt


def set_seperator(sep):
    """
    To have a custom formatter.
    A side-lined formatter is:
    `[DATE] SEP "L_SEP" EVENT "R_SEP" LOG`
    `loggy.side_seperator(lsep="||",rsep="||") # Default vals`
    """
    fmt['s']=str(sep)
    return fmt

def info(con,mode="a"):
    #f2=open(conf_file['info'],"r")
    #c=f2.read();f2.close()
    f = open(conf_file['info'],mode)
    c="\n[{0}] {2} {3}   INFO   {4} {1} ".format(now(),con,fmt['s'],fmt['ls'],fmt['rs'])
    f.write(c)
    f.close()
    return True

        
def error(con,mode="w"):
    f2=open(conf_file['error'],"r")
    c=f2.read();f2.close()
    f = open(conf_file['error'],mode)
    c="{2}\n[{0}] {3} {4}   ERROR  {5} {1} ".format(now(),con,c,fmt['s'],fmt['ls'],fmt['rs'])
    f.write(c)
    f.close()
    return True

    
def critical(con,mode="w"):
    f2=open(conf_file['critical'],"r")
    c=f2.read();f2.close()
    #print(c)
    f = open(conf_file['critical'],mode)
    c="{2}\n[{0}] {3} {4} CRITICAL {5} {1} ".format(now(),con,c,fmt['s'],fmt['ls'],fmt['rs'])
    #print(c)
    f.write(c)
    f.close()
    return True


def add_custom(name,filename=None):
    if filename is None:
        filename=default_name
    data = {str(name):str(filename)}
    conf_file.update(data)
    set_file(name,filename)
    return conf_file[name]


def custom(name,con,mode="w"):
    f2=open(conf_file[name],"r")
    c1=f2.read();f2.close()
    f = open(conf_file[name],mode)
    c="{2}\n[{0}] {3} {4} {6} {5} {1} ".format(now(),con,c1,fmt['s'],fmt['ls'],fmt['rs'],name)
    f.write(c)
    f.close()
    return True
    '''
    f = open(conf_file[name],mode)
    c="\n[{0}] {3} {4}  {2}  {5} {1}".format(now(),con,name,fmt['s'],fmt['ls'],fmt['rs'])
    f.append(c)
    f.close()
    return True
    '''

def get_log(name,index=0):
    c=""
    with open(conf_file[name],"r") as f:
        c=f.read()
    #print(c)
    x=c.split("\n")
    #print(x)
    x.reverse()
    return x[index]
