from _user import User

class Admin(User):
  def __init__(self, first_name, last_name, login_attempts):
    super().__init__(first_name, last_name, login_attempts)

    self.privileges = Privileges()

class Privileges():
  def __init__(self, privileges = ['разрешено добавлять сообщения',
                                   'разрешено удалять пользователей',
                                   'разрешено банить пользователей']):
    self.privileges = privileges

  def show_privileges(self):
    for privilege in self.privileges:
      print(privilege)