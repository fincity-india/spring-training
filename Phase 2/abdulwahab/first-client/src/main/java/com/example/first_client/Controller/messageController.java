package com.example.first_client.Controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class messageController {

    @Value("${message:Default message}")
    private String message;

    @Value("${firstName:No Name Found}")
    private String firstName;

    @GetMapping("/message")
    public String getMessage() {
        return message;
    }

    @GetMapping("/call")
    public String call() {
        return "hello "+firstName;
    }
}
