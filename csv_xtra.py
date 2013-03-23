import types
import csv

class dataFrame(object):
    def __init__(self):
        pass
    
    def __repr__(self):
        out = ''
        for i in [x for x in dir(self) if '__' not in x]:
            out += '%s: %s' % (i,getattr(self,i))
            out += ' \n'
        return out

def export_data(data, attributes, file_name = 'data_out.csv', delimiter = ','):
    data_out = []
    tmp = []
    for a in attributes:
        if type(a) == types.StringType:
            tmp.append(a)
        elif type(a) == types.TupleType:
            tmp.append(a[0]+'.'+a[1])
        else:
            print type(a) 
    data_out.append(tmp)
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
        data_out.append(tmp)
    f = open(file_name, 'wb')
    csv_writer = csv.writer(f, delimiter = delimiter)
    csv_writer.writerows(data_out)
    f.close()
    
def import_data(file_name, delimiter=',',lines=0, header = []):
    #function reads in flat file with data seperated in columns by a delimter and rows by new line
    #fileName is a string of the path and file name
    #delimiter is the character seperating row, default is a comma
    #lines is the number of rows to be loaded. useful for sampling if data is randomly sorted 
    #header denotes the names of the attributes in the columns. use default assingment if headers are included at the top of the file
    data = []    
    f = open(file_name, 'rb')
    csv_reader = csv.reader(f,delimiter=delimiter)
    if header == []:
        header = csv_reader.next()
    counter = 0
    for row in csv_reader:
        counter += 1
        if lines == 0 or counter <= lines:
            x = dataFrame()
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

def import_dict(file_name, delimiter=','):
    lookup = {}
    f = open(file_name, 'rb')
    csv_reader = csv.reader(f,delimiter=delimiter)
    header = csv_reader.next()
    for row in csv_reader:
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
            print 'error: row in %s has less than 2 columns \n %s' % (file_name, row)
        elif len(row) == 2:
            lookup[tmp_values[0]] = tmp_values[1]
        elif len(row) > 2:
            print 'error: row in %s has more than 2 colums. only using first 2. \n %s' % (file_name, row)
            lookup[tmp_values[0]] = tmp_values[2]
    return lookup
