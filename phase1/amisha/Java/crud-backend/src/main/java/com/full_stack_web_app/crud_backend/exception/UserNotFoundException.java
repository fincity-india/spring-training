package com.full_stack_web_app.crud_backend.exception;

public class UserNotFoundException extends RuntimeException{
   public UserNotFoundException(Long id) {
	   super("Could not found the id "+id);
   }
}
