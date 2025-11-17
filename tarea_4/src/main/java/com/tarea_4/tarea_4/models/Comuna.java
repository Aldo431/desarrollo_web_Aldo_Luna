package com.tarea_4.tarea_4.models;

import jakarta.persistence.*;

@Entity
@Table
public class Comuna {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private String nombre;

    @ManyToOne
    @JoinColumn(name = "region_id", nullable = false)
    private Region region;

    public Comuna() {}

    public Integer getId() { return id; }
    public String getNombre() { return nombre; }
    public Region getRegion() { return region; }
}
