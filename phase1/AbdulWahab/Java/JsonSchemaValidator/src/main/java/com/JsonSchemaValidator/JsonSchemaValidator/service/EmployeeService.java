package com.JsonSchemaValidator.JsonSchemaValidator.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.JsonSchemaValidator.JsonSchemaValidator.model.EmployeeMongo;
import com.JsonSchemaValidator.JsonSchemaValidator.model.EmployeeMysql;
import com.JsonSchemaValidator.JsonSchemaValidator.repository.EmployeeRepoMongo;
import com.JsonSchemaValidator.JsonSchemaValidator.repository.EmployeeRepoMysql;



@Service
public class EmployeeService {
	
	@Autowired
	private EmployeeRepoMongo employeeRepoMongo;
	
	@Autowired
	private EmployeeRepoMysql employeeRepoMysql;
	
	public EmployeeMongo addDetailsMongo(EmployeeMongo employee)
	{
		return employeeRepoMongo.save(employee);
	}
	
	public EmployeeMysql addDetailsMysql(EmployeeMysql employee)
	{
		return employeeRepoMysql.save(employee);
	}
}
