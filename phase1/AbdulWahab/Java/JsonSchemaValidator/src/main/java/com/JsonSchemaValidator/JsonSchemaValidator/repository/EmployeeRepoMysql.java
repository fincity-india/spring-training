package com.JsonSchemaValidator.JsonSchemaValidator.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.JsonSchemaValidator.JsonSchemaValidator.model.EmployeeMysql;


public interface EmployeeRepoMysql extends JpaRepository<EmployeeMysql,Integer>{
	
}
