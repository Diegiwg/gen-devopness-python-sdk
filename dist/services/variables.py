
class Variables:
    
    def list_variables_by_resource_type(self, resource_id: int, resource_type: str) -> None:
        """
        Return a list of variables belonging to a resource
        
        Args:
            resource_id (int): The resource ID.
            resource_type (str): The resource type to get variables from.

        """
    
        print("Calling operation 'list_variables_by_resource_type' of service 'Variables' ...")

    def add_variable(self, resource_id: int, resource_type: str) -> None:
        """
        Create a new variable linked to a resource
        
        Args:
            resource_id (int): The resource ID.
            resource_type (str): The resource type to get variables from.

        """
    
        print("Calling operation 'add_variable' of service 'Variables' ...")

    def delete_variable(self, variable_id: int) -> None:
        """
        Delete a variable by ID
        
        Args:
            variable_id (int): The ID of the variable.

        """
    
        print("Calling operation 'delete_variable' of service 'Variables' ...")

    def get_variable(self, variable_id: int) -> None:
        """
        Get a variable by ID
        
        Args:
            variable_id (int): The ID of the variable.

        """
    
        print("Calling operation 'get_variable' of service 'Variables' ...")

    def update_variable(self, variable_id: int) -> None:
        """
        Update an existing variable
        
        Args:
            variable_id (int): The ID of the variable.

        """
    
        print("Calling operation 'update_variable' of service 'Variables' ...")

    