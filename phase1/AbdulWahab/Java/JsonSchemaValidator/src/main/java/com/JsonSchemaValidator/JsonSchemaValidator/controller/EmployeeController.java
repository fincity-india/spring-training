package com.JsonSchemaValidator.JsonSchemaValidator.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.JsonSchemaValidator.JsonSchemaValidator.model.EmployeeMongo;
import com.JsonSchemaValidator.JsonSchemaValidator.model.EmployeeMysql;
import com.JsonSchemaValidator.JsonSchemaValidator.service.EmployeeService;



@RestController
public class EmployeeController {

	@Autowired
	private EmployeeService employeeService;
	
	@PostMapping("/addEmployeeMongo")
	public EmployeeMongo addEmployeeMongo(@RequestBody EmployeeMongo employee)
	{
		return employeeService.addDetailsMongo(employee);
	}
	
	@PostMapping("/addEmployeeMysql")
	public EmployeeMysql addEmployeeMysql(@RequestBody EmployeeMysql employee)
	{
		return employeeService.addDetailsMysql(employee);
	}
}
