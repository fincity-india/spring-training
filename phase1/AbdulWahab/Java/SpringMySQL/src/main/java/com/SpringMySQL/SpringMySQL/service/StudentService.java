package com.SpringMySQL.SpringMySQL.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.SpringMySQL.SpringMySQL.model.Student;
import com.SpringMySQL.SpringMySQL.repository.StudentRepo;

@Service
public class StudentService {
	
	@Autowired
	private StudentRepo studentRepo;
	
	public Student saveDetails(Student student)
	{
		return studentRepo.save(student);
	}
}
