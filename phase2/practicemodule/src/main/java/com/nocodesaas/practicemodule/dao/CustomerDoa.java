package com.nocodesaas.practicemodule.dao;

import com.nocodesaas.practicemodule.dto.Customer;
import org.springframework.stereotype.Component;
import reactor.core.publisher.Flux;

import java.io.InputStream;
import java.time.Duration;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@Component
public class CustomerDoa {
    public List<Customer> getCustomers(){
        return IntStream.rangeClosed(1,50)
                .peek(i -> System.out.println("processing count"))
                .mapToObj(i->new Customer(i,"cutstomer"+i))
                .collect(Collectors.toList());
    }

    public Flux<Customer> getCustomersStream(){
        return Flux.range(1,10)
                .delayElements(Duration.ofSeconds(1))
                .doOnNext(i -> System.out.println("processing count"))
                .map(i->new Customer(i,"cutstomer"+i));
    }

    public Flux<Customer> getCustomersList(){
        return Flux.range(1,50)
                .doOnNext(i -> System.out.println("processing count"))
                .map(i->new Customer(i,"cutstomer"+i));
    }
 }
