package com.modlix.config_client.service;

import com.modlix.config_client.model.Sample;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class ClientService {

    @Value("${service.name}")
    private String serviceName;

    public Sample getServiceInfo() {
        return new Sample(serviceName);
    }
}
