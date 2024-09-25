r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Assistants
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class MessageInstance(InstanceResource):
    """
    :ivar status: success or failure based on whether the request successfully generated a response.
    :ivar flagged: If successful, this property will denote whether the response was flagged or not.
    :ivar aborted: This property will denote whether the request was aborted or not.
    :ivar session_id: The unique name for the session.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that sent the Message.
    :ivar body: If successful, the body of the generated response
    :ivar error: The error message if generation was not successful
    """

    def __init__(self, version: Version, payload: Dict[str, Any], id: str):
        super().__init__(version)

        self.status: Optional[str] = payload.get("status")
        self.flagged: Optional[bool] = payload.get("flagged")
        self.aborted: Optional[bool] = payload.get("aborted")
        self.session_id: Optional[str] = payload.get("session_id")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.body: Optional[str] = payload.get("body")
        self.error: Optional[str] = payload.get("error")

        self._solution = {
            "id": id,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Assistants.V1.MessageInstance {}>".format(context)


class MessageList(ListResource):

    class AssistantsV1ServiceAssistantSendMessageRequest(object):
        """
        :ivar identity: The unique identity of user for the session.
        :ivar session_id: The unique name for the session.
        :ivar body: The query to ask the assistant.
        :ivar webhook: The webhook url to call after the assistant has generated a response or report an error.
        :ivar mode: one of the modes 'chat', 'email' or 'voice'
        """

        def __init__(self, payload: Dict[str, Any]):

            self.identity: Optional[str] = payload.get("identity")
            self.session_id: Optional[str] = payload.get("session_id")
            self.body: Optional[str] = payload.get("body")
            self.webhook: Optional[str] = payload.get("webhook")
            self.mode: Optional[str] = payload.get("mode")

        def to_dict(self):
            return {
                "identity": self.identity,
                "session_id": self.session_id,
                "body": self.body,
                "webhook": self.webhook,
                "mode": self.mode,
            }

    def __init__(self, version: Version, id: str):
        """
        Initialize the MessageList

        :param version: Version that contains the resource
        :param id: the Assistant ID.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "id": id,
        }
        self._uri = "/Assistants/{id}/Messages".format(**self._solution)

    def create(
        self,
        assistants_v1_service_assistant_send_message_request: AssistantsV1ServiceAssistantSendMessageRequest,
    ) -> MessageInstance:
        """
        Create the MessageInstance

        :param assistants_v1_service_assistant_send_message_request:

        :returns: The created MessageInstance
        """
        data = assistants_v1_service_assistant_send_message_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(self._version, payload, id=self._solution["id"])

    async def create_async(
        self,
        assistants_v1_service_assistant_send_message_request: AssistantsV1ServiceAssistantSendMessageRequest,
    ) -> MessageInstance:
        """
        Asynchronously create the MessageInstance

        :param assistants_v1_service_assistant_send_message_request:

        :returns: The created MessageInstance
        """
        data = assistants_v1_service_assistant_send_message_request.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})
        headers["Content-Type"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(self._version, payload, id=self._solution["id"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Assistants.V1.MessageList>"
