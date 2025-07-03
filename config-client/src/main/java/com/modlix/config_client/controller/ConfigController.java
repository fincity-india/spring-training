package com.modlix.config_client.controller;

import com.modlix.config_client.model.Sample;
import com.modlix.config_client.service.ClientService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/message")
@Slf4j
@RequiredArgsConstructor
public class ConfigController {


    private final ClientService clientService;

    @GetMapping
    public Sample getServiceInfo() {
        Sample sample = clientService.getServiceInfo();
        log.info("Fetched service info: {}", sample);
        return sample;
    }
}
