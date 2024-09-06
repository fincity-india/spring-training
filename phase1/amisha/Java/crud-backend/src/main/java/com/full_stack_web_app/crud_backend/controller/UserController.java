package com.full_stack_web_app.crud_backend.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.full_stack_web_app.crud_backend.exception.UserNotFoundException;
import com.full_stack_web_app.crud_backend.model.User;
import com.full_stack_web_app.crud_backend.repository.UserRepository;

@RestController
@CrossOrigin("http://localhost:3000")
public class UserController{
    
	@Autowired
	UserRepository userRepository;
	
	@GetMapping("/users")
	public List<User> GetAllUsers() {
	    	return userRepository.findAll();
	    }
	
	@PostMapping("/user")
	public void AddnewUser(@RequestBody User NewUser) {
		System.out.println("called");
		userRepository.save(NewUser);
	}
	
	@GetMapping("/user/{id}")
	public User getUserById(@PathVariable Long id) {
		return userRepository.findById(id)
				.orElseThrow(()-> new UserNotFoundException(id));
}
	
	@PutMapping("/user/{id}")
	public User updateUser(@RequestBody User newUser,@PathVariable Long id) {
		return userRepository.findById(id).map(user-> {
			user.setUsername(newUser.getUsername());
			user.setEmail(newUser.getEmail());
			user.setName(newUser.getName());
			return userRepository.save(user);
		}).orElseThrow(()-> new UserNotFoundException(id));
	}
	
	@DeleteMapping("/user/{id}")
	public String deleteUser(@PathVariable Long id) {
		if(!userRepository.existsById(id)) {
			throw new UserNotFoundException(id);
		}
		userRepository.deleteById(id);
		return "User with id "+id+" has been deleted";
	}
	
	
}
