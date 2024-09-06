package com.full_stack_web_app.crud_backend.controller;

import com.full_stack_web_app.crud_backend.model.MongoUser;
import com.full_stack_web_app.crud_backend.repository.MongoUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin("http://localhost:3000")
public class MongoUserController {

    @Autowired
    private MongoUserRepository mongoUserRepository;

    @GetMapping("/mongo-users")
    public List<MongoUser> getAllMongoUsers() {
        return mongoUserRepository.findAll();
    }

    @PostMapping("/mongo-user")
    public void addNewMongoUser(@RequestBody MongoUser newMongoUser) {
        mongoUserRepository.save(newMongoUser);
    }

    @GetMapping("/mongo-user/{id}")
    public MongoUser getMongoUserById(@PathVariable Long id) {
        return mongoUserRepository.findById(id).orElse(null);
    }

    @PutMapping("/mongo-user/{id}")
    public MongoUser updateMongoUser(@RequestBody MongoUser newMongoUser, @PathVariable Long id) {
        return mongoUserRepository.findById(id).map(user -> {
            user.setUsername(newMongoUser.getUsername());
            user.setEmail(newMongoUser.getEmail());
            user.setName(newMongoUser.getName());
            return mongoUserRepository.save(user);
        }).orElse(null);
    }

    @DeleteMapping("/mongo-user/{id}")
    public String deleteMongoUser(@PathVariable Long id) {
        mongoUserRepository.deleteById(id);
        return "MongoUser with id " + id + " has been deleted";
    }
}
