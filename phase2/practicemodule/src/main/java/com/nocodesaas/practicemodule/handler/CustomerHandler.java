package com.nocodesaas.practicemodule.handler;

import com.nocodesaas.practicemodule.dao.CustomerDoa;
import com.nocodesaas.practicemodule.dto.Customer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.server.ServerRequest;
import org.springframework.web.reactive.function.server.ServerResponse;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Service
public class CustomerHandler {

    @Autowired
    private CustomerDoa customerDoa;

    public Mono<ServerResponse> loadCustomer(ServerRequest request){
        Flux<Customer> customersList = customerDoa.getCustomersList();
        return ServerResponse.ok().body(customersList, Customer.class);
    }

    public Mono<ServerResponse> getCustomerById(ServerRequest request){
        int customerId = Integer.valueOf(request.pathVariable("customerId"));
        Mono<Customer> customer = customerDoa.getCustomersList().filter(c -> c.getId() == customerId).next();
        return ServerResponse.ok().body(customer, Customer.class);
    }

    public Mono<ServerResponse> saveCustomer(ServerRequest request){
        Mono<Customer> customerMono = request.bodyToMono(Customer.class);
        Mono<String> customerData = customerMono.map(dto -> dto.getId() + " : " + dto.getName());
        System.out.println(customerData);
        return ServerResponse.ok().body(customerData,String.class);
    }

}
