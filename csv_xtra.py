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

def export_data(data, attributes, fileName = 'dataOut.csv', delimiter = ','):
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
    csvWriter = csv.writer(f, delimiter = delimiter)
    csvWriter.writerows(dataOut)
    f.close()
    
def import_data(fileName, delimiter=',',lines=0, header = []):
    #function reads in flat file with data seperated in columns by a delimter and rows by new line
    #fileName is a string of the path and file name
    #delimiter is the character seperating row, default is a comma
    #lines is the number of rows to be loaded. useful for sampling if data is randomly sorted 
    #header denotes the names of the attributes in the columns. use default assingment if headers are included at the top of the file
    data = []    
    f = open(fileName, 'rb')
    csvReader = csv.reader(f,delimiter=delimiter)
    if header == []:
        header = csvReader.next()
    counter = 0
    for row in csvReader:
        counter += 1
        if lines == 0 or counter <= lines:
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

def import_lookup(fileName, delimiter=','):
    lookup = {}
    f = open(fileName, 'rb')
    csvReader = csv.reader(f,delimiter=delimiter)
    header = csvReader.next()
    for row in csvReader:
        tmp_values = []
        for tmp_value in row:
            try:
                tmp_value = int(tmp_value)
            except ValueError:
                try:
                    tmp_value = float(tmp_value)
                except ValueError:
                    pass
            tmp_values.append(tmp_value)
        if len(row) < 2:
            print 'error: row in %s has less than 2 columns \n %s' % (fileName, row)
        elif len(row) == 2:
            lookup[tmp_values[0]] = tmp_values[1]
        elif len(row) > 2:
            print 'error: row in %s has more than 2 colums. only using first 2. \n %s' % (fileName, row)
            lookup[tmp_values[0]] = tmp_values[2]
    return lookup



















