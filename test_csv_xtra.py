import csv_xtra
import subprocess
import os

class TestClass:
  def test_import_data(self):
    X = csv_xtra.import_data('test_data.csv')
    assert X[0].one == 1
    assert X[1].one == 10
    assert X[0].two == 2
    assert X[1].two == 20

  def test_export_data(self):
    x1, x2 = csv_xtra.dataFrame(), csv_xtra.dataFrame()
    x1.one, x2.one = 1, 10
    x1.two, x2.two = 2, 20
    csv_xtra.export_data([x1,x2],['one', 'two'], file_name = 'tmp_data_out.csv')
    process = subprocess.Popen('diff test_data.csv tmp_data_out.csv', 
                               shell = True, 
                               stdout = subprocess.PIPE, 
                               stderr = subprocess.PIPE)
    assert process.communicate() == ('','')
    os.remove('tmp_data_out.csv')
    