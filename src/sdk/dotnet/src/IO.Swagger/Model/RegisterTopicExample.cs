/* 
 * self-managed-osdu
 *
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// RegisterTopicExample
    /// </summary>
    [DataContract]
    public partial class RegisterTopicExample :  IEquatable<RegisterTopicExample>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="RegisterTopicExample" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="kind">kind.</param>
        /// <param name="op">op.</param>
        public RegisterTopicExample(string id = default(string), string kind = default(string), string op = default(string))
        {
            this.Id = id;
            this.Kind = kind;
            this.Op = op;
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public string Id { get; set; }

        /// <summary>
        /// Gets or Sets Kind
        /// </summary>
        [DataMember(Name="kind", EmitDefaultValue=false)]
        public string Kind { get; set; }

        /// <summary>
        /// Gets or Sets Op
        /// </summary>
        [DataMember(Name="op", EmitDefaultValue=false)]
        public string Op { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class RegisterTopicExample {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Kind: ").Append(Kind).Append("\n");
            sb.Append("  Op: ").Append(Op).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as RegisterTopicExample);
        }

        /// <summary>
        /// Returns true if RegisterTopicExample instances are equal
        /// </summary>
        /// <param name="input">Instance of RegisterTopicExample to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(RegisterTopicExample input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.Kind == input.Kind ||
                    (this.Kind != null &&
                    this.Kind.Equals(input.Kind))
                ) && 
                (
                    this.Op == input.Op ||
                    (this.Op != null &&
                    this.Op.Equals(input.Op))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.Kind != null)
                    hashCode = hashCode * 59 + this.Kind.GetHashCode();
                if (this.Op != null)
                    hashCode = hashCode * 59 + this.Op.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
