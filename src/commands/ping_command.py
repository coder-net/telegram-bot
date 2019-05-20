import time
import command_interface as commands


def ping_command(message):
    return 'pong ({} ms)'.format(int((time.time() - message['message']['date']) * 1e3))


ping = commands.Command()
ping.description = 'get ping'
ping.keys = [r'/ping\s*']
ping.handle = ping_command
