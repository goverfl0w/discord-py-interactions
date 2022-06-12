from typing import List, Optional

from ...api.cache import Cache
from ..models.role import Role
from .request import _Request

class GuildRequest:

    _req: _Request
    cache: Cache
    def __init__(self) -> None: ...
    async def get_self_guilds(self) -> List[dict]: ...
    async def get_guild(self, guild_id: int) -> dict: ...
    async def get_guild_preview(self, guild_id: int) -> dict: ...
    async def modify_guild(
        self, guild_id: int, payload: dict, reason: Optional[str] = None
    ) -> dict: ...
    async def leave_guild(self, guild_id: int) -> None: ...
    async def delete_guild(self, guild_id: int) -> None: ...
    async def get_guild_widget(self, guild_id: int) -> dict: ...
    async def get_guild_widget_settings(self, guild_id: int) -> dict: ...
    async def get_guild_widget_image(self, guild_id: int, style: Optional[str] = None) -> str: ...
    async def modify_guild_widget(self, guild_id: int, payload: dict) -> dict: ...
    async def get_guild_invites(self, guild_id: int) -> List[dict]: ...
    async def get_guild_welcome_screen(self, guild_id: int) -> dict: ...
    async def modify_guild_welcome_screen(
        self, guild_id: int, enabled: bool, welcome_channels: List[int], description: str
    ) -> dict: ...
    async def get_vanity_code(self, guild_id: int) -> dict: ...
    async def modify_vanity_code(
        self, guild_id: int, code: str, reason: Optional[str] = None
    ) -> None: ...
    async def get_guild_integrations(self, guild_id: int) -> List[dict]: ...
    async def delete_guild_integration(self, guild_id: int, integration_id: int) -> None: ...
    async def modify_current_user_voice_state(
        self,
        guild_id: int,
        channel_id: int,
        suppress: Optional[bool] = None,
        request_to_speak_timestamp: Optional[str] = None,
    ) -> None: ...
    async def modify_user_voice_state(
        self, guild_id: int, user_id: int, channel_id: int, suppress: Optional[bool] = None
    ) -> None: ...
    async def create_guild_from_guild_template(
        self, template_code: str, name: str, icon: Optional[str] = None
    ) -> dict: ...
    async def get_guild_templates(self, guild_id: int) -> List[dict]: ...
    async def create_guild_template(
        self, guild_id: int, name: str, description: Optional[str] = None
    ) -> dict: ...
    async def sync_guild_template(self, guild_id: int, template_code: str) -> dict: ...
    async def modify_guild_template(
        self,
        guild_id: int,
        template_code: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> dict: ...
    async def delete_guild_template(self, guild_id: int, template_code: str) -> dict: ...
    async def get_all_channels(self, guild_id: int) -> List[dict]: ...
    async def get_all_roles(self, guild_id: int) -> List[dict]: ...
    async def create_guild_role(
        self, guild_id: int, payload: dict, reason: Optional[str] = None
    ) -> dict: ...
    async def modify_guild_role_positions(
        self, guild_id: int, payload: List[dict], reason: Optional[str] = None
    ) -> List[dict]: ...
    async def modify_guild_role(
        self, guild_id: int, role_id: int, payload: dict, reason: Optional[str] = None
    ) -> dict: ...
    async def delete_guild_role(self, guild_id: int, role_id: int, reason: str = None) -> None: ...
    async def create_guild_kick(
        self, guild_id: int, user_id: int, reason: Optional[str] = None
    ) -> None: ...
    async def create_guild_ban(
        self,
        guild_id: int,
        user_id: int,
        delete_message_days: Optional[int] = 0,
        reason: Optional[str] = None,
    ) -> None: ...
    async def remove_guild_ban(
        self, guild_id: int, user_id: int, reason: Optional[str] = None
    ) -> None: ...
    async def get_guild_bans(
        self,
        guild_id: int,
        limit: Optional[int] = 1000,
        before: Optional[int] = None,
        after: Optional[int] = None,
    ) -> List[dict]: ...
    async def get_user_ban(self, guild_id: int, user_id: int) -> Optional[dict]: ...
    async def add_guild_member(
        self,
        guild_id: int,
        user_id: int,
        access_token: str,
        nick: Optional[str] = None,
        roles: Optional[List[Role]] = None,
        mute: bool = None,
        deaf: bool = None,
    ) -> dict: ...
    async def remove_guild_member(
        self, guild_id: int, user_id: int, reason: Optional[str] = None
    ) -> None: ...
    async def get_guild_prune_count(
        self, guild_id: int, days: int = 7, include_roles: Optional[List[int]] = None
    ) -> dict: ...
    async def get_guild_auditlog(
        self,
        guild_id: int,
        user_id: Optional[int] = None,
        action_type: Optional[int] = None,
        before: Optional[int] = None,
        limit: int = 50,
    ) -> dict: ...
