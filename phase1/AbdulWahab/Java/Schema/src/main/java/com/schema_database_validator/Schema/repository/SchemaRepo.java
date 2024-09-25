package com.schema_database_validator.schema.repository;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import com.schema_database_validator.schema.model.Schema;

public interface SchemaRepo extends MongoRepository<Schema,ObjectId>{

}
