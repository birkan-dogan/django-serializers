from .models import Path, Student
from faker import Faker

def run():
    """
    http://faker.readthedocs.io/en/master/

    $ pip install Faker  # install faker module
    python manage.py flush  # delete all exists data from .db don't forget: createsuperuser

    python manage.py shell
    from student_api.faker import run
    run()
    exit()

    """

fake = Faker(["tr-TR"])

paths = (
    "FullStack",
    "DataScience",
    "AwsDevops",
    "CyberSec"
)

for path in paths:
    new_path = Path.objects.create(path_name = path)

    for i in range(50):
        Student.objects.create(first_name = fake.first_name(), last_name = fake.last_name(), number = fake.pyint(), path = new_path)
