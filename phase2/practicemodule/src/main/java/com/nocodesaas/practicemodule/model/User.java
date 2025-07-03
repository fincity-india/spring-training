package com.nocodesaas.practicemodule.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Table;

@Data
@AllArgsConstructor
@RequiredArgsConstructor
@Table("users")
public class User {

    @Id
    private Long id;
    private String name;
    private String email;
}
