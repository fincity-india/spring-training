package com.full_stack_web_app.crud_backend.repository;

import com.full_stack_web_app.crud_backend.model.MongoUser;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface MongoUserRepository extends MongoRepository<MongoUser, Long> {
}
