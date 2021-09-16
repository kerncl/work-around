import logging, logging.handlers
import signal


def exit_plan(signum, frame):
    print('Bye bye')

signal.signal(signal.SIGINT, exit_plan)

log = logging.getLogger('mylog')
log.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SocketHandler('localhost',
                    logging.handlers.DEFAULT_TCP_LOGGING_PORT)

log.addHandler(socketHandler)


log.info('Jackdaws love my big sphinx of quartz.')


log.debug('Quick zephyrs blow, vexing daft Jim.')
log.info('How quickly daft jumping zebras vex.')
log.warning('Jail zesty vixen who grabbed pay from quack.')
log.error('The five boxing wizards jump quickly.')

exit_ = 0

while True:
    userinput = input('>>>')
    if 'exit' in userinput:
        break
    log.info(f'Received: {userinput}')
