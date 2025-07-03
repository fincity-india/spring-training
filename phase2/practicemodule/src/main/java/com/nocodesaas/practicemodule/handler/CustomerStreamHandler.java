package com.nocodesaas.practicemodule.handler;

import com.nocodesaas.practicemodule.dao.CustomerDoa;
import com.nocodesaas.practicemodule.dto.Customer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.server.ServerRequest;
import org.springframework.web.reactive.function.server.ServerResponse;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Service
public class CustomerStreamHandler {

    @Autowired
    private CustomerDoa customerDoa;
    public Mono<ServerResponse> getcustomer(ServerRequest request){
        Flux<Customer> customersStream = customerDoa.getCustomersStream();
        return ServerResponse.ok().contentType(MediaType.TEXT_EVENT_STREAM).body(customersStream,Customer.class);
    }
}
