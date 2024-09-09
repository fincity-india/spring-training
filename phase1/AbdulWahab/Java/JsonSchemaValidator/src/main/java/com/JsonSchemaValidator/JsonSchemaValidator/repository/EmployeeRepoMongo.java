package com.JsonSchemaValidator.JsonSchemaValidator.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.JsonSchemaValidator.JsonSchemaValidator.model.EmployeeMongo;


public interface EmployeeRepoMongo extends MongoRepository<EmployeeMongo,Integer>{

}
