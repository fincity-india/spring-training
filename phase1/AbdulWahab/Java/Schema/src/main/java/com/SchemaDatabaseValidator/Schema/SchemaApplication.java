package com.SchemaDatabaseValidator.Schema;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.mongodb.config.EnableMongoAuditing;

@SpringBootApplication
@EnableMongoAuditing
public class SchemaApplication {

	public static void main(String[] args) {
		SpringApplication.run(SchemaApplication.class, args);
	}

}
