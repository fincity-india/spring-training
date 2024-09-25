package com.schema_database_validator.schema.exception;

public class InvalidDataException extends RuntimeException{
	public InvalidDataException(String message) {
		super(message);
	}
}