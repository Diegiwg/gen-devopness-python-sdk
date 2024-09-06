
class Environments:
    
    def get_environment(self, environment_id: int) -> None:
        """
        Get an environment by ID
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'get_environment' of service 'Environments' ...")

    def update_environment(self, environment_id: int) -> None:
        """
        Update a given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'update_environment' of service 'Environments' ...")

    def list_environment_actions(self, environment_id: int) -> None:
        """
        List environment actions
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_actions' of service 'Environments' ...")

    def list_environment_actions_by_resource_type(self, environment_id: int, resource_type: str) -> None:
        """
        List environment actions of a resource type
        
        Args:
            environment_id (int): The ID of the environment.
            resource_type (str): The resource type to get related actions.

        """
    
        print("Calling operation 'list_environment_actions_by_resource_type' of service 'Environments' ...")

    def list_environment_applications(self, environment_id: int) -> None:
        """
        Return a list of all Applications belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_applications' of service 'Environments' ...")

    def add_environment_application(self, environment_id: int) -> None:
        """
        Create a new application
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_application' of service 'Environments' ...")

    def archive_environment(self, environment_id: int) -> None:
        """
        Archive an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'archive_environment' of service 'Environments' ...")

    def list_environment_credentials(self, environment_id: int) -> None:
        """
        Return a list of all Credentials belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_credentials' of service 'Environments' ...")

    def add_environment_credential(self, environment_id: int) -> None:
        """
        Add a Credential to the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_credential' of service 'Environments' ...")

    def get_environment_credential_settings(self, environment_id: int, provider_code: str) -> None:
        """
        Return provider settings
        
        Args:
            environment_id (int): The ID of the environment.
            provider_code (str): The code of the provider.

        """
    
        print("Calling operation 'get_environment_credential_settings' of service 'Environments' ...")

    def list_environment_cron_jobs(self, environment_id: int) -> None:
        """
        Return a list of all Cron Jobs belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_cron_jobs' of service 'Environments' ...")

    def add_environment_cron_job(self, environment_id: int) -> None:
        """
        Add a Cron Job to the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_cron_job' of service 'Environments' ...")

    def list_environment_daemons(self, environment_id: int) -> None:
        """
        Return a list of all Daemons belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_daemons' of service 'Environments' ...")

    def add_environment_daemon(self, environment_id: int) -> None:
        """
        Add a Daemon to the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_daemon' of service 'Environments' ...")

    def list_environment_network_rules(self, environment_id: int) -> None:
        """
        Return a list of all Network Rules belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_network_rules' of service 'Environments' ...")

    def add_environment_network_rule(self, environment_id: int) -> None:
        """
        Add a Network Rule to the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_network_rule' of service 'Environments' ...")

    def list_environment_networks(self, environment_id: int) -> None:
        """
        Return a list of all networks belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_networks' of service 'Environments' ...")

    def add_environment_network(self, environment_id: int) -> None:
        """
        Create a new network for the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_network' of service 'Environments' ...")

    def list_environment_servers(self, environment_id: int) -> None:
        """
        Return a list of all servers belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_servers' of service 'Environments' ...")

    def add_environment_server(self, environment_id: int) -> None:
        """
        Creates a server and link it to the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_server' of service 'Environments' ...")

    def list_environment_services(self, environment_id: int) -> None:
        """
        Return a list of all services belonging to a environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_services' of service 'Environments' ...")

    def add_environment_service(self, environment_id: int) -> None:
        """
        Add a Service to the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_service' of service 'Environments' ...")

    def list_environment_ssh_keys(self, environment_id: int) -> None:
        """
        Return a list of all SSH keys added to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_ssh_keys' of service 'Environments' ...")

    def add_environment_ssh_key(self, environment_id: int) -> None:
        """
        Create an SSH key and link it to the given environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_ssh_key' of service 'Environments' ...")

    def list_environment_ssl_certificates(self, environment_id: int) -> None:
        """
        Return a list of all SSL Certificates belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_ssl_certificates' of service 'Environments' ...")

    def add_environment_ssl_certificate(self, environment_id: int) -> None:
        """
        Create a new ssl certificate
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_ssl_certificate' of service 'Environments' ...")

    def list_environment_team_memberships(self, environment_id: int) -> None:
        """
        Return a list of teams with access to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_team_memberships' of service 'Environments' ...")

    def link_team_to_environment(self, environment_id: int, team_id: int) -> None:
        """
        Link team to a given environment
        
        Args:
            environment_id (int): The ID of the environment.
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'link_team_to_environment' of service 'Environments' ...")

    def unlink_team_from_environment(self, environment_id: int, team_id: int) -> None:
        """
        Unlink team from the environment
        
        Args:
            environment_id (int): The ID of the environment.
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'unlink_team_from_environment' of service 'Environments' ...")

    def unarchive_environment(self, environment_id: int) -> None:
        """
        Unarchive an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'unarchive_environment' of service 'Environments' ...")

    def list_environment_virtual_hosts(self, environment_id: int) -> None:
        """
        Return a list of all Virtual Hosts belonging to an environment
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'list_environment_virtual_hosts' of service 'Environments' ...")

    def add_environment_virtual_host(self, environment_id: int) -> None:
        """
        Create a new virtual host
        
        Args:
            environment_id (int): The ID of the environment.

        """
    
        print("Calling operation 'add_environment_virtual_host' of service 'Environments' ...")

    