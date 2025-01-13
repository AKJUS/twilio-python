r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TranscriptionInstance(InstanceResource):

    class Status(object):
        IN_PROGRESS = "in-progress"
        STOPPED = "stopped"

    class Track(object):
        INBOUND_TRACK = "inbound_track"
        OUTBOUND_TRACK = "outbound_track"
        BOTH_TRACKS = "both_tracks"

    class UpdateStatus(object):
        STOPPED = "stopped"

    """
    :ivar sid: The SID of the Transcription resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Transcription resource.
    :ivar call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Transcription resource is associated with.
    :ivar name: The user-specified name of this Transcription, if one was given when the Transcription was created. This may be used to stop the Transcription.
    :ivar status: 
    :ivar date_updated: The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar uri: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        call_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.name: Optional[str] = payload.get("name")
        self.status: Optional["TranscriptionInstance.Status"] = payload.get("status")
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[TranscriptionContext] = None

    @property
    def _proxy(self) -> "TranscriptionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TranscriptionContext for this TranscriptionInstance
        """
        if self._context is None:
            self._context = TranscriptionContext(
                self._version,
                account_sid=self._solution["account_sid"],
                call_sid=self._solution["call_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def update(
        self, status: "TranscriptionInstance.UpdateStatus"
    ) -> "TranscriptionInstance":
        """
        Update the TranscriptionInstance

        :param status:

        :returns: The updated TranscriptionInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(
        self, status: "TranscriptionInstance.UpdateStatus"
    ) -> "TranscriptionInstance":
        """
        Asynchronous coroutine to update the TranscriptionInstance

        :param status:

        :returns: The updated TranscriptionInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.TranscriptionInstance {}>".format(context)


class TranscriptionContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        """
        Initialize the TranscriptionContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Transcription resource.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Transcription resource is associated with.
        :param sid: The SID of the Transcription resource, or the `name` used when creating the resource
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Calls/{call_sid}/Transcriptions/{sid}.json".format(
                **self._solution
            )
        )

    def update(
        self, status: "TranscriptionInstance.UpdateStatus"
    ) -> TranscriptionInstance:
        """
        Update the TranscriptionInstance

        :param status:

        :returns: The updated TranscriptionInstance
        """

        data = values.of(
            {
                "Status": status,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, status: "TranscriptionInstance.UpdateStatus"
    ) -> TranscriptionInstance:
        """
        Asynchronous coroutine to update the TranscriptionInstance

        :param status:

        :returns: The updated TranscriptionInstance
        """

        data = values.of(
            {
                "Status": status,
            }
        )
        headers = values.of({})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.TranscriptionContext {}>".format(context)


class TranscriptionList(ListResource):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the TranscriptionList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Transcription resource.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Transcription resource is associated with.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Calls/{call_sid}/Transcriptions.json".format(
                **self._solution
            )
        )

    def create(
        self,
        name: Union[str, object] = values.unset,
        track: Union["TranscriptionInstance.Track", object] = values.unset,
        status_callback_url: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        inbound_track_label: Union[str, object] = values.unset,
        outbound_track_label: Union[str, object] = values.unset,
        partial_results: Union[bool, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        transcription_engine: Union[str, object] = values.unset,
        profanity_filter: Union[bool, object] = values.unset,
        speech_model: Union[str, object] = values.unset,
        hints: Union[str, object] = values.unset,
        enable_automatic_punctuation: Union[bool, object] = values.unset,
        intelligence_service: Union[str, object] = values.unset,
    ) -> TranscriptionInstance:
        """
        Create the TranscriptionInstance

        :param name: The user-specified name of this Transcription, if one was given when the Transcription was created. This may be used to stop the Transcription.
        :param track:
        :param status_callback_url: Absolute URL of the status callback.
        :param status_callback_method: The http method for the status_callback (one of GET, POST).
        :param inbound_track_label: Friendly name given to the Inbound Track
        :param outbound_track_label: Friendly name given to the Outbound Track
        :param partial_results: Indicates if partial results are going to be sent to the customer
        :param language_code: Language code used by the transcription engine, specified in [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) format
        :param transcription_engine: Definition of the transcription engine to be used, among those supported by Twilio
        :param profanity_filter: indicates if the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks
        :param speech_model: Recognition model used by the transcription engine, among those supported by the provider
        :param hints: A Phrase contains words and phrase \\\"hints\\\" so that the speech recognition engine is more likely to recognize them.
        :param enable_automatic_punctuation: The provider will add punctuation to recognition result
        :param intelligence_service: The SID of the [Voice Intelligence Service](https://www.twilio.com/docs/voice/intelligence/api/service-resource) for persisting transcripts and running post-call Language Operators .

        :returns: The created TranscriptionInstance
        """

        data = values.of(
            {
                "Name": name,
                "Track": track,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "InboundTrackLabel": inbound_track_label,
                "OutboundTrackLabel": outbound_track_label,
                "PartialResults": serialize.boolean_to_string(partial_results),
                "LanguageCode": language_code,
                "TranscriptionEngine": transcription_engine,
                "ProfanityFilter": serialize.boolean_to_string(profanity_filter),
                "SpeechModel": speech_model,
                "Hints": hints,
                "EnableAutomaticPunctuation": serialize.boolean_to_string(
                    enable_automatic_punctuation
                ),
                "IntelligenceService": intelligence_service,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    async def create_async(
        self,
        name: Union[str, object] = values.unset,
        track: Union["TranscriptionInstance.Track", object] = values.unset,
        status_callback_url: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        inbound_track_label: Union[str, object] = values.unset,
        outbound_track_label: Union[str, object] = values.unset,
        partial_results: Union[bool, object] = values.unset,
        language_code: Union[str, object] = values.unset,
        transcription_engine: Union[str, object] = values.unset,
        profanity_filter: Union[bool, object] = values.unset,
        speech_model: Union[str, object] = values.unset,
        hints: Union[str, object] = values.unset,
        enable_automatic_punctuation: Union[bool, object] = values.unset,
        intelligence_service: Union[str, object] = values.unset,
    ) -> TranscriptionInstance:
        """
        Asynchronously create the TranscriptionInstance

        :param name: The user-specified name of this Transcription, if one was given when the Transcription was created. This may be used to stop the Transcription.
        :param track:
        :param status_callback_url: Absolute URL of the status callback.
        :param status_callback_method: The http method for the status_callback (one of GET, POST).
        :param inbound_track_label: Friendly name given to the Inbound Track
        :param outbound_track_label: Friendly name given to the Outbound Track
        :param partial_results: Indicates if partial results are going to be sent to the customer
        :param language_code: Language code used by the transcription engine, specified in [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) format
        :param transcription_engine: Definition of the transcription engine to be used, among those supported by Twilio
        :param profanity_filter: indicates if the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks
        :param speech_model: Recognition model used by the transcription engine, among those supported by the provider
        :param hints: A Phrase contains words and phrase \\\"hints\\\" so that the speech recognition engine is more likely to recognize them.
        :param enable_automatic_punctuation: The provider will add punctuation to recognition result
        :param intelligence_service: The SID of the [Voice Intelligence Service](https://www.twilio.com/docs/voice/intelligence/api/service-resource) for persisting transcripts and running post-call Language Operators .

        :returns: The created TranscriptionInstance
        """

        data = values.of(
            {
                "Name": name,
                "Track": track,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "InboundTrackLabel": inbound_track_label,
                "OutboundTrackLabel": outbound_track_label,
                "PartialResults": serialize.boolean_to_string(partial_results),
                "LanguageCode": language_code,
                "TranscriptionEngine": transcription_engine,
                "ProfanityFilter": serialize.boolean_to_string(profanity_filter),
                "SpeechModel": speech_model,
                "Hints": hints,
                "EnableAutomaticPunctuation": serialize.boolean_to_string(
                    enable_automatic_punctuation
                ),
                "IntelligenceService": intelligence_service,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    def get(self, sid: str) -> TranscriptionContext:
        """
        Constructs a TranscriptionContext

        :param sid: The SID of the Transcription resource, or the `name` used when creating the resource
        """
        return TranscriptionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> TranscriptionContext:
        """
        Constructs a TranscriptionContext

        :param sid: The SID of the Transcription resource, or the `name` used when creating the resource
        """
        return TranscriptionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.TranscriptionList>"
