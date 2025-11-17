package com.tarea_4.tarea_4.models;

import jakarta.persistence.*;

@Entity
@Table
public class Region {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private String nombre;

    public Region() {}

    public Integer getId() { return id; }
    public String getNombre() { return nombre; }
}
