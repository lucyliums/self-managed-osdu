# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RegisterDdmsInterface(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_type': 'str',
        'schema': 'object'
    }

    attribute_map = {
        'entity_type': 'entityType',
        'schema': 'schema'
    }

    def __init__(self, entity_type=None, schema=None, _configuration=None):  # noqa: E501
        """RegisterDdmsInterface - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._entity_type = None
        self._schema = None
        self.discriminator = None

        if entity_type is not None:
            self.entity_type = entity_type
        self.schema = schema

    @property
    def entity_type(self):
        """Gets the entity_type of this RegisterDdmsInterface.  # noqa: E501


        :return: The entity_type of this RegisterDdmsInterface.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this RegisterDdmsInterface.


        :param entity_type: The entity_type of this RegisterDdmsInterface.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                entity_type is not None and not re.search(r'^[A-Za-z0-9-]{2,50}', entity_type)):  # noqa: E501
            raise ValueError(r"Invalid value for `entity_type`, must be a follow pattern or equal to `/^[A-Za-z0-9-]{2,50}/`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def schema(self):
        """Gets the schema of this RegisterDdmsInterface.  # noqa: E501


        :return: The schema of this RegisterDdmsInterface.  # noqa: E501
        :rtype: object
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this RegisterDdmsInterface.


        :param schema: The schema of this RegisterDdmsInterface.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and schema is None:
            raise ValueError("Invalid value for `schema`, must not be `None`")  # noqa: E501

        self._schema = schema

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RegisterDdmsInterface, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegisterDdmsInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterDdmsInterface):
            return True

        return self.to_dict() != other.to_dict()
