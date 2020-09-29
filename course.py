import requests
import course
import itertools
from collections import Counter
import numpy as np

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
    
    display_schedule = dict()

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
def conflict_check(schedule):
    time_conflict_check = list()
    for section in schedule:
        time_conflict_check += course.time(section)
        if len(time_conflict_check) != len(   Counter(time_conflict_check).keys()):
            return False
    return True

def create_schedules(raw_input):
    input = raw_input.split(",")
    schedule =  []
    crn_dict = dict()
    
    def conflict_check(schedule):
        time_conflict_check = list()
        for section in schedule:
            time_conflict_check += course.time(section)
            if len(time_conflict_check) != len(   Counter(time_conflict_check).keys()):
                return False
        return True
    
    for lecture in input:
        lesson = course.get(lecture)
        schedule.append(lesson)
        crn_list = course.get_all_crn(lesson)

        for crn in crn_list:
            crn_dict[crn] = lecture
    

    all_schedule = [p for p in itertools.product(*schedule) if conflict_check(p)]

    return course.schedule_translate(all_schedule,crn_dict)

