
class Applications:
    
    def delete_application(self, application_id: int) -> None:
        """
        Delete a given application
        
        Args:
            application_id (int): The ID of the application.

        """
    
        print("Calling operation 'delete_application' of service 'Applications' ...")

    def get_application(self, application_id: int) -> None:
        """
        Get an application by ID
        
        Args:
            application_id (int): The ID of the application.

        """
    
        print("Calling operation 'get_application' of service 'Applications' ...")

    def update_application(self, application_id: int) -> None:
        """
        Update an existing application
        
        Args:
            application_id (int): The ID of the application.

        """
    
        print("Calling operation 'update_application' of service 'Applications' ...")

    def add_application_deployment(self, application_id: int) -> None:
        """
        Trigger a new deployment for current application
        
        Args:
            application_id (int): The ID of the application.

        """
    
        print("Calling operation 'add_application_deployment' of service 'Applications' ...")

    def list_application_hooks(self, application_id: int) -> None:
        """
        List all hooks in an application
        
        Args:
            application_id (int): The ID of the application.

        """
    
        print("Calling operation 'list_application_hooks' of service 'Applications' ...")

    def list_application_variables(self, application_id: int) -> None:
        """
        Return a list of variables belonging to an application
        
        Args:
            application_id (int): The ID of the application.

        """
    
        print("Calling operation 'list_application_variables' of service 'Applications' ...")

    def add_application_variable(self, application_id: int) -> None:
        """
        Create a new variable linked to an application
        
        Args:
            application_id (int): The ID of the application.

        """
    
        print("Calling operation 'add_application_variable' of service 'Applications' ...")

    