
class ResourceLinks:
    
    def list_resource_links_by_resource_type(self, resource_id: int, resource_type: str) -> None:
        """
        List linked resources of the given resource
        
        Args:
            resource_id (int): The resource ID.
            resource_type (str): The resource type to get linked resources.

        """
    
        print("Calling operation 'list_resource_links_by_resource_type' of service 'ResourceLinks' ...")

    def link_resource_link_to_resource_link(self, child_id: int, child_type: str, resource_id: int, resource_type: str) -> None:
        """
        Link the given resources
        
        Args:
            child_id (int): The child resource ID.
            child_type (str): The resource type of the child resource.
            resource_id (int): The parent resource ID.
            resource_type (str): The resource type of the parent resource.

        """
    
        print("Calling operation 'link_resource_link_to_resource_link' of service 'ResourceLinks' ...")

    def unlink_resource_link_from_resource_link(self, child_id: int, child_type: str, resource_id: int, resource_type: str) -> None:
        """
        Delete a given resource link
        
        Args:
            child_id (int): The child resource ID.
            child_type (str): The resource type of the child resource.
            resource_id (int): The parent resource ID.
            resource_type (str): The resource type of the parent resource.

        """
    
        print("Calling operation 'unlink_resource_link_from_resource_link' of service 'ResourceLinks' ...")

    def list_resource_links_by_resource_type_and_link_type(self, link_type: str, resource_id: int, resource_type: str) -> None:
        """
        List linked resources of specified link type
        
        Args:
            link_type (str): The link type (`child` or `parent`).
            resource_id (int): The resource ID.
            resource_type (str): The resource type to get linked resources.

        """
    
        print("Calling operation 'list_resource_links_by_resource_type_and_link_type' of service 'ResourceLinks' ...")

    