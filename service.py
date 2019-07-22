__author__ = 'Nathan Atkinson'

import os
import paramiko
from base import Configuration

class SetUp(Configuration):

    def __init__(self):
        Configuration.__init__(self)
        self.hostname = self.get_configuration_for('server', 'host')
        self.username = self.get_configuration_for('server', 'username')
        self.password = self.get_raw_configuration_for('server', 'password')

        self.src_copy = self.get_configuration_for('location_copy', 'src')
        self.dst_copy = self.get_configuration_for('location_copy', 'dst')

        self.src_get = self.get_configuration_for('location_get', 'src')
        self.dst_get = self.get_configuration_for('location_get', 'dst')


    def copy_file(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)
        ftp_client = ssh_client.open_sftp()
        ftp_client.put(self.src_copy, self.dst_copy)
        ftp_client.close()

    def get_file(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)
        ftp_client = ssh_client.open_sftp()
        ftp_client.get(self.src_get, self.dst_get)
        ftp_client.close()
