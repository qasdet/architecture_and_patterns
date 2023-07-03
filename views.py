from framework.templator import render
from framework.common import FactoryCreate
from patterns.creational_patterns import Engine, Logger
from patterns.structural_patterns import AppRoute, Debug
from patterns.behavioral_patterns import EmailNotifier, SmsNotifier, \
    ListView, CreateView, BaseSerializer

site = Engine()
logger = Logger('main')
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()


@AppRoute(url='/')
class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


@AppRoute(url='/page/')
class Page:
    def __call__(self, request):
        if request['method'] == 'POST':
            name = request['data'].get('name', None)
            new_obj = site.create_user('student', name)
            site.students.append(new_obj)

        return '200 OK', render('page.html', date=request.get('date', None))


@AppRoute(url='/student-list/')
class StudentListView(ListView):
    queryset = site.students
    template_name = 'student_list.html'


@AppRoute(url='/add-student/')
class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course_name = site.decode_value(course_name)
        course = site.get_course(course_name)
        student_name = data['student_name']
        student_name = site.decode_value(student_name)
        student = site.get_student(student_name)
        course.add_student(student)


@AppRoute(url='/examples/')
class Examples:

    def __call__(self, request):
        id_category = None
        category = None

        if request['method'] == 'POST':
            data = request['data']
            for k, v in FactoryCreate.items():
                if k in data:
                    course = v.create(data, site)
                    if k == 'course_name':
                        course.observers.append(email_notifier)
                        course.observers.append(sms_notifier)

        elif request['method'] == 'GET' and request['request_params']:
            category = site.find_category_by_id(int(request['request_params']['id']))
            id_category = category.id

        category_list = []
        for i in site.categories:
            if (id_category is None and i.category == id_category) \
                    or (i.category is not None and i.category.id == id_category):
                category_list.append(i)

        courses_list = [ i for i in site.courses if i.category == category]

        id_category = '' if id_category is None else id_category
        return '200 OK', render('examples.html', objects_list=category_list, courses_list=courses_list,
                                cat_id=id_category)


@AppRoute(url='/contact/')
class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html', date=request.get('date', None))


@AppRoute(url='/another_page/')
class Another:
    def __call__(self, request):
        return '200 OK', render('another_page.html', date=request.get('date', None))


@AppRoute(url='/api/')
class CourseApi:
    @Debug(name='CourseApi')
    def __call__(self, request):
        return '200 OK', BaseSerializer(site.courses).save()
