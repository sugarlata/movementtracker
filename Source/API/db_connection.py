import MySQLdb
import mt_objects
class MVDatabaseConnect(object):
    ##This class is for database connection
    def __init__(self):
        super(MVDatabaseConnect, self).__init__(**kwargs) ##why is this written like this?##

        ##Login Details##
        host = 'localhost'
        user = 'nathan'
        passwd = 'nothing'
        dbname = 'campus_movements'

    def db_set(self, host, user, passwd, dbname):
        self.db = None
        self.cur = None

        self.db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
        self.cur = self.db.cursor()

class MVPersonDict:
