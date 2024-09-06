
class Hooks:
    
    def trigger_hook(self, hook_id: str) -> None:
        """
        Trigger an incoming hook associated action
        
        Args:
            hook_id (str): The ID of the hook.

        """
    
        print("Calling operation 'trigger_hook' of service 'Hooks' ...")

    def delete_hook(self, hook_id: str, hook_type: str) -> None:
        """
        Delete a given hook
        
        Args:
            hook_id (str): The ID of the hook.
            hook_type (str): The hook type.

        """
    
        print("Calling operation 'delete_hook' of service 'Hooks' ...")

    def get_hook(self, hook_id: str, hook_type: str) -> None:
        """
        Get a hook by ID
        
        Args:
            hook_id (str): The ID of the hook.
            hook_type (str): The hook type.

        """
    
        print("Calling operation 'get_hook' of service 'Hooks' ...")

    def update_hook(self, hook_id: str, hook_type: str) -> None:
        """
        Update an existing hook
        
        Args:
            hook_id (str): The ID of the hook.
            hook_type (str): The hook type.

        """
    
        print("Calling operation 'update_hook' of service 'Hooks' ...")

    def list_hook_requests_by_hook_type(self, hook_id: str, hook_type: str) -> None:
        """
        Returns a list of all hook requests belonging to a hook
        
        Args:
            hook_id (str): The ID of the hook.
            hook_type (str): The hook type.

        """
    
        print("Calling operation 'list_hook_requests_by_hook_type' of service 'Hooks' ...")

    