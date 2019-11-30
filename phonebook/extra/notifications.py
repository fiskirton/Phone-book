import npyscreen


def spawn_warning_incorrect_input(errors):
    message = errors + "\nPlease, try again(Press TAB)"
    npyscreen.notify_confirm(message, title="Incorrect input", form_color='Blue')


def spawn_notify_confirmation(action_name):
    message = 'Are you sure you want to {}?(Press TAB to make choice)'.format(action_name)
    title = " ".join(('Confirm ', action_name))
    answer = npyscreen.notify_yes_no(message, title=title)
    return answer
