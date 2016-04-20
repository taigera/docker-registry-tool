import os
import sys
import re
import subprocess
from ConfigParser import SafeConfigParser
from subprocess import call

import requests
from requests.auth import HTTPBasicAuth


class DockerRegistryToolOperations(object):
    @staticmethod
    def login():
        """This function authenticates with the Docker Registry by using the configured account."""
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        registry_email = parser.get('docker_registry_tool', 'RegistryEmail')
        call_arguments = ['docker', 'login', '--username=' + registry_username, '--password=' + registry_password, '--email=' + registry_email,
                          registry_address]
        try:
            call(call_arguments)
        except OSError as e:
            print '[ERROR] An error occurred after executing this command. Is Docker installed and running ' \
                  'in your system?'
            print e
            raise

    @staticmethod
    def logout():
        """This function de-authenticates with the Docker Registry."""
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        try:
            call(['docker', 'logout', registry_address])
        except OSError as e:
            print '[ERROR] An error occurred after executing this command. Is Docker installed and running ' \
                  'in your system?'
            print e
            raise

    @staticmethod
    def show_info(args):
        """Action for issuing info sub-command. Gets technical information about an image stored in the
        Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryProtocol') + parser.get('docker_registry_tool',
                                                                                               'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_tool', 'CertificatePath')
        request = requests.get(
            registry_address + '/v2/' + args.remote_image + '/manifests/' + args.tag,
            verify=certificate_path, auth=HTTPBasicAuth(registry_username, registry_password))
        print request.text

    @staticmethod
    def list_images(self):
        """Action for issuing images sub-command. Lists all images stored in the Docker Registry. """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryProtocol') + parser.get('docker_registry_tool',
                                                                                               'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_tool', 'CertificatePath')
        request = requests.get(registry_address + '/v2/_catalog/',
                               verify=certificate_path,
                               auth=HTTPBasicAuth(registry_username, registry_password))
        print request.text

    @staticmethod
    def list_tags(args):
        """Action for issuing tags sub-command. Lists all tags stored in the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryProtocol') + parser.get('docker_registry_tool',
                                                                                               'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_tool', 'CertificatePath')
        request = requests.get(registry_address + '/v2/' + args.remote_image + '/tags/list',
                               verify=certificate_path,
                               auth=HTTPBasicAuth(registry_username, registry_password))
        print request.text

    @staticmethod
    def search_image(args):
        """Action for issuing search sub-command. Tries to find an image stored in the Docker Registry using
        a search criteria.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryProtocol') + parser.get('docker_registry_tool',
                                                                                               'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_tool', 'CertificatePath')
        request = requests.get(registry_address + '/v2/_catalog',
                               verify=certificate_path,
                               auth=HTTPBasicAuth(registry_username, registry_password))
        images = request.json()['repositories']
        regex = re.compile('.*' + args.criteria + '.*')
        results = [m.group(0) for l in images for m in [regex.search(l)] if m]
        print 'Found images in the Docker Registry catalog:'
        print [result.encode('utf-8') for result in results]

    @staticmethod
    def get_digest(args):
        """Action for issuing digest sub-command. Shows the digest of an image stored in the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryProtocol') + parser.get('docker_registry_tool',
                                                                                               'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_tool', 'CertificatePath')
        request = requests.get(
            registry_address + '/v2/' + args.remote_image + '/manifests/' + args.tag,
            verify=certificate_path, auth=HTTPBasicAuth(registry_username, registry_password))
        if 'Docker-Content-Digest' in request.headers:
            print request.headers['Docker-Content-Digest']

    @staticmethod
    def parse_compose(args):
        """Action for issuing compose sub-command. Parse a Docker Compose file that uses images stored in the Docker
        Registry
        :param args: the values passed by the user """
        DockerRegistryToolOperations().login()
        p = subprocess.Popen(['docker-compose', 'up'], cwd=args.local_compose)
        p.wait()
        DockerRegistryToolOperations().logout()

    @staticmethod
    def commit_image(args):
        """Action for issuing commit sub-command. Commit the changes made to a local image and send it to the
        Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        call_tag_arguments = []

        call(['docker', 'commit', args.local_container, registry_address + '/' + args.remote_image + ':' + args.tag])
        call_tag_arguments.append('docker')
        call_tag_arguments.append('tag')
        if args.force_tag == "true":
            call_tag_arguments.append('--force=true')
        call_tag_arguments.append(args.remote_image)
        call_tag_arguments.append(registry_address + '/' + args.remote_image + ':' + args.tag)
        try:
            DockerRegistryToolOperations().login()
            with open(os.devnull, 'w') as devnull:
                call(call_tag_arguments, stdout=devnull, stderr=devnull)
            call(['docker', 'push', registry_address + '/' + args.remote_image + ':' + args.tag])
            DockerRegistryToolOperations().logout()
        except OSError as e:
            print '[ERROR] An error occurred after executing this command. Is Docker installed and running in ' \
                  'your system?'
            print e
            DockerRegistryToolOperations().logout()
            raise

    @staticmethod
    def upload_image(args):
        """Action for issuing upload sub-command. Upload a new image to the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        call_tag_arguments = ['docker', 'tag']

        if args.force_tag == "true":
            call_tag_arguments.append('--force=true')
        call_tag_arguments.append(args.local_image)
        call_tag_arguments.append(registry_address + '/' + args.local_image + ':' + args.tag)
        try:
            DockerRegistryToolOperations().login()
            with open(os.devnull, 'w') as devnull:
                call(call_tag_arguments, stdout=devnull, stderr=devnull)
            call(['docker', 'push', registry_address + '/' + args.local_image + ':' + args.tag])
            DockerRegistryToolOperations().logout()
        except OSError as e:
            print '[ERROR] An error occurred after executing this command. Is Docker installed and running in ' \
                  'your system?'
            print e
            DockerRegistryToolOperations().logout()
            raise

    @staticmethod
    def download_image(args):
        """Action for issuing download sub-command. Pulls an image from the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        try:
            DockerRegistryToolOperations().login()
            call(['docker', 'pull', registry_address + '/' + args.remote_image + ':' + args.tag])
            DockerRegistryToolOperations().logout()
        except OSError as e:
            print '[ERROR] An error occurred after executing this command. Is Docker installed and running in ' \
                  'your system?'
            print e
            DockerRegistryToolOperations().logout()
            raise

    @staticmethod
    def delete_image(args):
        """Action for issuing delete sub-command. Deletes an existing image from the Docker Registry.
        :param args: the values passed by the user
        """
        parser = SafeConfigParser()
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, 'docker_registry_tool.conf')
        parser.read(config_path)
        registry_address = parser.get('docker_registry_tool', 'RegistryProtocol') + parser.get('docker_registry_tool',
                                                                                               'RegistryAddress') + ':' + parser.get(
            'docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        certificate_path = parser.get('docker_registry_tool', 'CertificatePath')
        get_digest_request = requests.get(
            registry_address + '/v2/' + args.remote_image + '/manifests/' + args.tag,
            verify=certificate_path, auth=HTTPBasicAuth(registry_username, registry_password))
        if 'Docker-Content-Digest' in get_digest_request.headers:
            requests.delete(
                registry_address + '/v2/' + args.remote_image + '/manifests/' +
                get_digest_request.headers['Docker-Content-Digest'], verify=certificate_path,
                auth=HTTPBasicAuth(registry_username, registry_password))
            print 'Deleted image reference ' + registry_address + '/' + args.remote_image + ':' + args.tag + \
                  ' with digest ' + \
                  get_digest_request.headers['Docker-Content-Digest']
        else:
            print '[ERROR] Image or tag not found in the Docker Registry'
