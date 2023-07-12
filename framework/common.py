from patterns.creational_patterns import Logger


logger = Logger('main')
DB_name = 'site_db.sqlite'
FILE_CREATE_DATABASE_COMMAND = 'create_db.sql'
DEFAULT_PORT = 8080
DEFAULT_ADDRESS = ''


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


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}'
                         )