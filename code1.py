# This is pseudocode, congratulating a user on their progress
import libraries

progress = instruqt.user.course_level("Git")
user_name = instruqt.user.name()

if progress=="intermediate":
    print('''congratulations''', user_name, '''you are already at intermediate level in Git.
          Keep up the good work!''')
