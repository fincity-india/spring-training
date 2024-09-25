package com.schema_database_validator.schema.exception;

public class DataNotFoundException extends RuntimeException{
	public DataNotFoundException(String message) {
		super(message);
	}
}