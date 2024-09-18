package com.SchemaDatabaseValidator.Schema.service;


import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import com.SchemaDatabaseValidator.Schema.exception.SchemaNotFoundException;
import com.SchemaDatabaseValidator.Schema.model.Schema;
import com.SchemaDatabaseValidator.Schema.repository.SchemaRepo;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.Map;
import java.util.List;

@Service
public class SchemaService {

	public String collectionName="schema";

	@Autowired
	private SchemaRepo schemaRepo;

	@Autowired
	private MongoTemplate mongoTemplate;
	ObjectMapper objectMapper = new ObjectMapper();

	public String addSchemaToMongo(Schema schema)
	{
		schema.setVersion(0);
		return schemaRepo.save(schema).get_id().toString();
	}

	public JsonNode getSchemaMongo(String id) throws Exception {
		Query query = new Query();
		query.addCriteria(Criteria.where("_id").is(new ObjectId(id)));

		Schema schemaDoc = mongoTemplate.findById(query, Schema.class, collectionName);

		if (schemaDoc == null) {
			throw new SchemaNotFoundException("Schema not found for schemaId: " + id);
		}

		JsonNode jsonSchema;
		try {
			jsonSchema = objectMapper.valueToTree(schemaDoc.getSchema());
		} catch (Exception exception) {
			throw new Exception("Failed to parse schema JSON", exception);
		}

		return jsonSchema;
	}


	public List<Map> getAllMongo()
	{
		return mongoTemplate.findAll(Map.class, collectionName);
	}

	public void updateSchemaToMongo(Schema schema,String id) {

		ObjectId _id = new ObjectId(id);
		Schema newSchema = schemaRepo.findById(_id)
				.orElseThrow(() -> new SchemaNotFoundException("User not found"));

		newSchema.setSchemaName(schema.getSchemaName());
		newSchema.setSchema(schema.getSchema());
		newSchema.setVersion(schema.getVersion()+1);

		schemaRepo.save(newSchema);
	}

	public void deleteSchemaFromMongo(String id)
	{
		Query query = new Query();
		query.addCriteria(Criteria.where("_id").is(new ObjectId(id)));
		mongoTemplate.remove(query, Schema.class, collectionName);
	}

	public JsonNode convertMapToJsonNode(Map<String, Object> schemaMap) {
		return objectMapper.valueToTree(schemaMap);
	}
}
