package com.schema_database_validator.repository;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import com.schema_database_validator.model.Schema;

public interface SchemaRepo extends MongoRepository<Schema,ObjectId>{

}
