package com.nocodesaas.practicemodule.service;

import com.nocodesaas.practicemodule.dao.CustomerDoa;
import com.nocodesaas.practicemodule.dto.Customer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;

import java.util.List;

@Service
public class CustomerService {

    @Autowired
    private CustomerDoa customerDoa;

    public List<Customer> loadAllCustomers(){
        long start  = System.currentTimeMillis();
        List<Customer> customers = customerDoa.getCustomers();
        long end  = System.currentTimeMillis();
        System.out.println("loadAllCustomers total execution time: " + (end-start));
        return  customers;
    }

    public Flux<Customer> loadAllCustomersstream(){
        long start  = System.currentTimeMillis();
        Flux<Customer> customers = customerDoa.getCustomersStream();
        long end  = System.currentTimeMillis();
        System.out.println("loadAllCustomers total execution time: " + (end-start));
        return  customers;
    }

}
