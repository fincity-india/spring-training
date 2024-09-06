package com.SpringMongoMySQL.SpringMongoMySQL.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.SpringMongoMySQL.SpringMongoMySQL.model.Student;
import com.SpringMongoMySQL.SpringMongoMySQL.service.StudentService;

@RestController
public class StudentController {
	
	@Autowired
	private StudentService studentService;
	
	@PostMapping("/addStudent")
	public String addStudent(@RequestBody Student student)
	{
		studentService.setDetails(student);
		return "posted";
	}
}
