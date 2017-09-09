

class MVPerson(object):

    def __init__(self):
        self.person_id = 0
        self.person_fname = ''
        self.person_lname = ''
        self.person_status = ''
        self.person_postcode = 0
        self.person_phonenumber = ''
        self.person_email = ''
        self.person_contacttype = ''
        self.person_attendance = {}
        self.person_placement = {}
        self.person_church = ''


class MVMissionary(MVPerson):

    def __init__(self):
        super(MVMissionary, self).__init__()

        self.missionary_datestart = ''
        self.missionary_dateend = ''


class MVStudent(MVPerson):

    def __init__(self):
        super(MVStudent, self).__init__()

        self.student_currentcakelevel = ''
        self.student_datets = ''
        self.student_datebt = ''
        self.student_datecb = ''
        self.student_dateec = ''
        self.student_datestartuni = ''
        self.student_dateenduni = ''
        self.student_levelinvolvement = ''
        self.student_spiritualstate = ''
        self.student_parentid = 0
        self.student_levelleadership = ''
        self.student_enrolment = {}


class MVPlacement:

    def __init__(self):
        self.placement_campusid = 0
        self.placement_personid = 0
        self.placement_campusname = ''
        self.placement_campusdatestart = ''
        self.placement_campusdateend = ''
        self.placement_hoursavailable = 0
        self.placement_role = ''
        self.campus_name = ''


class MVAttendance:

    def __init__(self):

        self.attendance_personid = 0
        self.attendance_eventid = 0
        self.attendance_datestart = ''
        self.attendance_dateend = ''
        self.attendance_committoaction = ''
        self.attendance_levelinvolvement = ''
        self.attendance_frequency = ''
        self.event_id = 0
        self.event_name = ''
        self.event_theme = ''
        self.event_location = ''
        self.event_datestart = ''
        self.event_dateend = ''


class MVEnrolment:

    def __init__(self):

        self.enrolment_campusid = 0
        self.enrolment_studentid = 0
        self.enrolment_facultyid = 0
        self.enrolment_campusdatestart = ''
        self.enrolment_campusdateend = ''
        self.enrolment_hoursavailable = 0
        self.enrolment_role = ''
        self.faculty_headrep = ''
        self.faculty_name = ''
        self.campus_name = ''
