import time
import command_interface as commands


def ping_command(message):
    return {'text':'pong ({} ms)'.format(int((time.time() - message['message']['date']) * 1e3))}


commands.Command(
    '/ping',
    ping_command,
    '/ping - get ping'
)
