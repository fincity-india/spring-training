package com.SpringMongoMySQL.SpringMongoMySQL.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.SpringMongoMySQL.SpringMongoMySQL.model.Student;

public interface StudentRepo extends JpaRepository<Student,Integer>{

}
