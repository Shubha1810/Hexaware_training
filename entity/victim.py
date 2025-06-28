class Victim:
    def __init__(self, victim_id=None, first_name="", last_name="", dob="", gender="", contact_info=""):
        self.__victim_id = victim_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__gender = gender
        self.__contact_info = contact_info

    def get_victim_id(self): return self.__victim_id
    def set_victim_id(self, victim_id): self.__victim_id = victim_id

    def get_first_name(self): return self.__first_name
    def set_first_name(self, first_name): self.__first_name = first_name

    def get_last_name(self): return self.__last_name
    def set_last_name(self, last_name): self.__last_name = last_name

    def get_dob(self): return self.__dob
    def set_dob(self, dob): self.__dob = dob

    def get_gender(self): return self.__gender
    def set_gender(self, gender): self.__gender = gender

    def get_contact_info(self): return self.__contact_info
    def set_contact_info(self, contact_info): self.__contact_info = contact_info

    def __str__(self):
        return f"Victim[ID={self.__victim_id}, Name={self.__first_name} {self.__last_name}]"
