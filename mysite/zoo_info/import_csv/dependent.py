import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import Animal, Dependent

data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/DependentTable.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')

for row in data:
    if row[0] != 'Name':
        animal_id = Animal.objects.get(animal_id = row[3])
        dependent = Dependent()
        dependent.name = row[0]
        dependent.pname = row[1]
        dependent.relation = row[2]
        dependent.animal_id = animal_id
        dependent.save()