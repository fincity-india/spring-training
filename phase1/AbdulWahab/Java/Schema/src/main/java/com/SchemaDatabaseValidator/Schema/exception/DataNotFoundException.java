package com.SchemaDatabaseValidator.Schema.exception;

public class DataNotFoundException extends RuntimeException{
	public DataNotFoundException(String message) {
		super(message);
	}
}