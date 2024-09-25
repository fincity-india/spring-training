package com.schema_database_validator.schema.exception;

public class SchemaNotFoundException extends RuntimeException{
	public SchemaNotFoundException(String message) {
		super(message);
	}
}
