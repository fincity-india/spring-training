package com.nocodesaas.practicemodule.repository;

import com.nocodesaas.practicemodule.model.User;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepositoryInf extends ReactiveCrudRepository<User,Long> {

}
