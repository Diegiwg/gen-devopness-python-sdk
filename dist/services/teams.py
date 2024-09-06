
class Teams:
    
    def delete_team(self, team_id: int) -> None:
        """
        Delete a given team
        
        Args:
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'delete_team' of service 'Teams' ...")

    def get_team(self, team_id: int) -> None:
        """
        Get a team by ID
        
        Args:
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'get_team' of service 'Teams' ...")

    def update_team(self, team_id: int) -> None:
        """
        Update an existing team
        
        Args:
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'update_team' of service 'Teams' ...")

    def list_team_invitations(self, team_id: int) -> None:
        """
        Return a list of pending invitations belonging to a team
        
        Args:
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'list_team_invitations' of service 'Teams' ...")

    def add_team_invitation(self, team_id: int) -> None:
        """
        Send invitation to user email to participate to a team
        
        Args:
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'add_team_invitation' of service 'Teams' ...")

    def list_team_members(self, team_id: int) -> None:
        """
        Return a list of all members belonging to a team
        
        Args:
            team_id (int): The ID of the team.

        """
    
        print("Calling operation 'list_team_members' of service 'Teams' ...")

    def delete_team_member(self, team_id: int, user_id: int) -> None:
        """
        Delete a given team member
        
        Args:
            team_id (int): The ID of the team.
            user_id (int): The ID of the user.

        """
    
        print("Calling operation 'delete_team_member' of service 'Teams' ...")

    def get_team_member(self, team_id: int, user_id: int) -> None:
        """
        Get a member of team by ID
        
        Args:
            team_id (int): The ID of the team.
            user_id (int): The ID of the user.

        """
    
        print("Calling operation 'get_team_member' of service 'Teams' ...")

    