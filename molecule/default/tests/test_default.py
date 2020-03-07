import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_sources_file(host):
    file = host.file("/etc/apt/sources.list.d/hetzner-mirror.list")
    assert file.exists
    assert file.contains("http://mirror.hetzner.de/ubuntu/packages")
