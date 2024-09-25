package com.SchemaDatabaseValidator.Schema.validator;

import com.fasterxml.jackson.databind.JsonNode;

import java.util.ArrayList;
import java.util.List;

import org.springframework.context.annotation.Configuration;


@Configuration
public class CustomJsonSchemaValidator {

	public List<String> validateJson(JsonNode jsonData, JsonNode schema) {
		List<String> errors = new ArrayList<>();


		if (schema.has("required")) {
			for (JsonNode requiredField : schema.get("required")) {
				String fieldName = requiredField.asText();
				if (!jsonData.has(fieldName)) {
					errors.add("Missing required field: " + fieldName);
				}
			}
		}


		if (schema.has("properties")) {
			JsonNode properties = schema.get("properties");
			properties.fields().forEachRemaining(entry -> {
				String fieldName = entry.getKey();
				JsonNode fieldSchema = entry.getValue();
				if (jsonData.has(fieldName)) {
					JsonNode fieldValue = jsonData.get(fieldName);


					if (fieldSchema.has("type")) {
						String expectedType = fieldSchema.get("type").asText();
						if (!isTypeValid(fieldValue, expectedType)) {
							errors.add("Field '" + fieldName + "' should be of type " + expectedType);
						}
					}


					if (fieldSchema.has("minimum") && fieldValue.isInt()) {
						int min = fieldSchema.get("minimum").asInt();
						if (fieldValue.asInt() < min) {
							errors.add("Field '" + fieldName + "' should be >= " + min);
						}
					}


					if (fieldSchema.has("maximum") && (fieldValue.isInt()) || fieldValue.isDouble()) {
						int max = fieldSchema.get("maximum").asInt();
						if (fieldValue.asInt() > max) {
							errors.add("Field '" + fieldName + "' should be >= " + max);
						}
					}

				}
			});
		}

		return errors;
	}


	public boolean isTypeValid(JsonNode fieldValue, String expectedType) {
		switch (expectedType) {
		case "string":
			return fieldValue.isTextual();
		case "integer":
			return fieldValue.isInt();
		case "number":
			return fieldValue.isDouble() || fieldValue.isInt();
		case "boolean":
			return fieldValue.isBoolean();
		case "object":
			return fieldValue.isObject();
		case "array":
			return fieldValue.isArray();
		default:
			return false;
		}
	}
}

