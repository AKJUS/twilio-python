r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Proxy
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ShortCodeInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the ShortCode resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource.
    :ivar service_sid: The SID of the ShortCode resource's parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    :ivar date_created: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created.
    :ivar date_updated: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated.
    :ivar short_code: The short code's number.
    :ivar iso_country: The ISO Country Code for the short code.
    :ivar capabilities:
    :ivar url: The absolute URL of the ShortCode resource.
    :ivar is_reserved: Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.short_code: Optional[str] = payload.get("short_code")
        self.iso_country: Optional[str] = payload.get("iso_country")
        self.capabilities: Optional[str] = payload.get("capabilities")
        self.url: Optional[str] = payload.get("url")
        self.is_reserved: Optional[bool] = payload.get("is_reserved")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ShortCodeContext] = None

    @property
    def _proxy(self) -> "ShortCodeContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ShortCodeContext for this ShortCodeInstance
        """
        if self._context is None:
            self._context = ShortCodeContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ShortCodeInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ShortCodeInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ShortCodeInstance":
        """
        Fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ShortCodeInstance":
        """
        Asynchronous coroutine to fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, is_reserved: Union[bool, object] = values.unset
    ) -> "ShortCodeInstance":
        """
        Update the ShortCodeInstance

        :param is_reserved: Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated ShortCodeInstance
        """
        return self._proxy.update(
            is_reserved=is_reserved,
        )

    async def update_async(
        self, is_reserved: Union[bool, object] = values.unset
    ) -> "ShortCodeInstance":
        """
        Asynchronous coroutine to update the ShortCodeInstance

        :param is_reserved: Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated ShortCodeInstance
        """
        return await self._proxy.update_async(
            is_reserved=is_reserved,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.ShortCodeInstance {}>".format(context)


class ShortCodeContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the ShortCodeContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/ShortCodes/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the ShortCodeInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ShortCodeInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ShortCodeInstance:
        """
        Fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ShortCodeInstance:
        """
        Asynchronous coroutine to fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self, is_reserved: Union[bool, object] = values.unset
    ) -> ShortCodeInstance:
        """
        Update the ShortCodeInstance

        :param is_reserved: Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated ShortCodeInstance
        """
        data = values.of(
            {
                "IsReserved": is_reserved,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, is_reserved: Union[bool, object] = values.unset
    ) -> ShortCodeInstance:
        """
        Asynchronous coroutine to update the ShortCodeInstance

        :param is_reserved: Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated ShortCodeInstance
        """
        data = values.of(
            {
                "IsReserved": is_reserved,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.ShortCodeContext {}>".format(context)


class ShortCodePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ShortCodeInstance:
        """
        Build an instance of ShortCodeInstance

        :param payload: Payload response from the API
        """
        return ShortCodeInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.ShortCodePage>"


class ShortCodeList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the ShortCodeList

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/ShortCodes".format(**self._solution)

    def create(self, sid: str) -> ShortCodeInstance:
        """
        Create the ShortCodeInstance

        :param sid: The SID of a Twilio [ShortCode](https://www.twilio.com/docs/sms/api/short-code) resource that represents the short code you would like to assign to your Proxy Service.

        :returns: The created ShortCodeInstance
        """
        data = values.of(
            {
                "Sid": sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ShortCodeInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(self, sid: str) -> ShortCodeInstance:
        """
        Asynchronously create the ShortCodeInstance

        :param sid: The SID of a Twilio [ShortCode](https://www.twilio.com/docs/sms/api/short-code) resource that represents the short code you would like to assign to your Proxy Service.

        :returns: The created ShortCodeInstance
        """
        data = values.of(
            {
                "Sid": sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ShortCodeInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ShortCodeInstance]:
        """
        Streams ShortCodeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ShortCodeInstance]:
        """
        Asynchronously streams ShortCodeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ShortCodeInstance]:
        """
        Lists ShortCodeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ShortCodeInstance]:
        """
        Asynchronously lists ShortCodeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ShortCodePage:
        """
        Retrieve a single page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ShortCodeInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ShortCodePage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ShortCodePage:
        """
        Asynchronously retrieve a single page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ShortCodeInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ShortCodePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ShortCodePage:
        """
        Retrieve a specific page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ShortCodeInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ShortCodePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ShortCodePage:
        """
        Asynchronously retrieve a specific page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ShortCodeInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ShortCodePage(self._version, response, self._solution)

    def get(self, sid: str) -> ShortCodeContext:
        """
        Constructs a ShortCodeContext

        :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update.
        """
        return ShortCodeContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> ShortCodeContext:
        """
        Constructs a ShortCodeContext

        :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update.
        """
        return ShortCodeContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.ShortCodeList>"
