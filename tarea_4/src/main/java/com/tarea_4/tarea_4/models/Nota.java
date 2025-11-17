package com.tarea_4.tarea_4.models;

import jakarta.persistence.*;


@Entity
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Integer nota;

    @ManyToOne
    @JoinColumn(name = "aviso_id") 
    private AvisoAdopcion aviso;

    public Integer getNota() {
        return nota;
    }
}
