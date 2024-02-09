r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SettingsInstance(InstanceResource):
    """
    :ivar dialing_permissions_inheritance: `true` if the sub-account will inherit voice dialing permissions from the Master Project; otherwise `false`.
    :ivar url: The absolute URL of this resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.dialing_permissions_inheritance: Optional[bool] = payload.get(
            "dialing_permissions_inheritance"
        )
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[SettingsContext] = None

    @property
    def _proxy(self) -> "SettingsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SettingsContext for this SettingsInstance
        """
        if self._context is None:
            self._context = SettingsContext(
                self._version,
            )
        return self._context

    def fetch(self) -> "SettingsInstance":
        """
        Fetch the SettingsInstance


        :returns: The fetched SettingsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SettingsInstance":
        """
        Asynchronous coroutine to fetch the SettingsInstance


        :returns: The fetched SettingsInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, dialing_permissions_inheritance: Union[bool, object] = values.unset
    ) -> "SettingsInstance":
        """
        Update the SettingsInstance

        :param dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        """
        return self._proxy.update(
            dialing_permissions_inheritance=dialing_permissions_inheritance,
        )

    async def update_async(
        self, dialing_permissions_inheritance: Union[bool, object] = values.unset
    ) -> "SettingsInstance":
        """
        Asynchronous coroutine to update the SettingsInstance

        :param dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        """
        return await self._proxy.update_async(
            dialing_permissions_inheritance=dialing_permissions_inheritance,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Voice.V1.SettingsInstance>"


class SettingsContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the SettingsContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Settings"

    def fetch(self) -> SettingsInstance:
        """
        Fetch the SettingsInstance


        :returns: The fetched SettingsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SettingsInstance(
            self._version,
            payload,
        )

    async def fetch_async(self) -> SettingsInstance:
        """
        Asynchronous coroutine to fetch the SettingsInstance


        :returns: The fetched SettingsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SettingsInstance(
            self._version,
            payload,
        )

    def update(
        self, dialing_permissions_inheritance: Union[bool, object] = values.unset
    ) -> SettingsInstance:
        """
        Update the SettingsInstance

        :param dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        """
        data = values.of(
            {
                "DialingPermissionsInheritance": dialing_permissions_inheritance,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SettingsInstance(self._version, payload)

    async def update_async(
        self, dialing_permissions_inheritance: Union[bool, object] = values.unset
    ) -> SettingsInstance:
        """
        Asynchronous coroutine to update the SettingsInstance

        :param dialing_permissions_inheritance: `true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

        :returns: The updated SettingsInstance
        """
        data = values.of(
            {
                "DialingPermissionsInheritance": dialing_permissions_inheritance,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SettingsInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Voice.V1.SettingsContext>"


class SettingsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SettingsList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> SettingsContext:
        """
        Constructs a SettingsContext

        """
        return SettingsContext(self._version)

    def __call__(self) -> SettingsContext:
        """
        Constructs a SettingsContext

        """
        return SettingsContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.SettingsList>"
