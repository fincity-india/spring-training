package com.schema_database_validator.schema.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.schema_database_validator.schema.service.DataService;
import com.fasterxml.jackson.databind.JsonNode;

@RestController
public class DataController {


	@Autowired
	private DataService dataService;;

	@Autowired
	private SchemaController schemaController;

	@PostMapping("/insert/{_id}")
	public ResponseEntity<String> insertJson(@PathVariable("_id") String id,@RequestBody JsonNode jsonData) {
		try {
			JsonNode schema=schemaController.getSchema(id);
			String dataId=dataService.addToMongo(jsonData,schema);
			return ResponseEntity.ok("JSON data inserted successfully with Id:"+dataId);
		} catch (Exception e) {
			return ResponseEntity.status(500).body("Failed to insert JSON: " + e.getMessage());
		}
	}

	@GetMapping("getData/{id}")
	public JsonNode getDataById(@PathVariable("id") String id) {
		try {
			return dataService.getDataFromMongo(id);
		} catch (Exception exception) {
			exception.printStackTrace();
		}
		return null;
	}

	@PutMapping("/updateData/{id}")
	public ResponseEntity<String> updateData(@RequestBody JsonNode data, @PathVariable("id") String id)
	{
		dataService.updateDataToMongo(data,id);
		return ResponseEntity.ok("JSON schema updated successfully");
	}

	@DeleteMapping("/deleteData/{_id}")
	public ResponseEntity<String> deleteSchema(@PathVariable("_id") String id)
	{
		dataService.deleteDataFromMongo(id);
		return ResponseEntity.ok("JSON schema deleted successfully with id: "+id);
	}
}
