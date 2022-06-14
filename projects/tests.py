from django.test import TestCase

from users.models import Profile

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
 
 
 #test for Rating Model
class RatingsTestClass(TestCase):
  def setUp(self):
    self.user = Profile.objects.create(username='Liz')
    self.project=Project.objects.create(id=1,tittle='glowing-stars',description='just neon',project_image='image.png',urls='www.neon.com',profile=self.user)
    self.rating = Rating.objects.create(id=1, design=9, usability=10, content=10, profile=self.user, prjects=self.project)

  def tearDown(self):
    Profile.objects.all().delete()
    Project.objects.all().delete()
    Rating.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.rating,Rating))
  
  def test_save_rating(self):
    self.rating = Rating.objects.create(id=1, design=9, usability=10, content=10, profile=self.user, projects=self.project)
    self.rating.save_rating()
    ratings=Rating.objects.all()
    self.assertEqual(len(ratings),1)
  
  def test_delete_rating(self):
    self.rating = Rating.objects.create(id=1, design=9, usability=10, content=10, profile=self.user, prjects=self.project)
    self.rating.save_rating()
    ratings = Rating.objects.all()
    self.assertEqual(len(ratings), 1)
    self.rating.delete_rating()
    rate=Rating.objects.all()
    self.assertEqual(len(rate),0)


