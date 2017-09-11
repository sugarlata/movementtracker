import MySQLdb
import mt_objects

class MVDatabaseConnect(object):
    ##This class is for database connection
    def __init__(self):
        super(MVDatabaseConnect, self).__init__(**kwargs) ##why is this written like this?##

        ##Login Details##
        # self used to make the variables accessible to this class only
        self.host = 'localhost'
        self.user = 'nathan'
        self.passwd = 'nothing'
        self.dbname = 'campus_movements'

        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbname)
        self.cur = self.db.cursor()

    def getDB(self): #a function to return the access database details
        return self.db

    def getCur(self): #a function to return the cursor
        return self.cur

class MVPersonDict: #this is to access the dictionary of people

    def __init__(self, db, cur):
        self.db = db
        self.cur = cur

    #####TO DO#####
    def getAllPeople(self):
        pass

    def getAlMissionaries(self):
        pass

    def getAllStudents(self):
        pass

    def updatePerson(self):
        pass

    def updateAllMissionaries(self):
        pass

    def updateAllStudentss(self):
        pass

