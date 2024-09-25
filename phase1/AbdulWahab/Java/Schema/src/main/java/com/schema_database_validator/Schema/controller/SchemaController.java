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

import com.schema_database_validator.schema.model.Schema;
import com.schema_database_validator.schema.service.SchemaService;
import com.fasterxml.jackson.databind.JsonNode;

import java.util.List;
import java.util.Map;

@RestController
public class SchemaController {

	@Autowired
	private SchemaService schemaService;

	@PostMapping("/addingSchema")
	public ResponseEntity<String> addSchema(@RequestBody Schema schema)
	{
		String id=schemaService.addSchemaToMongo(schema);
		return ResponseEntity.ok("JSON schema inserted successfully with id:"+id);
	}

	@GetMapping("/getSchema/{id}")
	public JsonNode getSchema(@PathVariable("id") String id)throws Exception
	{

		return schemaService.getSchemaMongo(id);
	}


	@GetMapping("/getAllSchema")
	public List<Map> getAllSchema()
	{
		return schemaService.getAllMongo();
	}

	@PutMapping("/updateSchema/{id}")
	public ResponseEntity<String> updateSchema(@RequestBody Schema schema, @PathVariable("id") String id)
	{
		schemaService.updateSchemaToMongo(schema,id);
		return ResponseEntity.ok("JSON schema updated successfully");
	}

	@DeleteMapping("/deleteSchema/{_id}")
	public ResponseEntity<String> deleteSchema(@PathVariable("_id") String id)
	{
		schemaService.deleteSchemaFromMongo(id);
		return ResponseEntity.ok("JSON schema deleted successfully with id: "+id);
	}
}
