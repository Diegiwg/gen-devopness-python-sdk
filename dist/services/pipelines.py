
class Pipelines:
    
    def delete_pipeline(self, pipeline_id: int) -> None:
        """
        Delete a given Pipeline
        
        Args:
            pipeline_id (int): The ID of the pipeline.

        """
    
        print("Calling operation 'delete_pipeline' of service 'Pipelines' ...")

    def get_pipeline(self, pipeline_id: int) -> None:
        """
        Get a Pipeline by ID
        
        Args:
            pipeline_id (int): The ID of the pipeline.

        """
    
        print("Calling operation 'get_pipeline' of service 'Pipelines' ...")

    def update_pipeline(self, pipeline_id: int) -> None:
        """
        Update an existing Pipeline
        
        Args:
            pipeline_id (int): The ID of the pipeline.

        """
    
        print("Calling operation 'update_pipeline' of service 'Pipelines' ...")

    def list_pipeline_actions(self, pipeline_id: int) -> None:
        """
        Return a list of pipeline's actions
        
        Args:
            pipeline_id (int): The ID of the pipeline.

        """
    
        print("Calling operation 'list_pipeline_actions' of service 'Pipelines' ...")

    def add_pipeline_action(self, pipeline_id: int) -> None:
        """
        Create an action to run a Pipeline
        
        Args:
            pipeline_id (int): The ID of the pipeline that will be executed by the created action

        """
    
        print("Calling operation 'add_pipeline_action' of service 'Pipelines' ...")

    def list_pipeline_hooks(self, pipeline_id: int) -> None:
        """
        List all hooks in a pipeline
        
        Args:
            pipeline_id (int): The ID of the pipeline.

        """
    
        print("Calling operation 'list_pipeline_hooks' of service 'Pipelines' ...")

    def add_pipeline_hook(self, hook_type: str, pipeline_id: int) -> None:
        """
        Create a hook to a specific pipeline
        
        Args:
            hook_type (str): The hook type.
            pipeline_id (int): The ID of the pipeline that will be executed by the created action

        """
    
        print("Calling operation 'add_pipeline_hook' of service 'Pipelines' ...")

    def add_pipeline_step(self, pipeline_id: int) -> None:
        """
        Add a step to a pipeline
        
        Args:
            pipeline_id (int): The ID of the pipeline.

        """
    
        print("Calling operation 'add_pipeline_step' of service 'Pipelines' ...")

    def update_pipeline_step(self, pipeline_id: int, step_id: int) -> None:
        """
        Update an existing Pipeline Step
        
        Args:
            pipeline_id (int): The ID of the pipeline.
            step_id (int): The ID of the step.

        """
    
        print("Calling operation 'update_pipeline_step' of service 'Pipelines' ...")

    def link_step_to_pipeline(self, pipeline_id: int, step_id: int) -> None:
        """
        Link a step to a Pipeline
        
        Args:
            pipeline_id (int): The ID of the pipeline.
            step_id (int): The ID of the step.

        """
    
        print("Calling operation 'link_step_to_pipeline' of service 'Pipelines' ...")

    def unlink_step_from_pipeline(self, pipeline_id: int, step_id: int) -> None:
        """
        Unlink a step from a Pipeline
        
        Args:
            pipeline_id (int): The ID of the pipeline.
            step_id (int): The ID of the step.

        """
    
        print("Calling operation 'unlink_step_from_pipeline' of service 'Pipelines' ...")

    def list_pipelines_by_resource_type(self, resource_id: int, resource_type: str) -> None:
        """
        Return a list of pipelines to a resource
        
        Args:
            resource_id (int): The resource ID.
            resource_type (str): The resource type to get pipelines from.

        """
    
        print("Calling operation 'list_pipelines_by_resource_type' of service 'Pipelines' ...")

    def add_pipeline(self, resource_id: int, resource_type: str) -> None:
        """
        Add a Pipeline to a resource
        
        Args:
            resource_id (int): The resource ID.
            resource_type (str): The resource type to add a pipeline to.

        """
    
        print("Calling operation 'add_pipeline' of service 'Pipelines' ...")

    