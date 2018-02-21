class User():
  def __init__(self, first_name, last_name, login_attempts):
    self.first = first_name
    self.last = last_name
    self.login_attempts = login_attempts

  def increment_login_attempts(self):
    self.login_attempts += 1

  def resset_login_attempts(self):
    self.login_attempts = 0