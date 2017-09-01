

class MVPerson(object):

    def __init__(self):
        
        self.attrib_dict = {'person_id': None,
        'person_fname': None,
        'person_lname': None,
        'person_status': None,
        'person_postcode': None,
        'person_phonenumber': None,
        'person_email': None,
        'person_contacttype': None,
        'person_attendance': {},
        'person_placement': {},
        'person_church': None}


class MVMissionary(MVPerson):

    def __init__(self):
        super(MVMissionary, self).__init__()

        self.attrib_dict['missionary_datestart'] = None
        self.attrib_dict['missionary_dateend'] = None


class MVStudent(MVPerson):

    def __init__(self):
        super(MVStudent, self).__init__()

        self.attrib_dict['student_currentcakelevel'] = None
        self.attrib_dict['student_datets'] = None
        self.attrib_dict['student_datebt'] = None
        self.attrib_dict['student_datecb'] = None
        self.attrib_dict['student_dateec'] = None
        self.attrib_dict['student_datestartuni'] = None
        self.attrib_dict['student_dateenduni'] = None
        self.attrib_dict['student_levelinvolvement'] = None
        self.attrib_dict['student_spiritualstate'] = None
        self.attrib_dict['student_parentid'] = None
        self.attrib_dict['student_levelleadership'] = None
        self.attrib_dict['student_enrolment'] = {}


class MVPlacement:

    def __init__(self):
        
        self.attrib_dict = {'placement_campusid': None,
        'placement_personid': None,
        'placement_campusname': None,
        'placement_campusdatestart': None,
        'placement_campusdateend': None,
        'placement_hoursavailable': None,
        'placement_role': None,
        'campus_name': None}

class MVAttendance:

    def __init__(self):

        self.attrib_dict = {'attendance_personid': None,
        'attendance_eventid': None,
        'attendance_datestart': None,
        'attendance_dateend': None,
        'attendance_committoaction': None,
        'attendance_levelinvolvement': None,
        'attendance_frequency': None,
        'event_id': None,
        'event_name': None,
        'event_theme': None,
        'event_location': None,
        'event_datestart': None,
        'event_dateend': None}


class MVEnrolment:

    def __init__(self):

        self.attrib_dict = {'enrolment_campusid': None,
        'enrolment_studentid': None,
        'enrolment_facultyid': None,
        'enrolment_campusdatestart': None,
        'enrolment_campusdateend': None,
        'enrolment_hoursavailable': None,
        'enrolment_role': None,
        'faculty_headrep': None,
        'faculty_name': None,
        'campus_name': None}
