import sys
import zmq

ctx = zmq.Context()

def run_server(port, name):
    print("STARTING SERVER")
    sock = ctx.socket(zmq.REP)
    sock.bind(f'tcp://*:{port}')
    print("READY")
    while True:
        message = sock.recv_string()
        print(f'RECEIVED: {message}')
        print(f'SENDING:  {name},{message}')
        sock.send_string(','.join((name, message)))

if __name__ == '__main__':
    run_server(5000, 'kim')