import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    students_list = []
    with open(input_json_path) as data_file:
        data = json.load(data_file)
        for id_key in data:
            if course_name in data[id_key]['registered_courses']:
                students_list.append(data[id_key]["student_name"])
    return students_list


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    courses_dict = {}
    with open(input_json_path) as data_file:
        data = json.load(data_file)
        for id_key in data:
            for student_curses in data[id_key]['registered_courses']:
                if student_curses not in courses_dict.keys():
                    courses_dict[student_curses] = 1
                else:
                    courses_dict[student_curses] = courses_dict[student_curses] + 1

    with open(output_file_path, 'w') as outfile:
        for courseName, numOfStudents in sorted(courses_dict.items()):
            outfile.write('"'+courseName+'" '+str(numOfStudents)+'\n')


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    lecturers_dict = {}
    for file in os.listdir(json_directory_path):
        if file.endswith(".json"):
            with open(os.path.join(json_directory_path, file), 'r') as data_file:
                data = json.load(data_file)
                for course_id in data:
                    for lecturer in data[course_id]["lecturers"]:
                        course_name = data[course_id]["course_name"]
                        if lecturer not in lecturers_dict.keys():
                            lecturers_dict[lecturer] = [course_name]
                        else:
                            if course_name not in lecturers_dict[lecturer]:
                                lecturers_dict[lecturer].append(course_name)

    with open(output_json_path, 'w') as writeTo:
        json.dump(lecturers_dict, writeTo, indent=4)

    return lecturers_dict

