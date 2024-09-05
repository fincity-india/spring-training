package com.SpringMySQL.SpringMySQL.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.SpringMySQL.SpringMySQL.model.Student;

public interface StudentRepo extends JpaRepository<Student,Integer>{
	
}
