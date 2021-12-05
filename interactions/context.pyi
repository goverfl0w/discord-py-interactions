from typing import Any, Dict, List, Optional, Union

from .api.http import HTTPClient
from .api.models.channel import Channel
from .api.models.guild import Guild
from .api.models.member import Member
from .api.models.message import Embed, Message, MessageInteraction, MessageReference
from .api.models.misc import DictSerializerMixin
from .api.models.user import User
from .enums import ComponentType, InteractionType
from .models.command import Choice
from .models.component import Component
from .models.misc import InteractionData

class Context(DictSerializerMixin):
    message: Message
    member: Member
    user: User
    channel: Channel
    guild: Guild
    client: HTTPClient

    # TODO: AFTER v4: Alias author for member.
    def __init__(self, **kwargs) -> None: ...

class InteractionContext(Context):

    id: str
    application_id: str
    type: Union[int, InteractionType]
    data: InteractionData
    guild_id: str
    channel_id: str
    token: str
    version: int = 1
    responded: bool
    deferred: bool
    def __init__(self, **kwargs) -> None: ...
    async def send(
        self,
        content: Optional[str] = None,
        *,
        tts: Optional[bool] = None,
        # file: Optional[FileIO] = None,
        embeds: Optional[Union[Embed, List[Embed]]] = None,
        allowed_mentions: Optional[MessageInteraction] = None,
        message_reference: Optional[MessageReference] = None,
        components: Optional[Union[Component, List[Component]]] = None,
        sticker_ids: Optional[Union[str, List[str]]] = None,
        type: Optional[int] = None,
        flags: Optional[int] = None,
    ) -> Message: ...

class ComponentContext(InteractionContext):

    custom_id: str
    type: Union[str, int, ComponentType]
    values: list
    origin: bool
    def __init__(self, **kwargs) -> None: ...

class AutocompleteContext(Context):
    def __init__(self, **kwargs) -> None: ...
    async def populate(self, choices: Union[Choice, List[Choice]]) -> List[Choice]: ...
