#!/usr/bin/python

import argparse
from ConfigParser import SafeConfigParser

import requests

from docker_registry_tool_operations import DockerRegistryToolOperations


class DockerRegistryTool(object):
    CONST_SCRIPT_VERSION = '1.0.0'

    @staticmethod
    def main():
        """ Function that initializes the argument parser, so the user can give input data to the script using
        command line arguments"""
        if not DockerRegistryTool().check_configuration():
            return  # The script cannot start if the configuration file is incomplete.

        parser = argparse.ArgumentParser(
            description='Enables users to work faster with the Docker Registry, providing a simpler commands '
                        'syntax to launch each basic operation')
        subparsers = parser.add_subparsers()

        # create the parser for the "info" command
        parser_info = subparsers.add_parser('info',
                                            help='Show technical information about an image stored in the '
                                                 'Docker Registry')
        parser_info.add_argument('--remote-image', dest='remote_image', required=True,
                                 help='Image from the Docker Registry')
        parser_info.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image version')
        parser_info.set_defaults(func=DockerRegistryToolOperations().show_info)

        # create the parser for the "images" command
        parser_images = subparsers.add_parser('images', help='Show all images stored in the Docker Registry')
        parser_images.set_defaults(func=DockerRegistryToolOperations().list_images)

        # create the parser for the "tags" command
        parser_tags = subparsers.add_parser('tags',
                                            help='Show all tags stored for an image in the Docker Registry')
        parser_tags.add_argument('--remote-image', dest='remote_image', required=True,
                                 help='Image from the Docker Registry')
        parser_tags.set_defaults(func=DockerRegistryToolOperations().list_tags)

        # create the parser for the "digest" command
        parser_digest = subparsers.add_parser('digest',
                                              help='Get the digest of an image stored in the Docker Registry')
        parser_digest.add_argument('--remote-image', dest='remote_image', required=True,
                                   help='Image from the Docker Registry')
        parser_digest.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image version')
        parser_digest.set_defaults(func=DockerRegistryToolOperations().get_digest)

        # create the parser for the "search" command
        parser_search = subparsers.add_parser('search', help='Search a image in the Docker Registry')
        parser_search.add_argument('--criteria', dest='criteria', required=True, help='Search criteria')
        parser_search.set_defaults(func=DockerRegistryToolOperations().search_image)

        # create the parser for the "upload" command
        parser_upload = subparsers.add_parser('upload', help='Push an image to the Docker Registry')
        parser_upload.add_argument('--local-image', dest='local_image', required=True,
                                   help='Image to upload to the Docker Registry from your computer')
        parser_upload.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image version')
        parser_upload.add_argument('--force-tag', dest='force_tag', choices=['true', 'false'],
                                   help='Force tag of image')
        parser_upload.set_defaults(func=DockerRegistryToolOperations().upload_image)

        # create the parser for the "compose" command
        parser_compose = subparsers.add_parser('compose', help='Process a local Docker Compose file that uses images '
                                                               'stored in the Docker Registry')
        parser_compose.add_argument('--local-compose', dest='local_compose', required=True,
                                    help='Local Docker Compose file path')
        parser_compose.set_defaults(func=DockerRegistryToolOperations().parse_compose)

        # create the parser for the "commit" command
        parser_commit = subparsers.add_parser('commit', help='Commit changes to the Docker Registry')
        parser_commit.add_argument('--local-container', dest='local_container', required=True,
                                   help='Local Docker container with the corresponding changes')
        parser_commit.add_argument('--remote-image', dest='remote_image', required=True,
                                   help='Image from the Docker Registry to include the new changes made in the'
                                        ' local container')
        parser_commit.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image version')
        parser_commit.add_argument('--force-tag', dest='force_tag', choices=['true', 'false'],
                                   help='Force tag of image')
        parser_commit.set_defaults(func=DockerRegistryToolOperations().commit_image)

        # create the parser for the "download" command
        parser_download = subparsers.add_parser('download', help='Pull an image to the Docker Registry')
        parser_download.add_argument('--remote-image', dest='remote_image', required=True,
                                     help='Image to download from the Docker Registry')
        parser_download.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image version')
        parser_download.set_defaults(func=DockerRegistryToolOperations().download_image)

        # create the parser for the "delete" command
        parser_delete = subparsers.add_parser('delete', help='Remove an image reference in the Docker Registry')
        parser_delete.add_argument('--remote-image', dest='remote_image', required=True,
                                   help='Image to delete from the Docker Registry')
        parser_delete.add_argument('--tag', dest='tag', required=True, help='Tag for identifying the image version')
        parser_delete.set_defaults(func=DockerRegistryToolOperations().delete_image)

        # create the parser for the "version" command
        parser.add_argument('--version', action='version',
                            version='Docker Registry Tool version ' +
                                    DockerRegistryTool().CONST_SCRIPT_VERSION)
        args = parser.parse_args()
        args.func(args)

    @staticmethod
    def check_configuration():
        """ Checks if the settings written in 'docker_registry_tool.conf' are valid or not.
        :return: true if the settings are OK, otherwise returns false.
        """
        parser = SafeConfigParser()
        parser.read('docker_registry_tool.conf')
        registry_address = parser.get('docker_registry_tool', 'RegistryAddress')
        registry_protocol = parser.get('docker_registry_tool', 'RegistryProtocol')
        registry_port = parser.get('docker_registry_tool', 'RegistryPort')
        registry_username = parser.get('docker_registry_tool', 'RegistryUsername')
        registry_password = parser.get('docker_registry_tool', 'RegistryPassword')
        registry_email = parser.get('docker_registry_tool', 'RegistryEmail')
        certificate_path = parser.get('docker_registry_tool', 'CertificatePath')

        if not registry_address:
            print '[ERROR] RegistryAddress variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_protocol:
            print '[ERROR] RegistryProtocol variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_port:
            print '[ERROR] RegistryPort variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_username:
            print '[ERROR] RegistryUsername variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_password:
            print '[ERROR] RegistryPassword variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not registry_email:
            print '[ERROR] RegistryEmail variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        if not certificate_path:
            print '[ERROR] CertificatePath variable is empty in the configuration file. The script will not run until' \
                  ' you configure the script properly'
            return False
        return True


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    DockerRegistryTool().main()
