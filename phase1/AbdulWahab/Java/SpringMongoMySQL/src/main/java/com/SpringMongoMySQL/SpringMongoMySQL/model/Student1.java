package com.SpringMongoMySQL.SpringMongoMySQL.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

//import lombok.AllArgsConstructor;
//import lombok.Data;
//import lombok.NoArgsConstructor;

@Document
//@Data
//@NoArgsConstructor
//@AllArgsConstructor
public class Student1 {
	
	@Id
	private int id;
	
	private String name;
	
	private String address;
	
	public Student1() {
		
	}

	public Student1(int id, String name, String address) {
		super();
		this.id = id;
		this.name = name;
		this.address = address;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}
	
	
}

