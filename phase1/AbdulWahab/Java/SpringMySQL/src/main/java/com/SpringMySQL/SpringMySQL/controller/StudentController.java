package com.SpringMySQL.SpringMySQL.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.SpringMySQL.SpringMySQL.model.Student;
import com.SpringMySQL.SpringMySQL.service.StudentService;

@RestController
public class StudentController {

	@Autowired
	private StudentService studentService;
	
	@PostMapping("/addStudent")
	public String addStudent(@RequestBody Student student)
	{
		studentService.saveDetails(student);
		return "Posted";
	}
}
