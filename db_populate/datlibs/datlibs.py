import csv

class DatReader:
    def __init__(self, filepath, has_headers=True):
        self.has_headers = has_headers
        self.dat_delimiter = chr(20)
        self.dat_quotechar = chr(254)
        self.dat_newline   = chr(174)
        self.dat_column_count = 0
        self._open_file(filepath)

    def _open_file(self, fp):
        self.fp = open(fp, 'r', encoding='utf-8')
        self.csv_fp = csv.reader(self.fp,
                                 delimiter=self.dat_delimiter,
                                 quotechar=self.dat_quotechar)

        self.headers = self._read_headers()
        if not self.has_headers:
            ## if has_headers is false we still need column count
            ## this generates generic columns and resets to start of dat file
            self.fp.seek(0)
            for k in self.headers:
                self.headers[k] = "COLUMN {0}".format(k)

    def _read_headers(self):
        """ returns dict {header position: header name}"""
        tmp_headers = next(self.csv_fp)
        self.dat_column_count = len(tmp_headers)
        return(dict(zip([i for i in range(len(tmp_headers))], tmp_headers)))

    def get_column_max(self):
        self.column_maxlen = {n: 0 for n in range(self.dat_column_count)}
        for row in self.csv_fp:
            for column in self.column_maxlen:
                if len(row[column]) > self.column_maxlen[column]:
                    self.column_maxlen[column] = len(row[column])
        self._open_file(self.fp.name)  ## necessary to re-open after iterating to the end of the csv
        return(self.column_maxlen)

    def print_report(self):
        try:
            self.column_maxlen
        except AttributeError:
            self.get_column_max()

        for n in range(self.dat_column_count):
            print("\t".join([self.headers[n], str(self.column_maxlen[n])]))

    def close(self):
        self.fp.close()
        return(self.fp.closed)

    def reader_gen(self):
        for row in self.csv_fp:
            yield(row)

    def __next__(self):
        return(next(self.csv_fp))


