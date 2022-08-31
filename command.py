# format string -> python > 3.6
import argparse
import os
image_name = "metricvoid/ece438:20220829.a1"

def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--install',
                action='store_true',
                help='Install Image')
    parser.add_argument('--stop_all',
                action='store_true',
                help='Stop All the Containers')
    parser.add_argument('--remove_all',
                action='store_true',
                help='Remove All the Containers')
    parser.add_argument('--list_all',
                action='store_true',
                help='List All the Containers')
    parser.add_argument('--start',
                    default=None,
                    type=int,
                    help='Start Container Id (Integer):')
    parser.add_argument('--attach',
                default=None,
                type=int,
                help='Attach Container Id (Integer):')
    
    args = parser.parse_args()
    return args

def install():
    print("Start build")
    _command = f"docker build -t {image_name} . "
    val = os.system(_command)

def attach(opt):
    id = opt.attach
    print(f"Attach Container {id}")
    print(f"Attaching to Container ece438-{id}")
    print(f"You may need to press enter a few times to get the command prompt")
    print(f"Use Ctrl-P Ctrl-Q to detach")
    print(f"+================= Container ece438-$id =================+")
    os.system(f"docker attach ece438-{id}") 
    
def start(opt):
    id = opt.start
    ssh_portassign = opt.start + 43820
    print(f"Starting Container {id}")
    with os.popen("pwd") as p:
        pwd = p.read()
    pwd = pwd[:-1]
    
    # container_id
    container_id_cmd = f'docker run -itd --name ece438-{id} --hostname ece438-{id} -p {ssh_portassign}:22 -v \"{pwd}/repo:/repo\" {image_name}'
    with os.popen(container_id_cmd) as p:
        container_id = p.read()
    
    # container_ip
    tmp = '\'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}\''
    container_ip_cmd = f'docker inspect -f {tmp} {container_id}'
    os.system(container_ip_cmd)
    
    print(f"Started Container with name ece348-{id}")
    print(f"You can attach to it with Attach-Container {id}")
    print(f"You can also access this container with SSH at localhost: {ssh_portassign}. Password for root is root")
    print(f"SSH commandline: ssh -lroot localhost -p {ssh_portassign}")

def list_all(opt):
    name_cmd = "docker container ls -q --filter name=ece438-*"
    with os.popen(name_cmd) as p:
        name_list = (p.read()).split('\n')[:-1]
    return name_list

def stop_all(opt):
    print(f"Stopping all ECE 438 containers...")
    name_list=list_all(opt)
    for n in name_list:
        os.system(f"docker container stop {n}")
    print(f"All ECE438 containers stopped.")

def remove_all(opt):
    print(f"Removing all ECE 438 containers...")
    name_list=list_all(opt)
    for n in name_list:
        os.system(f"docker rm -f {n}")
    print(f"All ECE438 containers removed.")

def ssh(opt):
    _command = f"echo {opt.start}"
    val = os.system(_command)

if __name__ == '__main__':
    opt = get_opt()
    if opt.install:
        install()
    
    if (opt.list_all):
        print(list_all(opt))
        # for i in list_all(opt):
            # print(i)

    if (opt.stop_all):
        stop_all(opt)

    if (opt.remove_all):
        remove_all(opt)

    if (opt.start is not None):
        start(opt)

    if (opt.attach is not None):
        attach(opt)



