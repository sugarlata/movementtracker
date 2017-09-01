from db_connection import MVConnection


class FilterType:

    def __init__(self, filter_name, campus_id):
        self.filter_name = filter_name
        self.chart_data = ChartData(filter_name)
        self.campus_id = campus_id

    def load_data(self):
        self.chart_data.load_data(self.campus_id)

    def cd_get_all_breakdown(self):
        self.chart_data.get_all_breakdowns()

    def nd_close_mv_conn(self):
        self.chart_data.name_data.close_mv_conn()

    def nd_get_list_students(self, attrib_val):
        self.chart_data.name_data.get_list_students(attrib_val)

    def nd_get_all_students(self):
        self.chart_data.name_data.get_all_students()


class ChartData:

    def __init__(self, filter_name):
        self.filter_name = filter_name
        self.name_data = NameData(filter_name)

    def load_data(self, campus_id):
        self.name_data.load_data(campus_id)

    def get_all_breakdowns(self):

        students = self.name_data.get_all_students()
        attrib_list = list(set(v.attrib_dict['student_%s' % self.filter_name]
                               for v in students.values()))

        total_students = len(students.values())

        # Get all the attribute values and the percentage breakdown
        attrib_values = {y: len([1 for x in students.values() if
                         x.attrib_dict['student_%s' % self.filter_name] == y])
                         / float(total_students) for y in attrib_list}

        return attrib_values


class NameData:

    def __init__(self, filter_name):
        self.filter_name = filter_name
        self.person_dict = {}
        self.mv_conn = self.create_mv_conn()

    # ------------------------------------------------------------------------------------------
    # Following two functions go together to create and have function to close connections on DB
    def create_mv_conn(self):
        return MVConnection()

    def close_mv_conn(self):
        self.mv_conn.db_close_connections()
    # ------------------------------------------------------------------------------------------

    def load_data(self, campus_id):
        self.person_dict = None
        self.person_dict = self.mv_conn.summary_get_names(self.filter_name, campus_id)

    def get_list_students(self, attrib_val):
        td = {}
        for u, v in self.person_dict.items():
            if v.attrib_dict['student_%s' % self.filter_name] == attrib_val:
               td[u] = v

        return td

    def get_all_students(self):
        return self.person_dict



