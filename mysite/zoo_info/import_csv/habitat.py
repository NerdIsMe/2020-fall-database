import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import Habitat


data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/Habitat.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')
print(data)
for row in data:
    if row[0] != 'H_ID':
        print('H_id = %s'%row[0])
        habitat = Habitat()
        habitat.H_id = row[0]
        habitat.weather = row[2]
        habitat.continent = row[1]
        habitat.terrian = row[3]

        habitat.save()