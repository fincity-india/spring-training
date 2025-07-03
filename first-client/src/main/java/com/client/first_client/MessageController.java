package com.client.first_client;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MessageController {

    @Value("${message:Default message from code}")
    private String message;

    @GetMapping("/message")
    public String getMessage() {
        return message;
    }
}
