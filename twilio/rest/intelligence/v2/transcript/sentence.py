r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Intelligence
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SentenceInstance(InstanceResource):
    """
    :ivar media_channel: The channel number.
    :ivar sentence_index: The index of the sentence in the transcript.
    :ivar start_time: Offset from the beginning of the transcript when this sentence starts.
    :ivar end_time: Offset from the beginning of the transcript when this sentence ends.
    :ivar transcript: Transcript text.
    :ivar sid: A 34 character string that uniquely identifies this Sentence.
    :ivar confidence:
    """

    def __init__(self, version: Version, payload: Dict[str, Any], transcript_sid: str):
        super().__init__(version)

        self.media_channel: Optional[int] = deserialize.integer(
            payload.get("media_channel")
        )
        self.sentence_index: Optional[int] = deserialize.integer(
            payload.get("sentence_index")
        )
        self.start_time: Optional[float] = deserialize.decimal(
            payload.get("start_time")
        )
        self.end_time: Optional[float] = deserialize.decimal(payload.get("end_time"))
        self.transcript: Optional[str] = payload.get("transcript")
        self.sid: Optional[str] = payload.get("sid")
        self.confidence: Optional[float] = deserialize.decimal(
            payload.get("confidence")
        )

        self._solution = {
            "transcript_sid": transcript_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Intelligence.V2.SentenceInstance {}>".format(context)


class SentencePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> SentenceInstance:
        """
        Build an instance of SentenceInstance

        :param payload: Payload response from the API
        """
        return SentenceInstance(
            self._version, payload, transcript_sid=self._solution["transcript_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.SentencePage>"


class SentenceList(ListResource):

    def __init__(self, version: Version, transcript_sid: str):
        """
        Initialize the SentenceList

        :param version: Version that contains the resource
        :param transcript_sid: The unique SID identifier of the Transcript.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "transcript_sid": transcript_sid,
        }
        self._uri = "/Transcripts/{transcript_sid}/Sentences".format(**self._solution)

    def stream(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SentenceInstance]:
        """
        Streams SentenceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool redacted: Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(redacted=redacted, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SentenceInstance]:
        """
        Asynchronously streams SentenceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool redacted: Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(redacted=redacted, page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SentenceInstance]:
        """
        Lists SentenceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool redacted: Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
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
                redacted=redacted,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SentenceInstance]:
        """
        Asynchronously lists SentenceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool redacted: Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
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
                redacted=redacted,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        redacted: Union[bool, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SentencePage:
        """
        Retrieve a single page of SentenceInstance records from the API.
        Request is executed immediately

        :param redacted: Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SentenceInstance
        """
        data = values.of(
            {
                "Redacted": redacted,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SentencePage(self._version, response, self._solution)

    async def page_async(
        self,
        redacted: Union[bool, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SentencePage:
        """
        Asynchronously retrieve a single page of SentenceInstance records from the API.
        Request is executed immediately

        :param redacted: Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SentenceInstance
        """
        data = values.of(
            {
                "Redacted": redacted,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SentencePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SentencePage:
        """
        Retrieve a specific page of SentenceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SentenceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SentencePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SentencePage:
        """
        Asynchronously retrieve a specific page of SentenceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SentenceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SentencePage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.SentenceList>"
