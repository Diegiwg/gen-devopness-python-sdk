
class Credentials:
    
    def delete_credential(self, credential_id: int) -> None:
        """
        Delete a given credential
        
        Args:
            credential_id (int): The ID of the credential.

        """
    
        print("Calling operation 'delete_credential' of service 'Credentials' ...")

    def get_credential(self, credential_id: int) -> None:
        """
        Get a credential by ID
        
        Args:
            credential_id (int): The ID of the credential.

        """
    
        print("Calling operation 'get_credential' of service 'Credentials' ...")

    def update_credential(self, credential_id: int) -> None:
        """
        Update an existing Credential
        
        Args:
            credential_id (int): The ID of the credential.

        """
    
        print("Calling operation 'update_credential' of service 'Credentials' ...")

    def get_status_credential(self, credential_id: int) -> None:
        """
        Get current status of a credential on its provider
        
        Args:
            credential_id (int): The ID of the credential.

        """
    
        print("Calling operation 'get_status_credential' of service 'Credentials' ...")

    def list_credential_repositories(self, credential_id: int) -> None:
        """
        Return a list of all repositories belonging to the source provider linked to the credential
        
        Args:
            credential_id (int): The ID of the credential.

        """
    
        print("Calling operation 'list_credential_repositories' of service 'Credentials' ...")

    def get_credential_repository(self, credential_id: int, repository_name: str, repository_owner: str) -> None:
        """
        Get details of a repository by its name
        
        Args:
            credential_id (int): The ID of the credential.
            repository_name (str): The repository name
            repository_owner (str): The owner of the repository

        """
    
        print("Calling operation 'get_credential_repository' of service 'Credentials' ...")

    