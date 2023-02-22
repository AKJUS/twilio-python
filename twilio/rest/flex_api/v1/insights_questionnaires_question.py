# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class InsightsQuestionnairesQuestionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the InsightsQuestionnairesQuestionList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionList
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionList
        """
        super(InsightsQuestionnairesQuestionList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Insights/QM/Questions'.format(**self._solution)

    def create(self, category_id, question, description, answer_set_id, allow_na,
               token=values.unset):
        """
        Create the InsightsQuestionnairesQuestionInstance

        :param unicode category_id: Category ID
        :param unicode question: The question.
        :param unicode description: The question description.
        :param unicode answer_set_id: The answer_set for question.
        :param bool allow_na: Flag to enable NA for answer.
        :param unicode token: The Token HTTP request header

        :returns: The created InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        data = values.of({
            'CategoryId': category_id,
            'Question': question,
            'Description': description,
            'AnswerSetId': answer_set_id,
            'AllowNa': allow_na,
        })
        headers = values.of({'Token': token, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers, )

        return InsightsQuestionnairesQuestionInstance(self._version, payload, )

    def stream(self, category_id=values.unset, token=values.unset, limit=None,
               page_size=None):
        """
        Streams InsightsQuestionnairesQuestionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param list[unicode] category_id: List of category Ids
        :param unicode token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(category_id=category_id, token=token, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, category_id=values.unset, token=values.unset, limit=None,
             page_size=None):
        """
        Lists InsightsQuestionnairesQuestionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param list[unicode] category_id: List of category Ids
        :param unicode token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance]
        """
        return list(self.stream(category_id=category_id, token=token, limit=limit, page_size=page_size, ))

    def page(self, category_id=values.unset, token=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of InsightsQuestionnairesQuestionInstance records from the API.
        Request is executed immediately

        :param list[unicode] category_id: List of category Ids
        :param unicode token: The Token HTTP request header
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        """
        data = values.of({
            'CategoryId': serialize.map(category_id, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        headers = values.of({'Token': token, })

        response = self._version.page(method='GET', uri=self._uri, params=data, headers=headers, )

        return InsightsQuestionnairesQuestionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InsightsQuestionnairesQuestionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return InsightsQuestionnairesQuestionPage(self._version, response, self._solution)

    def get(self, question_id):
        """
        Constructs a InsightsQuestionnairesQuestionContext

        :param question_id: Unique Question ID

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        return InsightsQuestionnairesQuestionContext(self._version, question_id=question_id, )

    def __call__(self, question_id):
        """
        Constructs a InsightsQuestionnairesQuestionContext

        :param question_id: Unique Question ID

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        return InsightsQuestionnairesQuestionContext(self._version, question_id=question_id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionList>'


class InsightsQuestionnairesQuestionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the InsightsQuestionnairesQuestionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionPage
        """
        super(InsightsQuestionnairesQuestionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InsightsQuestionnairesQuestionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        return InsightsQuestionnairesQuestionInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionPage>'


class InsightsQuestionnairesQuestionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, question_id):
        """
        Initialize the InsightsQuestionnairesQuestionContext

        :param Version version: Version that contains the resource
        :param question_id: Unique Question ID

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        super(InsightsQuestionnairesQuestionContext, self).__init__(version)

        # Path Solution
        self._solution = {'question_id': question_id, }
        self._uri = '/Insights/QM/Questions/{question_id}'.format(**self._solution)

    def update(self, allow_na, category_id=values.unset, question=values.unset,
               description=values.unset, answer_set_id=values.unset,
               token=values.unset):
        """
        Update the InsightsQuestionnairesQuestionInstance

        :param bool allow_na: Flag to enable NA for answer.
        :param unicode category_id: Category ID
        :param unicode question: The question.
        :param unicode description: The question description.
        :param unicode answer_set_id: The answer_set for question.
        :param unicode token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        data = values.of({
            'AllowNa': allow_na,
            'CategoryId': category_id,
            'Question': question,
            'Description': description,
            'AnswerSetId': answer_set_id,
        })
        headers = values.of({'Token': token, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers, )

        return InsightsQuestionnairesQuestionInstance(
            self._version,
            payload,
            question_id=self._solution['question_id'],
        )

    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesQuestionInstance

        :param unicode token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'Token': token, })

        return self._version.delete(method='DELETE', uri=self._uri, headers=headers, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionContext {}>'.format(context)


class InsightsQuestionnairesQuestionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, question_id=None):
        """
        Initialize the InsightsQuestionnairesQuestionInstance

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        super(InsightsQuestionnairesQuestionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'question_id': payload.get('question_id'),
            'question': payload.get('question'),
            'description': payload.get('description'),
            'category': payload.get('category'),
            'answer_set_id': payload.get('answer_set_id'),
            'allow_na': payload.get('allow_na'),
            'usage': deserialize.integer(payload.get('usage')),
            'answer_set': payload.get('answer_set'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'question_id': question_id or self._properties['question_id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: InsightsQuestionnairesQuestionContext for this InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionContext
        """
        if self._context is None:
            self._context = InsightsQuestionnairesQuestionContext(
                self._version,
                question_id=self._solution['question_id'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource and owns this Flex Insights
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def question_id(self):
        """
        :returns: Unique Question ID
        :rtype: unicode
        """
        return self._properties['question_id']

    @property
    def question(self):
        """
        :returns: The question.
        :rtype: unicode
        """
        return self._properties['question']

    @property
    def description(self):
        """
        :returns: The question description.
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def category(self):
        """
        :returns: The question category.
        :rtype: dict
        """
        return self._properties['category']

    @property
    def answer_set_id(self):
        """
        :returns: The answer_set for question.
        :rtype: unicode
        """
        return self._properties['answer_set_id']

    @property
    def allow_na(self):
        """
        :returns: Flag to enable NA for answer.
        :rtype: bool
        """
        return self._properties['allow_na']

    @property
    def usage(self):
        """
        :returns: Questions usage
        :rtype: unicode
        """
        return self._properties['usage']

    @property
    def answer_set(self):
        """
        :returns: Question's Answer set
        :rtype: dict
        """
        return self._properties['answer_set']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, allow_na, category_id=values.unset, question=values.unset,
               description=values.unset, answer_set_id=values.unset,
               token=values.unset):
        """
        Update the InsightsQuestionnairesQuestionInstance

        :param bool allow_na: Flag to enable NA for answer.
        :param unicode category_id: Category ID
        :param unicode question: The question.
        :param unicode description: The question description.
        :param unicode answer_set_id: The answer_set for question.
        :param unicode token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesQuestionInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_question.InsightsQuestionnairesQuestionInstance
        """
        return self._proxy.update(
            allow_na,
            category_id=category_id,
            question=question,
            description=description,
            answer_set_id=answer_set_id,
            token=token,
        )

    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesQuestionInstance

        :param unicode token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(token=token, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesQuestionInstance {}>'.format(context)