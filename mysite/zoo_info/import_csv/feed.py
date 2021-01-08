import csv, sys, os 
#print(sys.path)
project_dir = '/home/jerome/2020_fall/database_project/mysite'
sys.path.append(project_dir)
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()
from zoo_info.models import Feed, Zoo, Animal, Zookeeper

data = csv.reader(open('/home/jerome/2020_fall/database_project/mysite/zoo_info/import_csv/Feed.csv', 'r', encoding = 'utf-8-sig'), delimiter = ',')
for row in data:
    if row[0] != 'Animal_ID':
        animal = Animal.objects.get(animal_id = row[0])
        keeper = Zookeeper.objects.get(keeper_id = row[1])
        feed = Feed()
        feed.animal_id = animal
        feed.keeper_id = keeper
        feed.food = row[2]
        feed.temperature_low = row[3]
        feed.temperature_high = row[4]
        feed.save()
    
print('done.')