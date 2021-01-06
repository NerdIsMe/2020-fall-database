import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import IndividualAnimal, Animal


data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/IndividualTable.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')
print(data)
for row in data:
    if row[0] != 'Name':
        individual = IndividualAnimal()
        individual.name = row[0]
        individual.year_in = row[1]
        individual.age = row[2]
        individual.animal_id = Animal.objects.get(animal_id = row[3])

        individual.save()