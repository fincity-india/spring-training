package com.full_stack_web_app.crud_backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.full_stack_web_app.crud_backend.model.User;

public interface UserRepository extends JpaRepository<User,Long>{

}
