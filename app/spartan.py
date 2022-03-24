class Spartan:
    def __init__(self, s_id, s_fn, s_ln, s_bd, s_bm, s_by, s_co, s_st):
        self.sparta_id = s_id
        self.first_name = s_fn
        self.last_name = s_ln
        self.birth_day = s_bd
        self.birth_month = s_bm
        self.birth_year = s_by
        self.course = s_co
        self.stream = s_st

    def __str__(self):
        return vars(self).__str__()

    def get_sparta_id(self):
        return self.sparta_id

    def set_sparta_id(self, s_id):
        self.sparta_id = s_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, s_fn):
        self.first_name = s_fn

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, s_ln):
        self.last_name = s_ln

    def get_birth_day(self):
        return self.birth_day

    def set_birth_day(self, s_bd):
        self.birth_day = s_bd

    def get_birth_month(self):
        return self.birth_month

    def set_birth_month(self, s_bm):
        self.birth_month = s_bm

    def get_birth_year(self):
        return self.birth_year

    def set_birth_year(self, s_by):
        self.birth_year = s_by

    def get_course(self):
        return self.course

    def set_course(self, s_co):
        self.course = s_co

    def get_stream(self):
        return self.stream

    def set_stream(self, s_st):
        self.stream = s_st
