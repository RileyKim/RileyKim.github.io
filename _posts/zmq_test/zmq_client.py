import sys
import zmq

ctx = zmq.Context()

def run_client(*ports):
    sock = ctx.socket(zmq.REQ)
    for port in ports:
        sock.connect(f'tcp://localhost:{port}')
    while True:
        line = input('>> ')
        print(f'SENDING: {line}')
        sock.send_string(line)
        rep = sock.recv_string()
        name, message = rep.split(',', 1)
        print(f'RECEIVED: {message} FROM {name}')
        if line == 'bye':
            break
    sock.close()

if __name__ == '__main__':
    run_client(*sys.argv[1:])
