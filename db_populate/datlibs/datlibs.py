import csv

class DatReader:
    def __init__(self, filepath, has_headers=True):
        self.dat_delimiter = chr(20)
        self.dat_quotechar = chr(254)
        self.dat_newline   = chr(174)
        self.dat_column_count = 0

        fp = open(filepath, 'r', encoding='utf-8')
        self.csv_fp = csv.reader(fp, delimiter=self.dat_delimiter, quotechar=self.dat_quotechar)

        if has_headers:
            tmp_headers = self._read_headers()
            self.headers = dict(zip([i for i in range(len(tmp_headers))], tmp_headers))
            self.dat_column_count = len(tmp_headers)
        else:
            self.headers = None
            ## NEED TO GET THE COLUMN COUNT HERE?

    def _read_headers(self):
        return(next(self.csv_fp))

    def column_max_sizes(self):




    def reader_gen(self):
        for row in self.csv_fp:
            yield(row)


