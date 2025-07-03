package com.test.config.config_server;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.config.server.EnableConfigServer;


@SpringBootApplication
//@EnableConfigServer It tells Spring Boot application to start the config server and expose endpoints like : http://localhost:8888/{application-name}/{profile}
@EnableConfigServer
public class ConfigServerApplication {

	public static void main(String[] args) {

		SpringApplication.run(ConfigServerApplication.class, args);
	}

}
