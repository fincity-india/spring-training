package com.nocodesaas.practicemodule.controller;

import com.nocodesaas.practicemodule.model.User;
import com.nocodesaas.practicemodule.service.UserService;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/user")
public class UserController {


    private UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/{id}")
    public Mono<User> getUserById(@PathVariable Long id){
        return userService.findByUsernameById(id);
    }

    @PostMapping("/saveUser")
    public Mono<User> createUser(@RequestBody User user){
        return userService.save(user);
    }

    @GetMapping("/getAllUser")
    public Flux<User> getAllUser(){
        return userService.getAllusers();
    }

    @PutMapping("/updateUser/{id}")
    public Mono<User> updateUser(@PathVariable Long id ,@RequestBody User user){
        return  userService.updateUser(id,user);
    }

    @DeleteMapping("/deleteUser/{id}")
    public Mono<Void> delteUserById(@PathVariable Long id){
        System.out.println("id : "+id);
         return userService.deleteUserById(id);
    }

}
