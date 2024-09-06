
class Actions:
    
    def list_actions(self, ) -> None:
        """
        Return a list of all actions belonging to current user
        
        Args:

        """
    
        print("Calling operation 'list_actions' of service 'Actions' ...")

    def list_actions_by_target_resource_type(self, target_resource_id: int, target_resource_type: str) -> None:
        """
        List actions triggered to a given action target resource
        
        Args:
            target_resource_id (int): The resource ID of the action target.
            target_resource_type (str): The resource type of the action target on which this action will be executed to perform operations on the action resource.

        """
    
        print("Calling operation 'list_actions_by_target_resource_type' of service 'Actions' ...")

    def get_action(self, action_id: int) -> None:
        """
        Get an action by ID
        
        Args:
            action_id (int): The ID of the action.

        """
    
        print("Calling operation 'get_action' of service 'Actions' ...")

    def retry_action(self, action_id: int) -> None:
        """
        Retry an action
        
        Args:
            action_id (int): The ID of the action.

        """
    
        print("Calling operation 'retry_action' of service 'Actions' ...")

    def get_action_log(self, action_id: int, action_step_order: int, action_target_id: int) -> None:
        """
        Get action target step log
        
        Args:
            action_id (int): The ID of the action.
            action_step_order (int): The action step order.
            action_target_id (int): The ID of the action target.

        """
    
        print("Calling operation 'get_action_log' of service 'Actions' ...")

    def list_actions_by_resource_type(self, resource_id: int, resource_type: str) -> None:
        """
        List resource actions of an action type
        
        Args:
            resource_id (int): The resource ID.
            resource_type (str): The resource type to get related actions.

        """
    
        print("Calling operation 'list_actions_by_resource_type' of service 'Actions' ...")

    