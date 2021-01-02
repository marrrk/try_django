from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm
# this is raw class based stuff section


# Create your views here.
# HTTP Methods
def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})


# changing the above function to a class
class CourseView(View):
    # want to make this into a detail view, and having two different templates both working
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None, *args, **kwargs):  # makes id no longer required. Default of no id

        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)


# Raw List View
class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.queryset
        }
        return render(request, self.template_name, context)


class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request, id=None, *args, **kwargs):  # makes id no longer required. Default of no id
        # GET method
        form = CourseModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class CourseUpdateView(View):
    template_name = 'courses/course_update.html'

    def get_object(self): # how we gonna call the required object in the GET and POST methods
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseDeleteView(View):
    template_name = 'courses/course_delete.html'

    def get_object(self): # how we gonna call the required object in the GET and POST methods
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses')
        return render(request, self.template_name, context)


class CourseObjectMixin(object):  # this is used to replace the get_object() method in all the classes above
    # works by the classes that have the method inheriting this thing, and the get_method() thing will work the same
    model = Course
    lookup = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.Model, id=id)
        return obj
