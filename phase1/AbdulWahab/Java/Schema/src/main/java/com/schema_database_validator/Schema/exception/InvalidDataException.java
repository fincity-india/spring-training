package com.schema_database_validator.exception;

public class InvalidDataException extends RuntimeException{
	public InvalidDataException(String message) {
		super(message);
	}
}