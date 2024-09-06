from dist.services.virtual_hosts import VirtualHosts
from dist.services.environments import Environments

virtual_hosts = VirtualHosts()
virtual_hosts.get_status_virtual_host()

environments = Environments()
environments.list_environment_applications
