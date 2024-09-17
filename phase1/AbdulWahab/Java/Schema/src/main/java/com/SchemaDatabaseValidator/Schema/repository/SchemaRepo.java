package com.SchemaDatabaseValidator.Schema.repository;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import com.SchemaDatabaseValidator.Schema.model.Schema;

public interface SchemaRepo extends MongoRepository<Schema,ObjectId>{

}
