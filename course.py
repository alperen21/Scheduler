import requests
import course
import itertools
from collections import Counter

class CourseClass:
    def __init__(self,info):
        self.info = info

def prettify(course_name):
    course_name_list = course_name.split("_")
    return course_name_list[0].upper() + " " + course_name_list[1]
    
def get(course):

    url = "http://sabancicourseapi.pythonanywhere.com/course/" + course
    response = requests.get(url)
    json_object = response.json()

    return json_object

def time(class_list):

    day_dict = {
        "M":100,
        "T":200,
        "W":300,
        "R":400,
        "F":500,
    }

    time_dict_start = { #start
        "8:40 am":1,
        "9:40 am":2,
        "10:40 am":3,
        "11:40 am":4,
        "12:40 pm":5,
        "1:40 pm":6,
        "2:40 pm":7,
        "3:40 pm":8,
        "4:40 pm":9,
        "5:40 pm":10,
        "6:40 pm":11,
    }

    time_dict_end = { #start
        "9:30 am":2,
        "10:30 am":3,
        "11:30 am":4,
        "12:30 pm":5,
        "1:30 pm":6,
        "2:30 pm":7,
        "3:30 pm":8,
        "4:30 pm":9,
        "5:30 pm":10,
        "6:30 pm":11,
    }

    return_list = list()
    temp_list = list()

    for index,clas in enumerate(class_list):
        if index != len(class_list) - 1:
            day = clas["day"]
            time = clas["time"]

            start_time = time.split(" - ")[0]
            end_time = time.split(" - ")[1]

            j = 0
            value = time_dict_start[start_time]
            while j < time_dict_end[end_time] - time_dict_start[start_time]:
                temp_list.append(value)
                value += 1
                j += 1
        day_value = day_dict[day]
        temp_list = [element + day_value for element in temp_list]
        return_list += temp_list
        temp_list = []
    return return_list

def get_crn(section_list):

    mydict =  section_list[-1]
    return mydict["crn"]

def get_all_crn(course_list):
    return_list = list()
    for element in course_list:
        crn_dict = element[-1]
        return_list.append(crn_dict["crn"])
    return return_list

def schedule_translate(all_schedule,crn_dict):
    
    display_schedule = {
    101:"",
    102:"",
    103:"",
    104:"",
    105:"",
    106:"",
    107:"",
    108:"",
    109:"",
    110:"",
    111:"",

    201:"",
    202:"",
    203:"",
    204:"",
    205:"",
    206:"",
    207:"",
    208:"",
    209:"",
    210:"",
    211:"",

    301:"",
    302:"",
    303:"",
    304:"",
    305:"",
    306:"",
    307:"",
    308:"",
    309:"",
    310:"",
    311:"",

    401:"",
    402:"",
    403:"",
    404:"",
    405:"",
    406:"",
    407:"",
    408:"",
    409:"",
    410:"",
    411:"",

    501:"",
    502:"",
    503:"",
    504:"",
    505:"",
    506:"",
    507:"",
    508:"",
    509:"",
    510:"",
    511:"",

    "crns":"",
    }

    display_schedule_template = display_schedule.copy()

    translated_schedule_list = list()
    crn_list = list()

    for schedule in all_schedule:
        schedule = list(schedule)
        for lecture in schedule:
            lecture_name = crn_dict[lecture[-1]["crn"]]
            lecture_name = prettify(lecture_name)
            crn_list.append(lecture[-1]["crn"])
            lecture_time_list = time(lecture)

            for lecture_time in lecture_time_list:
                display_schedule[lecture_time] = lecture_name
        
        display_schedule["crns"] = crn_list
        crn_list = []
        lecture_time_list = []
        translated_schedule_list.append(display_schedule)

        display_schedule = display_schedule_template.copy()
        
    return translated_schedule_list

def create_schedules(input):
    schedule =  []
    crn_dict = dict()

    #burada olabilecek tüm schedule olasılıklarını oluşturuyorum
    for lecture in input:
        lesson = course.get(lecture)
        schedule.append(lesson)
        crn_list = course.get_all_crn(lesson)

        for crn in crn_list:
            crn_dict[crn] = lecture
        

    all_schedule = list(itertools.product(*schedule))

    #burada çakışma yaşanan scheduleları siliyorum
    time_conflict_check = list()
    to_be_removed = list()
    for schedule in all_schedule:
        for section in schedule:
            time_conflict_check += course.time(section)
        if len(time_conflict_check) != len(Counter(time_conflict_check).keys()):
            to_be_removed.append(schedule)
        time_conflict_check = []

    for remove in to_be_removed:
        all_schedule.remove(remove)

    return course.schedule_translate(all_schedule,crn_dict)

