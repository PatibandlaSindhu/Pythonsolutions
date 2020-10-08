
def get_action_date(action):
  return action.date

def current_users(actions):
  actions.sort(key=get_action_date)
  machines = {}
  for action in actions:
    if action.machine not in machines:
      machines[action.machine] = set()
    if action.type == "login":
      machines[action.machine].add(action.user)
    elif action.type == "logout":
        if action.user in machines:
            machines[action.machine].remove(action.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
  
class action:
  def __init__(self, action_date, action_type, machine_name, user):
    self.date = action_date
    self.type = action_type
    self.machine = machine_name
    self.user = user

actions = [
    action('2019-10-20 12:45:56', 'login', 'macA.local', 'jordan'),
    action('2019-01-22 15:53:42', 'logout', 'macB.local', 'jordan'),
    action('2019-01-21 18:53:21', 'login', 'macB.local', 'lane'),
    action('2019-01-22 10:25:34', 'logout', 'macA.local', 'jordan'),
    action('2019-01-21 08:20:01', 'login', 'macB.local', 'jordan'),
    action('2019-01-23 11:24:35', 'logout', 'macC.local', 'chris'),
]


users = current_users(actions)
print(users)
generate_report(users)



