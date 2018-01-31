from paramiko import client

class Ssh:
    client = None

    def __init__(self, address, username, password):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)

    def sendCommand(self, command):
        if (self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata
                    print(str(alldata, "utf8"))
        else:
            return"Connection not opened."

    def canais(self, start):
        count = 1
        while count <= 99:
            self.sendCommand('mkdir -p /root/teste/canais/CFR_' + str(start) + '_' + str(count) + '_' + '1')
            self.sendCommand('chown -R ftp:ftp /root/teste/canais/CFR_' + str(start) + '_' + str(count) + '_' + '1')
            self.sendCommand('chmod -R 755 /root/teste/canais/CFR_' + str(start) + '_' + str(count) + '_' + '1')
            count += 1

    def venda(self, start, end):
        inicio = int(start)
        fim = int(end)
        while inicio <= fim:
            self.sendCommand('mkdir -p /root/teste/vd/CFR_' + str(inicio))
            self.sendCommand('chown -R ftp:ftp /root/teste/vd/CFR_' + str(inicio))
            self.sendCommand('chmod -R 755 /root/teste/vd/CFR_' + str(inicio))
            inicio += 1