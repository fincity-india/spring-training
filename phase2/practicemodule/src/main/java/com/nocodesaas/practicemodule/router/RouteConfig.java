package com.nocodesaas.practicemodule.router;

import com.nocodesaas.practicemodule.handler.CustomerHandler;
import com.nocodesaas.practicemodule.handler.CustomerStreamHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.server.RouterFunction;
import org.springframework.web.reactive.function.server.RouterFunctions;
import org.springframework.web.reactive.function.server.ServerResponse;

@Configuration
public class RouteConfig {

    @Autowired
    private CustomerHandler customerHandler;

    @Autowired
    private CustomerStreamHandler customerStreamHandler;


    @Bean
    public RouterFunction<ServerResponse> routFunction(){
        return RouterFunctions.route()
                .GET("/router/customer",customerHandler::loadCustomer)
                .GET("/router/customer/Stream",customerStreamHandler::getcustomer)
                .GET("router/customer/stream/findUser/{customerId}",customerHandler::getCustomerById)
                .POST("router/customer/stream/saveuser",customerHandler::saveCustomer)
                .build();
    }

}
