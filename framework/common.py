from patterns.creational_patterns import Logger, Engine
from patterns.behavioral_patterns import Subject
from patterns.creational_patterns import CourseFactory

logger = Logger('main')
class CreateCategory:
    @staticmethod
    def create(data, site):
        name = site.decode_value(data['categori_name'])
        id_parent = site.decode_value(data['id_parent'])
        id_parent = '' if id_parent == 'None' else id_parent
        logger.log(f'Создание курса: {name}')

        category = None
        if id_parent:
            category = site.find_category_by_id(int(id_parent))

        new_category = site.create_category(name, category)

        site.categories.append(new_category)

        return new_category


class CreateCourse:
    @staticmethod
    def create(data, site):
        name = site.decode_value(data['course_name'])
        id_parent = site.decode_value(data['id_parent'])
        id_parent = '' if id_parent == 'None' else id_parent
        logger.log(f'Создание курса: {name}')

        category = None
        if id_parent:
            category = site.find_category_by_id(int(id_parent))

        new_course = site.create_course('record', name, category)

        site.courses.append(new_course)

        return new_course


FactoryCreate = {
        'categori_name': CreateCategory,
        'course_name': CreateCourse,
}