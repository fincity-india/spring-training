package com.nocodesaas.practicemodule.service;

import com.nocodesaas.practicemodule.model.User;
import com.nocodesaas.practicemodule.repository.UserRepository;
import com.nocodesaas.practicemodule.repository.UserRepositoryInf;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Service
public class UserService {


    private UserRepositoryInf userRepository;

     public UserService(UserRepositoryInf userRepository){
         this.userRepository = userRepository;
     }

    public Mono<User> findByUsernameById(Long id) {
        return userRepository.findById(id);
    }

    public Mono<User> save(User user) {
        return userRepository.save(user);
    }

    public Flux<User> getAllusers(){
        return userRepository.findAll();
    }

    public Mono<Void>  deleteUserById(Long id) {
        return userRepository.deleteById(id);
    }

    public Mono<User> updateUser(Long id, User user) {
        return userRepository.findById(id).flatMap(existingUser->{
            existingUser.setName(user.getName());
            existingUser.setEmail(user.getEmail());
            return userRepository.save(existingUser);
        });
    }


}
