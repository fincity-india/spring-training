package com.SchemaDatabaseValidator.Schema.model;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import com.fasterxml.jackson.databind.JsonNode;

@Document
public class Schema {
	
	private ObjectId _id;
	private String schemaName;
	private Object schema;
	private int version;
	
	@CreatedDate
    private Date createdAt;

    @LastModifiedDate
    private Date updatedAt;
    
    public Schema() {
    	
    }

	public Schema(ObjectId _id, String schemaName, Object schema, int version, Date createdAt, Date updatedAt) {
		super();
		this._id = _id;
		this.schemaName = schemaName;
		this.schema = schema;
		this.version = version;
		this.createdAt = createdAt;
		this.updatedAt = updatedAt;
	}

	public ObjectId get_id() {
		return _id;
	}

	public void set_id(ObjectId _id) {
		this._id = _id;
	}

	public String getSchemaName() {
		return schemaName;
	}

	public void setSchemaName(String schemaName) {
		this.schemaName = schemaName;
	}

	public Object getSchema() {
		return schema;
	}

	public void setSchema(Object schema) {
		this.schema = schema;
	}

	public int getVersion() {
		return version;
	}

	public void setVersion(int version) {
		this.version = version;
	}

	public Date getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}

	public Date getUpdatedAt() {
		return updatedAt;
	}

	public void setUpdatedAt(Date updatedAt) {
		this.updatedAt = updatedAt;
	}
    
    
}
