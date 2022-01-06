/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.22
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/RegisterSecret'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./RegisterSecret'));
  } else {
    // Browser globals (root is window)
    if (!root.SelfManagedOsdu) {
      root.SelfManagedOsdu = {};
    }
    root.SelfManagedOsdu.RegisterSubscription = factory(root.SelfManagedOsdu.ApiClient, root.SelfManagedOsdu.RegisterSecret);
  }
}(this, function(ApiClient, RegisterSecret) {
  'use strict';

  /**
   * The RegisterSubscription model module.
   * @module model/RegisterSubscription
   * @version 0.11.0
   */

  /**
   * Constructs a new <code>RegisterSubscription</code>.
   * @alias module:model/RegisterSubscription
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>RegisterSubscription</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/RegisterSubscription} obj Optional instance to populate.
   * @return {module:model/RegisterSubscription} The populated <code>RegisterSubscription</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('name'))
        obj.name = ApiClient.convertToType(data['name'], 'String');
      if (data.hasOwnProperty('description'))
        obj.description = ApiClient.convertToType(data['description'], 'String');
      if (data.hasOwnProperty('topic'))
        obj.topic = ApiClient.convertToType(data['topic'], 'String');
      if (data.hasOwnProperty('pushEndpoint'))
        obj.pushEndpoint = ApiClient.convertToType(data['pushEndpoint'], 'String');
      if (data.hasOwnProperty('secret'))
        obj.secret = RegisterSecret.constructFromObject(data['secret']);
    }
    return obj;
  }

  /**
   * @member {String} name
   */
  exports.prototype.name = undefined;

  /**
   * @member {String} description
   */
  exports.prototype.description = undefined;

  /**
   * @member {String} topic
   */
  exports.prototype.topic = undefined;

  /**
   * @member {String} pushEndpoint
   */
  exports.prototype.pushEndpoint = undefined;

  /**
   * @member {module:model/RegisterSecret} secret
   */
  exports.prototype.secret = undefined;


  return exports;

}));
