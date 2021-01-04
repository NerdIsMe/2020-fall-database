import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import Area, Zoo

zoo_id = Zoo.objects.get(zoo_id = '台北市立動物園')
data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/AreaTable.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')
print(data)
for row in data:
    if row[0] != 'Area_ID':
        area = Area()
        area.area_id = row[0]
        area.close_time = row[1]
        area.theme = row[2]
        area.nearby = row[3]
        area.distance = row[4]
        area.position = row[5]
        area.zoo_id = zoo_id
        area.save()