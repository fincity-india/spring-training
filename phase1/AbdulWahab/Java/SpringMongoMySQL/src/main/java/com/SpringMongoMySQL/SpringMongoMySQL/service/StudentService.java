package com.SpringMongoMySQL.SpringMongoMySQL.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.SpringMongoMySQL.SpringMongoMySQL.model.Student;
import com.SpringMongoMySQL.SpringMongoMySQL.repository.StudentRepo;

@Service
public class StudentService {
	
	@Autowired
	private StudentRepo studentRepo;
	
	public Student setDetails(Student student)
	{
		return studentRepo.save(student);
	}
}
