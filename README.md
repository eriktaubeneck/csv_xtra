csv_xtra
========

`csv_xtra` is a welterweight module built on top of the standard csv library for quickly and simply objectifying data stored in a csv or other delimited file formats. all of the functionality provided in `csv_xtra` is also replicated in the excellent [pandas](link to pandas) library, however in some cases a user may prefer a smaller package that doesn't rely on any other packages.

usage
=====

    import csv_xtra
    X = csv_xtra.import_data('my_data_file.csv')
    print sum([x.revenue for x in X])

Other attributes of `import_data` can be used. If your data file does not have attribute names in the first row, these must be passed in as `header`. If your data file is not comma delimited, use `delimiter`. If you only want the top n rows, use `lines`. 

    X = csv_xtra.import_data('my_data_file2.tsv', header=['id', 'revenue', 'price', 'units', 'unit_cost'], lines = 10)

If your data is only two columns, a key and a value, the `import_dict` is more useful. Usage is the same, however the `header` attribute isn't relevant, and the `lines` attribute is not built in.

Exporting data is also simple. Given a collection of objects `X` and a list of attributes, the `export_data` function will export `x.attribute` for each x in X and attribute in attributes. If an attribute is unavailable, the utility will export `nan` and will not raise an exception.

    for x in X:
        x.profit = x.revenue - x.units * x.unit_cost
    csv_xtra.export_data(X,['id', 'profit'], file_name = 'my_data_out.csv')


