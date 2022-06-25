import json
import os

"""
This function returns a list of the names of the students who registered for
the course with the name "course_name".

:param input_json_path: Path of the students database json file.
:param course_name: The name of the course.
:return: List of the names of the students.
"""


def names_of_registered_students(input_json_path, course_name):
    students_list = []
    with open(input_json_path) as data_file:  #os.poen?
        data = json.load(data_file)
        return [data[id_key]["student_name"] for id_key in data if course_name in data[id_key]["registered_courses"]]
        #for id_key in data:
            #if (course_name in data[id_key]['registered_courses']):
                #students.append(data[id_key]["student_name"]);
    return students_list


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    pass


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass


students = []
input_json_path = "c:\Compiles C AVIA\hw5\students_database.json";
course_name = "Introduction to Algorithms";
print(names_of_registered_students(input_json_path,course_name));