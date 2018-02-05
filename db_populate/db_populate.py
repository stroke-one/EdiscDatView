import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DBConnect:
    def __init__(self, **kwargs):
        self.con = None
        try:
            self.con = psycopg2.connect(**kwargs)
            self.curs = self.con.cursor()

        except psycopg2.OperationalError as err:
            print("Error connecting to database\n{0}".format(err))
            return(False)
        return

    def close(self):
        if self.con is not None:
            self.con.close()

class DBCreateNew(DBConnect):

    def db_name(self, db_name):
        self.db_name = db_name


class DBInitialSetup():
    def __init__(self, main_db_name):
        self.main_db_name = main_db_name

    def connect(self, **kwargs):
        self.con = None
        try:
            self.con = psycopg2.connect(**kwargs)
            self.curs = self.con.cursor()

        except psycopg2.OperationalError as err:
            print("Error connecting to database\n{0}".format(err))
            return(False)
        return
    def dbsetup(self):
        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        ##  create a main database called dat_viewer_main
        sql = "select datname from pg_database where datname='{0}'".format(self.main_db_name)
        self.curs.execute(sql)
        if bool(self.curs.rowcount):
            raise Exception("Main dat_viewer database exists")
        else:
            try:
                sql = "CREATE DATABASE {0}".format(self.main_db_name)
                self.curs.execute(sql)
            except (Exception, psycopg2.DatabaseError) as err:
                print("Unable to create the new main database\n{0}".format(self.main_db_name))
                print(err)
            finally:
                if self.con is not None:
                    self.con.close()

    def tblsetup(self):
        try:
            sql = """
            CREATE TABLE all_dat_databases (
            database_id SERIAL PRIMARY KEY,
            matter_name VARCHAR(255) NOT NULL,
            matter_number VARCHAR(255) NOT NULL,
            database_name VARCHAR(255) NOT NULL
            )
            """
            self.curs.execute(sql)
            self.con.commit()
        except (Exception, psycopg2.DatabaseError) as err:
            print("Unable to create the new main tables\n{0}".format(main_db_name))
            print(err)

    def close(self):
        if self.con is not None:
            self.con.close()

    def tbltest(self):
        sql = "SELECT * FROM all_dat_databases"
        self.curs.execute(sql)
        row = self.curs.fetchone()
        while row:
            print(row, "Ok")
            row = self.curs.fetchone()
        print("done testing")

    def tblwrite(self, word):
        sql = "INSERT INTO all_dat_databases (matter_name, matter_number, database_name) VALUES ('no', 'no', '{0}')".format(word)
        print(sql)
        self.curs.execute(sql)
        self.con.commit()
        return()

class DBInjectDat(DBConnect):

    def select_database(self):
        pass









