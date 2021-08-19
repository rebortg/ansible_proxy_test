import paramiko


ssh = paramiko.SSHClient()

ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

proxy = paramiko.ProxyCommand('ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -W rtr01:22 -i /home/rob/git/vyos/vyos_ansible_proxy/inventory/id_rsa vyos@vyos-oobm')

ssh.connect(
    "rtr01",
    username="vyos",
    allow_agent=True,
    look_for_keys=True,
    key_filename="/home/rob/git/vyos/vyos_ansible_proxy/inventory/id_rsa",
    port=22,
    sock=proxy)

(stdin, stdout, stderr) = ssh.exec_command('uname -a')
for line in stdout.readlines():
    print(line)
ssh.close()