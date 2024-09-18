package com.SchemaDatabaseValidator.Schema.service;

import java.util.List;
import java.util.Map;

import org.bson.Document;
import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import com.SchemaDatabaseValidator.Schema.exception.DataNotFoundException;
import com.SchemaDatabaseValidator.Schema.exception.InvalidDataException;
import com.SchemaDatabaseValidator.Schema.validator.CustomJsonSchemaValidator;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;


@Service
public class DataService {

	public String collectionName="data";
	@Autowired
	private CustomJsonSchemaValidator jsonSchema;

	@Autowired
	private MongoTemplate mongoTemplate;

	ObjectMapper objectMapper=new ObjectMapper();

	public String addToMongo(JsonNode jsonNode, JsonNode schema) throws Exception{

		List<String> errors = jsonSchema.validateJson(jsonNode,schema);
		if (!errors.isEmpty()) {
			throw new InvalidDataException("Invalid JSON data: " + errors.toString());
		}

		Document document = Document.parse(jsonNode.toString());

		return mongoTemplate.insert(document, collectionName).get("_id").toString();
	}

	public JsonNode getDataFromMongo(String id)throws Exception
	{

		Query query = new Query();
		query.addCriteria(Criteria.where("_id").is(new ObjectId(id)));
		Map<String, Object> map = (Map<String, Object>) mongoTemplate.findById(new ObjectId(id), Map.class, collectionName);
		JsonNode jsonSchema = convertMapToJsonNode(map);
		if (jsonSchema.isNull()) {
			throw new DataNotFoundException("Data not found for dataId: " + id);
		}
		return jsonSchema;
	}

	public void updateDataToMongo(JsonNode data,String id) {

		try {
			Document document = Document.parse(data.toString());
			document.append("_id",new ObjectId(id));
			mongoTemplate.save(document, collectionName);
		} catch (Exception exception) {
			exception.printStackTrace();
		}

	}

	public void deleteDataFromMongo(String id)
	{
		Query query = new Query();
		query.addCriteria(Criteria.where("_id").is(new ObjectId(id)));
		mongoTemplate.remove(query, Map.class, collectionName);
	}

	public JsonNode convertMapToJsonNode(Map<String, Object> schemaMap) {
		return objectMapper.valueToTree(schemaMap);
	}


}
