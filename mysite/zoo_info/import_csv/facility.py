import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import Facility, Zoo, Area

data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/FacilityTable.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')
zoo_id = Zoo.objects.get(zoo_id = '台北市立動物園')
for row in data:
    if row[0] != 'Zoo_ID':
        area = Area.objects.get(area_id = row[3])
        facility = Facility()
        facility.zoo_id = zoo_id
        facility.type = row[1]
        facility.name = row[2]
        facility.area_id = area
        facility.save()