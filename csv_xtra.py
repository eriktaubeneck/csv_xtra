import types
import csv

class tmp_class(object):
    def __init__(self):
        pass
    
    def __repr__(self):
        out = ''
        for i in [x for x in dir(self) if '__' not in x]:
            out += '%s: %s' % (i,getattr(self,i))
            out += ' \n'
        return out

def export_data(data, attributes, fileName = 'dataOut.csv'):
    dataOut = []
    tmp = []
    for a in attributes:
        if type(a) == types.StringType:
            tmp.append(a)
        elif type(a) == types.TupleType:
            tmp.append(a[0]+'.'+a[1])
        else:
            print type(a) 
    dataOut.append(tmp)
    for x in data:
        tmp = []
        for a in attributes:
            if type(a) == types.StringType:
                try:
                    tmp.append(getattr(x,a))
                except AttributeError:
                    tmp.append('nan')
            elif type(a) == types.TupleType:
                tmp.append(getattr(getattr(x,a[0]),a[1]))
            else:
                print type(a)
        dataOut.append(tmp)
    f = open(fileName, 'wb')
    csvWriter = csv.writer(f, delimiter = ',')
    csvWriter.writerows(dataOut)
    f.close()
    
def import_data(fileName, delimiter_in=','):
    data = []    
    f = open(fileName, 'rb')
    csvReader = csv.reader(f,delimiter=delimiter_in)
    header = csvReader.next()
    for row in csvReader:
        x = tmp_class()
        for h in header:
            tmp_value = row[header.index(h)]
            try:
                tmp_value = int(tmp_value)
            except ValueError:
                try:
                    tmp_value = float(tmp_value)
                except ValueError:
                    pass
            setattr(x,h,tmp_value)
        data.append(x)
    return(data)



















