package com.nocodesaas.practicemodule.controller;

import com.nocodesaas.practicemodule.dto.Customer;
import com.nocodesaas.practicemodule.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

import java.util.List;

@RestController
@RequestMapping("/customers")
public class CustomerController {

    @Autowired
    public CustomerService customerService;

   @GetMapping("/")
    public List<Customer> getCustomers(){
        return customerService.loadAllCustomers();
    }

    @GetMapping(value = "/stream",produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<Customer> getCustomersStream(){
        return customerService.loadAllCustomersstream();
    }
}
