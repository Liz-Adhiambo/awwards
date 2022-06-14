from django.test import TestCase

from .models import  Project, Rating
# Create your tests here.

class ProjectTestClass(TestCase):
    #Set up Method
    def setUp(self):
        self.proj = Project(tittle="galleria")
        self.proj.save_project()

    def test_instance(self):
        self.assertTrue(isinstance(self.proj,Project))

    def test_save_method(self):
        self.proj.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.proj.save_project()
        self.proj.delete_project()
        project = Project.objects.all()
        self.assertTrue(len(project) == 0)

    def test_update(self):
        project = Project.get_project_id(self.proj.id)
        project.update_project('galleria')
        project = Project.get_project_id(self.proj.id)
        self.assertTrue(project.username == 'galleria')
 
 
 #test for Post Model