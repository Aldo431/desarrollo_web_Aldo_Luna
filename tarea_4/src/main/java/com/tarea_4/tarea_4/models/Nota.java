package com.tarea_4.tarea_4.models;

import jakarta.persistence.*;


@Entity
public class Nota {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private Integer nota;

    @ManyToOne
    @JoinColumn(name = "aviso_id", nullable = false)
    private AvisoAdopcion aviso;

    public Nota() {}

    public Nota(Integer nota, AvisoAdopcion aviso) {
        this.nota = nota;
        this.aviso = aviso;
    }

    public Long getId() {
        return id;
    }

    public Integer getNota() {
        return nota;
    }

    public AvisoAdopcion getAviso() {
        return aviso;
    }
    public static boolean validateNota(Integer nota) {
    return nota != null && nota >= 1 && nota <= 7;
    }
}