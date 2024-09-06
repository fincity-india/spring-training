package com.SpringMongoMySQL.SpringMongoMySQL.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.SpringMongoMySQL.SpringMongoMySQL.model.Student1;
import com.SpringMongoMySQL.SpringMongoMySQL.service.Student1Service;

@RestController
public class Student1Controller {
	
	@Autowired
	private Student1Service student1Service;
	
	@PostMapping("/addStudent1")
	public String addStudent1(@RequestBody Student1 student1)
	{
		student1Service.setDetails(student1);
		return "postedMongo";
	}
}
