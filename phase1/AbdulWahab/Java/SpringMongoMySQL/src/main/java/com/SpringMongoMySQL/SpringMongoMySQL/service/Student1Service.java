package com.SpringMongoMySQL.SpringMongoMySQL.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.SpringMongoMySQL.SpringMongoMySQL.model.Student1;
import com.SpringMongoMySQL.SpringMongoMySQL.repository.Student1Repo;

@Service
public class Student1Service {

	@Autowired
	private Student1Repo student1Repo;
	
	public Student1 setDetails(Student1 student1)
	{
		return student1Repo.save(student1);
	}
}
