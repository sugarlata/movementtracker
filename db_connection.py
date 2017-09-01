import MySQLdb
from mt_objects import MVStudent
from mt_objects import MVMissionary


class MVConnection:

    def __init__(self):

        # TODO Add in options to this function for key word arguments
        host = 'localhost'
        user = 'nathan'
        passwd = 'nothing'
        dbname = 'campus_movements'
        self.db_set(host, user, passwd, dbname)

    def db_set(self, host, user, passwd, dbname):
        self.db = None
        self.db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)

    def db_close_connections(self):
        self.db.cursor().close()
        self.db.close()

    def summary_get_names(self, filter_type, campus_id):

        cur = self.db.cursor()

        # cur string below factors in specific campus. Will skip that for the moment though
        # cur_str = """SELECT p.person_id, p.person_fname, p.person_lname, s.student_%s
        # FROM person AS p
        # INNER JOIN student AS s ON p.person_id = s.student_personid
        # INNER JOIN enrolment AS e ON p.person_id = e.enrolment_idstudent
        # WHERE p.person_status = 'Active' AND p.person_contacttype = 'Student' AND e.enrolment_campusid = %s""" % filter_type, campus_id
        cur_str = """SELECT p.person_id, p.person_fname, p.person_lname, s.student_%s
        FROM person AS p
        INNER JOIN student AS s ON p.person_id = s.student_personid
        WHERE p.person_status = 'Active' AND p.person_contacttype = 'Student'""" % filter_type

        cur.execute(cur_str)
        resp = cur.fetchall()

        stud_dict = {}
        for s in resp:
            student = MVStudent()
            student.attrib_dict['person_id'] = s[0]
            student.attrib_dict['person_fname'] = s[1]
            student.attrib_dict['person_lname'] = s[2]
            student.attrib_dict['student_%s' % filter_type] = s[3]

            stud_dict[s[0]] = student

        return stud_dict









