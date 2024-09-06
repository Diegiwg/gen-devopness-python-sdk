
class Servers:
    
    def delete_server(self, server_id: int) -> None:
        """
        Delete a given server
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'delete_server' of service 'Servers' ...")

    def get_server(self, server_id: int) -> None:
        """
        Get a server by ID
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'get_server' of service 'Servers' ...")

    def update_server(self, server_id: int) -> None:
        """
        Update an existing server
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'update_server' of service 'Servers' ...")

    def get_server_commands(self, server_id: int) -> None:
        """
        Get commands to be executed on the given server
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'get_server_commands' of service 'Servers' ...")

    def connect_server(self, activation_token: str, server_id: int) -> None:
        """
        Connect a server to devopness platform
        
        Args:
            activation_token (str): The server activation token.
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'connect_server' of service 'Servers' ...")

    def get_status_server(self, server_id: int) -> None:
        """
        Get current status of the server on the cloud provider
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'get_status_server' of service 'Servers' ...")

    def restart_server(self, server_id: int) -> None:
        """
        Restart a current running server
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'restart_server' of service 'Servers' ...")

    def start_server(self, server_id: int) -> None:
        """
        Start a previously stopped server
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'start_server' of service 'Servers' ...")

    def stop_server(self, server_id: int) -> None:
        """
        Stop a running server
        
        Args:
            server_id (int): The ID of the server.

        """
    
        print("Calling operation 'stop_server' of service 'Servers' ...")

    