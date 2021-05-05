from instapy import InstaPy
from instapy import smart_run
# import schedule
import time

my_username = 'erikmikrospace@mail.ru'
my_password = 'nj~7@Qgvq'

session = InstaPy(username=my_username, password=my_password,
                  headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(
        enabled=True, delimit_by_numbers=True, max_followers=500, min_followers=30, min_following=50)

    session.set_do_follow(True, percentage=100)
    # session.set_dont_like([''])

    session.like_by_tags(['elisatest', 'microbiology', 'laboratory',
                          'medicine', 'biochemistry', 'health'], amount=50)

    # session.like_by_locations([216253160/central-park-reservoir-running-track/])
    # session.follow_by_tags([])

# schedule.every().day.at("6:00").do(job)
# schedule.every().day.at("18:00").do(job)
while True:
    schedule.run_panding()
    time.sleep(10)
