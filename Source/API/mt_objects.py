
"""
Classes:
MVPerson - holds generic people's details
MVMissionary
MVStudent
MVPlacement
MVAttendance
MVEnrolment
"""
class MVPerson(object):
    #this is to hold generic people's details
    def __init__(self):
        self.person_id = 0 #this is the primary key
        self.person_fname = '' #first name
        self.person_lname = '' #last name
        self.person_status = '' #what is the status for?
        self.person_postcode = 0 #
        self.person_phonenumber = ''
        self.person_email = ''
        self.person_contacttype = ''
        self.person_attendance = {}
        self.person_placement = {}
        self.person_church = ''
        ##Do we want address details as well?

class MVMissionary(MVPerson):
    #
    def __init__(self):
        super(MVMissionary, self).__init__()

        self.missionary_datestart = '' #the missionaries start date
        self.missionary_dateend = '' #the missionaries end date


class MVStudent(MVPerson):

    def __init__(self):
        super(MVStudent, self).__init__()

        self.student_currentcakelevel = '' #are we sticking with the cake model?
        self.student_datets = '' #what does these dates mean?
        self.student_datebt = ''
        self.student_datecb = ''
        self.student_dateec = ''
        self.student_datestartuni = '' #date that student started university
        self.student_dateenduni = '' #date that student ended university
        self.student_levelinvolvement = '' #defines their level of involvement
        self.student_spiritualstate = '' #shows the student's current state
        self.student_parentid = 0 #what does this mean?
        self.student_levelleadership = '' #what levels of them are there?
        self.student_enrolment = {} #why is this a dictionary?


class MVPlacement: #what is this for?

    def __init__(self):
        self.placement_campusid = 0 #primary key
        self.placement_personid = 0 #foreign key
        self.placement_campusname = ''
        self.placement_campusdatestart = ''
        self.placement_campusdateend = ''
        self.placement_hoursavailable = 0
        self.placement_role = ''
        self.campus_name = ''


class MVAttendance: #this is for attendance of events (?)

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


class MVEnrolment: #this is for where the student is enrolled (?)

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
