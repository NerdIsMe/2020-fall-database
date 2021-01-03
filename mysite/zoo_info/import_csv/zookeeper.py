import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import Zookeeper


data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/Zookeeper.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')
print(data)
for row in data:
    if row[0] != 'KeeperID':
        zookeeper = Zookeeper()
        zookeeper.keeper_id = row[0]
        zookeeper.name = row[1]
        zookeeper.join_time = row[2]
        zookeeper.department = row[3]
        zookeeper.birth = row[4]
        zookeeper.save()