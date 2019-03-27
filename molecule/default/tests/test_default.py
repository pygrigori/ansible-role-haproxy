import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    package = host.package('haproxy')

    assert package.is_installed


def test_service_is_enabled(host):
    service = host.service('haproxy')

    assert service.is_enabled


def test_config_exists(host):
    file = host.file('/etc/haproxy/haproxy.cfg')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_config_is_valid(host):
    cmd = host.run('haproxy -c -f /etc/haproxy/haproxy.cfg')

    assert not cmd.rc
