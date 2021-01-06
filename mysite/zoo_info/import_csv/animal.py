import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import Animal, Zoo, Area, Habitat

zoo_id = Zoo.objects.get(zoo_id = '台北市立動物園')
data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/AnimalNewTable.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')
print(data)
for row in data:
    if row[0] != 'Animal_ID':
        A_id = Area.objects.get(area_id = int(row[3]))
        H_id = Habitat.objects.get(H_id = int(row[6]))
        animal = Animal()
        animal.animal_id = row[0]
        animal.scientific_id = row[2]
        animal.animal_name = row[1]
        animal.category = row[4]
        animal.conservation = row[5]
        animal.h_id = H_id
        animal.area_id = A_id
        
        animal.save()